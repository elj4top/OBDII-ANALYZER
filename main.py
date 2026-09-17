#connecting the two
from obd_reader import OBDReader
from dtc_lookup import explain
from diagnose import diagnose
from logger import log_reading, LOG_FILE


reader = OBDReader(simulate=True)  # flip to False once got hardware

print("=== Live Data ===")
for key, value in reader.get_live_data().items():
    print(f"{key}: {value}")



print("\n=== Stored DTCs ===")
for code, official_name in reader.get_dtcs():
    print(f"{code}: {official_name}")
    print(f"  → {explain(code)}")

print("\n=== Diagnosis ===")
data = reader.get_live_data()
codes = reader.get_dtcs()
for finding in diagnose(data, codes):
    print(f"- {finding}")    


log_reading(data, codes)
print(f"\nReading logged to {LOG_FILE}")    