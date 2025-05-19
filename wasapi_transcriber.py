import soundcard as sc
import numpy as np
import socket
import time
import warnings
warnings.simplefilter("ignore")

# Whisper expects: 16kHz, mono, 16-bit PCM
SAMPLERATE = 16000
CHUNK_DURATION = 0.5  # seconds per chunk
CHUNK_SIZE = SAMPLERATE * CHUNK_DURATION

# Connect to Whisper server (running on localhost:43007)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 43007))
print("🔗 Connected to Whisper server on port 43007")

# Get loopback mic from default speaker
loopback = sc.get_microphone(sc.default_speaker().name, include_loopback=True)

# Start streaming audio
with loopback.recorder(samplerate=SAMPLERATE, channels=1) as recorder:
    print("🎧 Capturing from system audio...")
    while True:
        audio_chunk = recorder.record(numframes=CHUNK_SIZE)
        # Convert float32 [-1,1] → int16 PCM
        pcm_chunk = (audio_chunk * 32767).astype(np.int16).tobytes()
        # Send to Whisper
        sock.sendall(pcm_chunk)
