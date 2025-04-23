
# Multithreaded Sensor Read, wait, log, repeat to allow async operation w read and log
import threading
import queue
import time
import random

q = queue.Queue()

def producer():
    # Baseline temp = RT
    baseline = 22.5

    # For private in range 20:
    for _ in range(20):
        # 5% chance of a spike
        if random.random() < 0.05:
            temp = baseline + random.uniform(10.0, 15.0)
        # 10% chance of a failed reading (skip)
        elif random.random() < 0.10:
            print("Sensor error: failed to read temperature.")
            time.sleep(1)
            continue
        else:
            # Normal fluctuation around baseline
            temp = baseline + random.uniform(-0.3, 0.3)

        print(f"Producing temp: {temp:.2f}°C")
        q.put(temp)
        time.sleep(1)

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consuming {item}")
        q.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # signal to stop the consumer
consumer_thread.join()
