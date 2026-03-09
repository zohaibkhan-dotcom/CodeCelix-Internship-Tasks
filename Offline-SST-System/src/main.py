# src/main.py

import queue
import threading
from .audio_capture import AudioCapture
from .recognizer import StreamingRecognizer
from .session_manager import SessionManager
from .logger import Logger
from . import config


class STTEngine:
    """
    The main Speech-to-Text engine that orchestrates all modules.
    """

    def __init__(self):
        """Initializes all system components."""
        print("--- Offline Real-Time STT System ---")
        self.audio_queue = queue.Queue()
        self.session_manager = SessionManager()
        self.logger = Logger()
        self.audio_capture = AudioCapture(self.audio_queue)
        self.recognizer = StreamingRecognizer(self.audio_queue, self.session_manager)
        print("✅ System initialized. Ready to start.")

    def run(self):
        """
        Starts the speech-to-text process and handles the main application loop.
        """
        try:
            # Start session and audio capture
            self.session_manager.start_session()
            self.audio_capture.start()

            # Run recognition processing in the main thread
            self.recognizer.process_stream()

        except KeyboardInterrupt:
            print("\nCaught KeyboardInterrupt, stopping gracefully...")
        finally:
            # Stop session and audio capture
            self.session_manager.stop_session()
            self.audio_capture.stop()

            # Display summary and log results
            final_text, processing_time = self.session_manager.display_summary()
            if final_text:
                self.logger.log_transcription(final_text, processing_time)

            print("System shut down.")

def main():
    """Main function to run the STT engine."""
    engine = STTEngine()
    engine.run()

if __name__ == "__main__":
    main()
