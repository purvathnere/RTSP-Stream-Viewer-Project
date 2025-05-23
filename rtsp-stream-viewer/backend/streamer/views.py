from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .models import StreamSession
from .serializers import StreamSessionSerializer
import subprocess
import os
from django.conf import settings

def show_stream_page(request):
    return render(request, 'stream.html')

def home(request):
    return HttpResponse("Welcome to RTSP Stream Viewer")

def stream_video(request, stream_id):
    return HttpResponse(f"Streaming video for stream ID: {stream_id}")

class StreamSessionViewSet(viewsets.ModelViewSet):
    queryset = StreamSession.objects.all()
    serializer_class = StreamSessionSerializer

    @action(detail=True, methods=['post'])
    def stop(self, request, pk=None):
        try:
            stream = self.get_object()
            stream.is_active = False
            stream.save()
            return Response({'status': 'stream stopped'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def start_stream(request):
    stream_id = request.data.get('stream_id')
    rtsp_url = request.data.get('rtsp_url')

    if not stream_id or not rtsp_url:
        return Response({'error': 'Missing stream_id or rtsp_url'}, status=status.HTTP_400_BAD_REQUEST)

    output_dir = os.path.join(settings.MEDIA_ROOT, 'streams', stream_id)
    os.makedirs(output_dir, exist_ok=True)

    command = [
        "ffmpeg",
        "-i", rtsp_url,
        "-c:v", "libx264",
        "-hls_time", "2",
        "-hls_list_size", "5",
        "-f", "hls",
        os.path.join(output_dir, "index.m3u8")
    ]

    try:
        subprocess.Popen(command)
        return Response({'status': 'Stream started'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Yeh updated stream_view jo stream_id lega aur template me stream_url pass karega
def stream_view(request, stream_id='camera1'):
    stream_url = f'/media/streams/{stream_id}/index.m3u8'  # Dynamic path according to stream_id
    return render(request, 'stream.html', {'stream_url': stream_url})
