readings = [
    {'timestamp': '2024-04-01T12:00', 'temp': 22.5},
    {'timestamp': '2024-04-01T12:01', 'temp': 23.1},
    {'timestamp': '2024-04-01T12:02', 'temp': 30.5},  # breach
    {'timestamp': '2024-04-01T12:03', 'temp': 22.8}
]

def detect_breach_reading(readings, thresholdC):
    output = []
    for record in readings:
        if record['temp'] > thresholdC:
            print(f"Warning: Temperature Breach Detected: {record['temp'] - thresholdC}degC over limit of {thresholdC}")
            output.append(record)
        else: continue

    print(f"Breached Readings: {output}")

detect_breach_reading(readings, 30.0)