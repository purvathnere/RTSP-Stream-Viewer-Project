 # RTSP Stream Viewer
A full-stack web application to view live RTSP streams directly in the browser.
This project allows users to input RTSP stream URLs and watch multiple streams simultaneously with basic controls (play/pause). 
Built with React.js (frontend), Django (backend), and FFmpeg for RTSP to HLS conversion.
#Tech Stack
Layer	Technology
Frontend	React.js, HLS.js
Backend	Django, Django Channels
Media Proc.	FFmpeg
Streaming	HLS (.m3u8)
Deployment	GitHub Pages (frontend), Heroku/Vercel (backend)
#ackend Setup (Django + Channels)
```
# Clone the repo
git clone https://github.com/purvathnere/RTSP-Stream-Viewer-Project
cd rtsp-stream-viewer/backend

# Create virtual environment
python -m venv env
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Django development server
python manage.py runserver

```
Server start at: http://127.0.0.1:8000
## Frontend Setup (React)
```
cd ../frontend

# Install dependencies
npm install

# Start development server
npm start
```
Open your browser and visit: http://localhost:3000

Open in Browser to check URL is correct or not( it downaload)
http://127.0.0.1:8000/media/streams/<stream-id>/index.m3u8

## FFmpeg Setup (for RTSP to HLS)
`ffmpeg -version
`
# convert RTSP stream to HLS format:
`
mkdir media/streams/<stream-id>
ffmpeg -rtsp_transport tcp -analyzeduration 10000000 -probesize 10000000 \
-i "<rtsp-url>" -c:v copy -hls_time 10 -hls_list_size 6 -hls_flags delete_segments \
media/streams/<stream-id>/index.m3u8
`

##  Stream Directory Creation (Windows)

folder creation
`
New-Item -ItemType Directory -Path "C:\Users\HP\OneDrive\Desktop\colne rstp\rtsp-stream-viewer\media\streams\<stream-id>" -Force`

##  RTSP to HLS Conversion (FFmpeg)

Use `FFmpeg` to convert RTSP stream to HLS format:

`
ffmpeg -rtsp_transport tcp -analyzeduration 10000000 -probesize 10000000 \
-i "rtsp://admin:admin123@49.248.155.178:555/cam/realmonitor?channel=1&subtype=0" \
-c:v copy -hls_time 10 -hls_list_size 6 -hls_flags delete_segments \
"C:\Users\HP\OneDrive\Desktop\colne rstp\rtsp-stream-viewer\media\streams\<stream-id>\index.m3u8 `


 Backend run = python manage.py runserver ( Django )
 frontend = npm start ( React )
