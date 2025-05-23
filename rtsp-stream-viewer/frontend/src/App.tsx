// import React from 'react';
// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.tsx</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
import React, { useState } from 'react';
import axios from 'axios';
import VideoPlayer from './videoplayer'; 
import './App.css';

function App() {
  const [rtspUrl, setRtspUrl] = useState('');
  const [streamId, setStreamId] = useState<string | null>(null);

  const handleStartStream = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/streams/', {
        rtsp_url: rtspUrl
      });
      setStreamId(response.data.id);
      alert('Stream started with ID: ' + response.data.id);
    } catch (error) {
      console.error(error);
      alert('Failed to start stream');
    }
  };

  const handleStopStream = async () => {
    if (!streamId) return;
    try {
      await axios.post(`http://127.0.0.1:8000/api/streams/${streamId}/stop/`);
      alert('Stream stopped');
      setStreamId(null);
    } catch (error) {
      console.error(error);
      alert('Failed to stop stream');
    }
  };

  return (
    <div className="App">
      <h2>RTSP Streamer</h2>

      <input
        type="text"
        value={rtspUrl}
        onChange={(e) => setRtspUrl(e.target.value)}
        placeholder="Enter RTSP URL"
        style={{ padding: '8px', width: '300px', marginBottom: '10px' }}
      />
      <br />

      <button onClick={handleStartStream} style={{ marginRight: '10px' }}>
        Start Stream
      </button>

      <button onClick={handleStopStream} disabled={!streamId}>
        Stop Stream
      </button>
      

    {/*}  {streamId && (
        <div style={{ marginTop: '20px' }}>
          <h3>Live Stream</h3>
          <video
  src={`http://127.0.0.1:8000/media/streams/916b3877-ab85-455c-84b0-7c88ae9ed50c/index.m3u8`}
  

  controls
  autoPlay
  style={{ width: '600px', border: '1px solid black' }}
/>
*/}

{streamId && (
  <div style={{ marginTop: '20px' }}>
    <h3>Live Stream</h3>
    <VideoPlayer streamId={streamId} />
  </div>
)}
        </div>
    
  );
}

export default App;
