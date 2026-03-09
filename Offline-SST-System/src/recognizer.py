#src/recognizer.py
import whisper
import queue
import time
import numpy as np
from . import config

class StreamingRecognizer:
    def __init__(self, audio_queue: queue.Queue, session_manager):
        self._audio_queue = audio_queue
        self._session_manager = session_manager
        self.model = whisper.load_model("small")  # Urdu ke liye acha model

    def process_stream(self):

        audio_buffer = b""

        while self._session_manager.is_listening:
            try:
                chunk = self._audio_queue.get(timeout=0.1)
                audio_buffer += chunk

                # 5 seconds audio collect karo
                if len(audio_buffer) > config.SAMPLE_RATE * 2 * 5:

                    audio_np = np.frombuffer(audio_buffer, np.int16).astype(np.float32) / 32768.0

                    result = self.model.transcribe(
                        audio_np,
                        language="ur",
                        fp16=False
                    )

                    text = result["text"].strip()

                    if text:
                        self._session_manager.handle_final_result(text)

                    audio_buffer = b""

            except queue.Empty:
                time.sleep(config.CPU_SLEEP_TIME)