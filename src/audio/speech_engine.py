import pyttsx3
import threading
from datetime import datetime

class SpeechEngine:
    def __init__(self, rate=150, cooldown=3):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.last_speech_time = {}
        self.speech_cooldown = cooldown

    def speak(self, text, identifier=None):
        """Speak text if cooldown period has passed"""
        current_time = datetime.now()
        
        if identifier is None:
            self._speak_thread(text)
        elif identifier not in self.last_speech_time or \
             (current_time - self.last_speech_time[identifier]).total_seconds() > self.speech_cooldown:
            self._speak_thread(text)
            self.last_speech_time[identifier] = current_time

    def _speak_thread(self, text):
        """Speak text in a separate thread"""
        try:
            threading.Thread(target=self._speak, args=(text,), daemon=True).start()
        except Exception as e:
            print(f"Error in speech: {str(e)}")

    def _speak(self, text):
        """Actually perform the speech"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in speech thread: {str(e)}") 