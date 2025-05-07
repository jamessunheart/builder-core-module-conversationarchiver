import json
import time

class ConversationArchiver:
    def __init__(self, threshold=10):
        self.history = []
        self.threshold = threshold
        self.archive_file = "conversation_archive.json"

    def log(self, role: str, message: str):
        self.history.append({"time": time.time(), "role": role, "message": message})
        if len(self.history) >= self.threshold:
            self.save()

    def save(self):
        try:
            with open(self.archive_file, "a") as f:
                json.dump(self.history, f, indent=2)
                f.write(",\n")
            self.history = []
            print("[ARCHIVER] Conversation saved.")
        except Exception as e:
            print(f"[ARCHIVER ERROR] {str(e)}")