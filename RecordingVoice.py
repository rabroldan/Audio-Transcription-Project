import subprocess
import whisper_timestamped as whisper
import numpy as np

# Config
MIC_NAME = "Analogue 1 + 2 (Focusrite USB Audio)"
SAMPLE_RATE = 16000
CHUNK_DURATION_SEC = 3
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION_SEC * 2)  # 2 bytes per sample

# Start ffmpeg
cmd = [
    "ffmpeg",
    "-f", "dshow",
    "-i", f"audio={MIC_NAME}",
    "-ac", "1",
    "-ar", str(SAMPLE_RATE),
    "-f", "s16le",
    "-loglevel", "error",
    "-"
]

model = whisper.load_model("base")

print("🎤 Listening and transcribing with timestamps...")

with subprocess.Popen(cmd, stdout=subprocess.PIPE) as proc:
    try:
        while True:
            raw_audio = proc.stdout.read(CHUNK_SIZE)
            if not raw_audio or len(raw_audio) < CHUNK_SIZE // 2:
                print("⚠️ Skipped empty or short chunk")
                continue

            # Convert raw bytes to NumPy array (int16 → float32 normalized to -1.0 to 1.0)
            audio = np.frombuffer(raw_audio, np.int16).astype(np.float32) / 32768.0

            try:
                result = whisper.transcribe(model, audio, language="en")

                for segment in result["segments"]:
                    print(f"[{segment['start']:>6.2f}s - {segment['end']:>6.2f}s] {segment['text']}")

            except Exception as e:
                print("❌ Transcription error:", str(e))

    except KeyboardInterrupt:
        print("🛑 Stopped.")
    finally:
        proc.kill()
