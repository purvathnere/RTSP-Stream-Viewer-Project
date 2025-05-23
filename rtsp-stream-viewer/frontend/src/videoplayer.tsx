import React, { useEffect, useRef } from 'react';
import Hls from 'hls.js';

interface VideoPlayerProps {
  streamId: string;
}

const backendUrl = 'http://localhost:8000'; 
const VideoPlayer: React.FC<VideoPlayerProps> = ({ streamId }) => {
  const videoRef = useRef<HTMLVideoElement | null>(null);

  useEffect(() => {
    const video = videoRef.current;
    if (!video || !streamId) return;

    if (Hls.isSupported()) {
      const hls = new Hls();
     hls.loadSource(`${backendUrl}/media/streams/${streamId}/index.m3u8`);
    

     
      hls.attachMedia(video);
      hls.on(Hls.Events.MANIFEST_PARSED, () => {
        video.play();
      });
    } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
     
      
video.src = `${backendUrl}/media/streams/${streamId}/index.m3u8`;

      video.addEventListener('loadedmetadata', () => {
        video.play();
      });
    }
  }, [streamId]);

  return <video ref={videoRef} controls style={{ width: '100%', maxWidth: '600px' }} />;
};

export default VideoPlayer;
