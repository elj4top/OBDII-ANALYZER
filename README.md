# OBD-II Diagnostic Analyzer

A Python tool for reading live vehicle data and diagnostic trouble codes (DTCs) via the OBD-II protocol, built as part of a 5-project automotive diagnostics portfolio.

## Features
- Reads live sensor data (RPM, coolant temp, fuel trims, throttle position) via ELM327
- Decodes stored DTCs into human-readable explanations
- Includes a simulation mode for development without hardware

## Usage
```bash
pip install -r requirements.txt
python main.py
```

## Status
In development — currently supports simulated data; real ELM327 hardware testing in progress.

## Part of
Automotive Technology & Diagnostics Portfolio — built toward automotive ECU/diagnostics specialization.
