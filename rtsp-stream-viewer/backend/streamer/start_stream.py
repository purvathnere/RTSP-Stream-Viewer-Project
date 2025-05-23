from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent.parent

def start_stream(rtsp_url, stream_id):
    output_dir = BASE_DIR / "media" / "streams" / stream_id
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "index.m3u8"
    
    command = [
        "ffmpeg",
        "-i", rtsp_url,
        "-c:v", "libx264",
        "-hls_time", "2",
        "-hls_list_size", "5",
        "-f", "hls",
        str(output_path)
    ]
    
    logfile = output_dir / "ffmpeg.log"
    with open(logfile, "wb") as log:
        return subprocess.Popen(command, stdout=log, stderr=log)
