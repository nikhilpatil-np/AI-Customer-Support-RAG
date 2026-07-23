import csv
import os
from datetime import datetime

# Create logs folder automatically if it doesn't exist
os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/chat_logs.csv"


def log_chat(question, answer):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Timestamp", "Question", "Answer"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            question,
            answer
        ])