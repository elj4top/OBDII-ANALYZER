# logger.py
import csv
import os
from datetime import datetime

LOG_FILE = "data_log.csv"

def log_reading(live_data, dtcs):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)

        # write header only once, the first time the file is created
        if not file_exists:
            header = ["timestamp"] + list(live_data.keys()) + ["dtcs"]
            writer.writerow(header)

        row = [datetime.now().isoformat()] + list(live_data.values()) + [";".join(dtcs)]
        writer.writerow(row)