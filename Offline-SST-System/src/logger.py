# src/logger.py

import os
import datetime
from . import config

class Logger:
    """Handles logging of final transcriptions to a file."""

    def __init__(self):
        """Initializes the logger and ensures the log directory exists."""
        if not os.path.exists(config.LOG_DIR):
            os.makedirs(config.LOG_DIR)

    def log_transcription(self, text: str, processing_time: float):
        """
        Appends a structured log entry to the log file.

        Args:
            text (str): The final recognized text.
            processing_time (float): The total time taken for the session.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = (
            f"Timestamp: {timestamp}\n"
            f"Recognized Text: {text}\n"
            f"Processing Time: {processing_time:.2f} seconds\n"
            f"--------------------------------------------------\n"
        )
        try:
            with open(config.LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except IOError as e:
            print(f"Error: Could not write to log file: {e}")
