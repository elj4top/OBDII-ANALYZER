#connecting the two
from obd_reader import OBDReader
from dtc_lookup import explain

reader = OBDReader(simulate=True)  # flip to False once you have hardware

print("=== Live Data ===")
for key, value in reader.get_live_data().items():
    print(f"{key}: {value}")

print("\n=== Stored DTCs ===")
for code in reader.get_dtcs():
    print(f"{code}: {explain(code)}")