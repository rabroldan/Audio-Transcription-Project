# 🔊 Real-Time System Audio Transcription with Whisper

This project captures your system audio in real time (using loopback) and streams it to a Whisper transcription server for live transcription.

---

## 🧱 Components

1. **Client** (`client_loopback_streamer.py`)
   - Captures **system audio only** using loopback
   - Converts it to 16-bit PCM, mono, 16kHz
   - Streams it over TCP to a server

2. **Server** (`whisper_online_server.py`)
   - Listens on port `43007`
   - Receives raw audio stream
   - Transcribes it using Whisper

---

## 📦 Requirements

Install dependencies:

```bash
pip install soundcard numpy
pip install openai-whisper
pip install whisper_timestamped
▶️ Run the Client
Use the provided runner.py to start the audio capture and streaming client:

bash
Copy
Edit
python runner.py
Make sure the server (whisper_online_server.py) is running and listening on port 43007 before launching the client.

📚 Reference
If you use or extend this system, please consider citing:

bibtex
Copy
Edit
@inproceedings{machacek-etal-2023-turning,
    title = "Turning Whisper into Real-Time Transcription System",
    author = "Mach{\'a}{\v{c}}ek, Dominik  and
      Dabre, Raj  and
      Bojar, Ond{\v{r}}ej",
    editor = "Saha, Sriparna  and
      Sujaini, Herry",
    booktitle = "Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics: System Demonstrations",
    month = nov,
    year = "2023",
    address = "Bali, Indonesia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.ijcnlp-demo.3",
    pages = "17--24",
}