import csv
import os
from datetime import datetime

LOG_FILE = "data_log.csv"

def log_reading(live_data, dtcs):
    file_exists = os.path.isfile(LOG_FILE)

    # dtcs is a list of (code, description) tuples — join just the codes for the CSV
    dtc_codes = ";".join(code for code, desc in dtcs)

    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            header = ["timestamp"] + list(live_data.keys()) + ["dtcs"]
            writer.writerow(header)

        row = [datetime.now().isoformat()] + list(live_data.values()) + [dtc_codes]
        writer.writerow(row)
