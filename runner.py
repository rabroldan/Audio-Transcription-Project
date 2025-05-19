import subprocess
import time

# Define the commands
commands = [
    ["python", "whisper_online_server.py", "--backend", "whisper_timestamped", "--model", "base", "--vac", "--port", "43007"],
    #["python", "RecordingVoice.py"], #enabled for using microphones
]

# Launch the first two processes immediately
processes = []
for cmd in commands:
    p = subprocess.Popen(cmd)
    processes.append(p)

# Add delay before launching WASAPI transcriber
print("⏳ Waiting 3 seconds before starting wasapi_transcriber.py...")
time.sleep(3)

# Start the delayed process
wasapi_cmd = ["python", "wasapi_transcriber.py"]
p = subprocess.Popen(wasapi_cmd)
processes.append(p)

print("✅ All processes launched. Press Ctrl+C to stop.")

# Wait for all to finish
try:
    for p in processes:
        p.wait()
except KeyboardInterrupt:
    print("\n🛑 Shutting down...")
    for p in processes:
        p.terminate()
