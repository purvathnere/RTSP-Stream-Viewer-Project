RTSP live stream viewer using React and Django
# 📡 RTSP Stream Viewer
A full-stack web application to **view live RTSP streams** directly in the browser.
This project allows users to input RTSP stream URLs and watch multiple streams simultaneously with basic controls (play/pause). Built with **React.js (frontend)**, **Django (backend)**, and **FFmpeg** for RTSP to HLS conversion.
#Features
✅ Input field to add RTSP URLs

✅ View multiple streams in a grid

✅ Play/Pause controls

✅ Real-time stream via WebSocket (Django Channels)

✅ Responsive UI using React

✅ FFmpeg-powered stream processing
#🔧 Tech Stack
Layer	Technology
Frontend	React.js, HLS.js
Backend	Django, Django Channels
Media Proc	FFmpeg
Streaming	HLS (.m3u8)
Deployment	GitHub Pages (frontend), Heroku/Vercel (backend)
#Backend Setup (Django + Channels)
Clone the repo:
git clone https://github.com/purvathnere/RTSP-Stream-Viewer-Project
cd rtsp-stream-viewer/backend
Create virtual environment:
python -m venv env
env\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Run the server:
python manage.py runserver
✅ It should start at: http://127.0.0.1:8000/
 FFmpeg Setup
 ffmpeg -version
 Start the HLS stream:
mkdir media/streams/<stream-id>
ffmpeg -rtsp_transport tcp -analyzeduration 10000000 -probesize 10000000 \
-i "<rtsp-url>" -c:v copy -hls_time 10 -hls_list_size 6 -hls_flags delete_segments \
media/streams/<stream-id>/index.m3u8

Frontend Setup (React)
Open the frontend folder:
cd ""Open the frontend folder:

bash
Copy
Edit
cd ../frontend
Install dependencies:

bash
Copy
Edit
npm install
Start the frontend:

bash
Copy
Edit
npm start
🖥 App runs at: http://localhost:3000



















