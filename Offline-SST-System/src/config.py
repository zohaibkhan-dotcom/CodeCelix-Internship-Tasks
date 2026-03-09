#src/config.py

## Vosk model

# import os

# # Project paths
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# MODEL_PATH = os.path.join(BASE_DIR, 'models', 'vosk-model-small-en-in-0.4')
# LOG_DIR = os.path.join(BASE_DIR, 'logs')
# LOG_FILE = os.path.join(LOG_DIR, 'transcription_log.txt')

# # Audio settings
# SAMPLE_RATE = 16000
# CHANNELS = 1
# FRAME_PER_BUFFER = 8192
# AUDIO_FORMAT = "int16"

# # System settings
# CPU_SLEEP_TIME = 0.05














# Wisper
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'transcription_log.txt')

# Whisper model
WHISPER_MODEL = "small"   # tiny, base, small, medium, large

# Audio settings
SAMPLE_RATE = 16000
CHANNELS = 1
FRAME_PER_BUFFER = 8192
AUDIO_FORMAT = "int16"

CPU_SLEEP_TIME = 0.05