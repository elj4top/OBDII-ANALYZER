# diagnose.py
"""this is where the tool stops just reporting numbers
 and starts reasoning like a technician,
 connecting the fuel trim value to the DTC"""
def diagnose(live_data, dtcs):
    findings = []

    ltft = live_data.get("LONG_FUEL_TRIM_1")
    stft = live_data.get("SHORT_FUEL_TRIM_1")

    if ltft is not None:
        if ltft > 10:
            findings.append(
                f"LTFT is significantly positive ({ltft}%) — engine is running lean. "
                f"Likely causes: vacuum leak, weak fuel pump/pressure, dirty MAF sensor, "
                f"or clogged injector(s)."
            )
        elif ltft < -10:
            findings.append(
                f"LTFT is significantly negative ({ltft}%) — engine is running rich. "
                f"Likely causes: leaking injector, faulty MAF/MAP sensor reading high, "
                f"or a stuck-open EVAP purge valve."
            )

    if "P0171" in dtcs and ltft is not None and ltft > 5:
        findings.append(
            "P0171 confirmed by fuel trim data — this isn't just a stored code, "
            "the live data actively supports a lean condition right now. "
            "Check intake boots, vacuum lines, and manifold gasket first."
        )

    if not findings:
        findings.append("No significant fuel trim anomalies detected in current data.")

    return findings