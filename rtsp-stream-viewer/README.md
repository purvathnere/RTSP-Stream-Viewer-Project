# 📡 RTSP Live Stream Viewer using React and Django

A full-stack web application to **view RTSP streams live** in the browser using React (frontend), Django (backend), and FFmpeg (for RTSP to HLS conversion).

---

## ✅ Features

- Input field to add RTSP URLs  
- View multiple streams in a grid layout  
- Play/Pause controls  
- Real-time streaming using Django Channels (WebSocket)  
- Responsive UI built with React  
- Stream processing using FFmpeg  

---

## 🔧 Tech Stack

| Layer      | Technology              |
|------------|--------------------------|
| Frontend   | React.js, HLS.js         |
| Backend    | Django, Django Channels  |
| Media Proc | FFmpeg                   |
| Streaming  | HLS (.m3u8)              |
| Deployment | GitHub Pages (frontend), Heroku/Vercel (backend) |

---

## 🛠️ Backend Setup (Django + Channels)

1. **Clone the repo**
```bash
git clone https://github.com/purvathnere/RTSP-Stream-Viewer-Project
cd rtsp-stream-viewer/backend
1. **Clone the repo**
```bash
git clone https://github.com/purvathnere/RTSP-Stream-Viewer-Project
cd rtsp-stream-viewer/backend
Create virtual environment

bash
Copy
Edit
python -m venv env
env\Scripts\activate    # For Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Django server

bash
Copy
Edit
python manage.py runserver
✅ Server should start at: http://127.0.0.1:8000/

🧰 FFmpeg Setup
Check if FFmpeg is installed:

bash
Copy
Edit
ffmpeg -version
Create a stream folder and run FFmpeg:

bash
Copy
Edit
mkdir media/streams/<stream-id>

ffmpeg -rtsp_transport tcp -analyzeduration 10000000 -probesize 10000000 \
-i "<rtsp-url>" -c:v copy -hls_time 10 -hls_list_size 6 -hls_flags delete_segments \
media/streams/<stream-id>/index.m3u8
🟢 Make sure index.m3u8 and .ts files are being generated inside the folder.

⚛️ Frontend Setup (React)
Open the frontend folder:

bash
Copy
Edit
cd ../frontend
Install frontend packages:

bash
Copy
Edit
npm install
Start the frontend:

bash
Copy
Edit
npm start
✅ Frontend will run at: http://localhost:3000/

🌐 Deployment (Optional)
Frontend can be deployed using GitHub Pages

Backend can be deployed on Render, Heroku, or Vercel (must support ASGI)

🧪 Sample RTSP Stream for Testing
Use this public test stream:

bash
Copy
Edit
rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov
📬 Contact
Author: Purva Thnere
GitHub: @purvathnere

📝 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

Let me know if you'd like to include screenshots, or a Hindi version, or if you want me to add a


















