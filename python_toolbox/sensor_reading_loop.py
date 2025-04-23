
# Simulated Sensor Reading with Retry Logic
import time
import random

def read_sensor():
    if random.random() < 0.2:  # simulate 20% failure
        raise ValueError("Sensor read error")
    return random.uniform(20.0, 25.0)

def read_with_retry(max_retries=3, delay=1):
    for attempt in range(max_retries):
        try:
            reading = read_sensor()
            print(f"Sensor reading: {reading:.2f}°C")
            return reading
        except ValueError as e:
            print(f"Attempt {attempt + 1}: {e}")
            time.sleep(delay)
    print("All retries failed.")
    return None

read_with_retry()
