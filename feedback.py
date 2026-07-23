import csv
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

FEEDBACK_FILE = "logs/feedback.csv"

def save_feedback(question, answer, feedback):
    file_exists = os.path.isfile(FEEDBACK_FILE)

    with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Timestamp", "Question", "Answer", "Feedback"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            question,
            answer,
            feedback
        ])