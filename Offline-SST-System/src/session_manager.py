# src/session_manager.py

import time

class SessionManager:
    def __init__(self):
        self.is_listening = False 
        self.last_partial_text = ""
        self.start_time = None

    def start_session(self):
        """Session shuru karta hai."""
        self.is_listening = True
        self.start_time = time.time()
        print("\n🚀 Session started. Listening for Urdu speech...")

    def stop_session(self):
        """Session ko rokta hai."""
        self.is_listening = False
        print("\n🛑 Session stopped.")

    def handle_partial_result(self, partial_text: str):
        """Aadha sentence handle karta hai."""
        if partial_text and partial_text != self.last_partial_text:
            self.last_partial_text = partial_text
            print(f"   ... {partial_text}", end='\r', flush=True)

    def handle_final_result(self, final_text: str):
        if final_text:
            print(f"\n✅ Final: {final_text}")
            
            # File mein save karne ke liye ye lines add karein:
            with open("logs/Speech_Text.txt", "a", encoding="utf-8") as f:
                f.write(f"{time.ctime()}: {final_text}\n")
                
            self.last_partial_text = ""

    def display_summary(self):
        """Ye function missing tha jiski wajah se error aa raha tha."""
        duration = 0
        if self.start_time:
            duration = round(time.time() - self.start_time, 2)
        
        print("\n" + "="*30)
        print(f"📊 Session Summary")
        print(f"⏱️  Duration: {duration} seconds")
        print("="*30 + "\n")
        
        # main.py expects some return values
        return "Session Ended", duration

    def handle_error(self, error_message: str):
        print(f"\n❌ Error: {error_message}")
        self.stop_session()