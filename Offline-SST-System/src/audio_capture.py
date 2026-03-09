#src/audio_capture.py

import pyaudio
import queue
from . import config

class AudioCapture:
    def __init__(self, audio_queue: queue.Queue):
        self._audio = pyaudio.PyAudio()
        self._audio_queue = audio_queue
        self._stream = None
        self.is_running = False

    def _audio_callback(self, in_data, frame_count, time_info, status):
        if self.is_running:
            self._audio_queue.put(in_data)
        return (None, pyaudio.paContinue)

    def start(self):
        if self.is_running:
            return
        self.is_running = True
        self._stream = self._audio.open(
            format=pyaudio.paInt16,
            channels=config.CHANNELS,
            rate=config.SAMPLE_RATE,
            input=True,
            frames_per_buffer=config.FRAME_PER_BUFFER,
            stream_callback=self._audio_callback,
        )
        self._stream.start_stream()
        print("🎤 Microphone stream started.")

    def stop(self):
        if not self.is_running:
            return
        self.is_running = False
        if self._stream:
            self._stream.stop_stream()
            self._stream.close()
        self._stream = None
        print("🎤 Microphone stream stopped.")

    def __del__(self):
        self._audio.terminate()
