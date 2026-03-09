# Offline Real-Time Speech-to-Text (STT) System

This project provides an **offline real-time speech recognition system** for Urdu speech using the Whisper speech recognition model.

The system captures audio from a microphone, processes it locally, and converts spoken Urdu into text in real time.

---

# Features

* **Offline Speech Recognition** – Works without an internet connection.
* **Real-Time Transcription** – Converts speech to text while speaking.
* **Urdu Language Support** – Optimized for Urdu speech recognition.
* **Automatic Logging** – All recognized speech is saved with timestamps.
* **Modular Architecture** – Clean and maintainable project structure.

---

# Technologies Used

* Python
* Whisper Speech Recognition Model
* PyAudio (for microphone input)
* NumPy (for audio processing)

---

# Installation and Setup

## 1. Prerequisites

Make sure the following are installed:

* Python 3.8 or higher
* pip (Python package manager)

---

## 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Required libraries include:

* whisper
* torch
* pyaudio
* numpy

Note:
If PyAudio fails to install on Windows, install it using a precompiled wheel.

---

# Running the System

To start the speech recognition system run:

```bash
python -m src.main
```

After running the command:

1. The system initializes the microphone.
2. Start speaking in Urdu.
3. Recognized speech will appear in the terminal.

Example output:

```
🎤 Microphone stream started

✅ Final: اسلام علیکم
✅ Final: میرا نام زوہیب ہے
```

To stop the program press:

```
Ctrl + C
```

---

# Project Structure

```
offline-stt-system
│
├── src
│   ├── audio_capture.py
│   ├── recognizer.py
│   ├── session_manager.py
│   ├── logger.py
│   ├── config.py
│   └── main.py
│
├── logs
│   └── transcription_log.txt
│
├── requirements.txt
└── README.md
```

---

# How It Works

1. Audio is captured from the microphone using PyAudio.
2. Audio chunks are sent to the Whisper model.
3. The model processes the speech and generates text.
4. Recognized text is displayed in the terminal.
5. Final results are saved into the logs folder.

---

# Future Improvements

* Real-time subtitle window (GUI)
* Faster streaming recognition
* Multi-language speech support
* Speaker identification

---

# License

This project is intended for educational and research purposes.
