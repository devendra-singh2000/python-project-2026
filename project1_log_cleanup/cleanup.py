import os
import time

LOG_DIR = "/var/log"   # change for local testing
DAYS = 7

now = time.time()

for filename in os.listdir(LOG_DIR):
    file_path = os.path.join(LOG_DIR, filename)

    if os.path.isfile(file_path):
        file_age = now - os.path.getmtime(file_path)

        if file_age > DAYS * 86400:
            print(f"Deleting: {file_path}")
            os.remove(file_path)