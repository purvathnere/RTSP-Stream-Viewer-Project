import subprocess
import os

def start_stream(rtsp_url, stream_id):
    # Output folder banao
    output_dir = os.path.join('media', 'streams', stream_id)
    os.makedirs(output_dir, exist_ok=True)

    # Output file paths
    output_path = os.path.join(output_dir, 'index.m3u8')
    log_path = os.path.join(output_dir, 'ffmpeg.log')

    # FFmpeg command with probe settings to fix codec detection
    command = [
        "ffmpeg",
        "-analyzeduration", "10000000",
        "-probesize", "10000000",
        "-i", rtsp_url,
        "-c:v", "libx264",
        "-hls_time", "2",
        "-hls_list_size", "5",
        "-f", "hls",
        output_path
    ]

    # Run ffmpeg and log output
    with open(log_path, 'wb') as log_file:
        process = subprocess.Popen(command, stdout=log_file, stderr=log_file)

    print(f"FFmpeg started with PID: {process.pid}, logging to {log_path}")
    return process

if __name__ == "__main__":
    rtsp_url = "rtsp://admin:admin123@49.248.155.178:555/cam/realmonitor?channel=1&subtype=1"
    stream_id = "camera1"  # Fixed stream id

    process = start_stream(rtsp_url, stream_id)
