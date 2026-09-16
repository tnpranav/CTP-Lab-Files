import threading
import queue
import time

buffer = queue.Queue(maxsize=5)

def producer():
    for i in range(1, 11):
        buffer.put(i)
        print(f"Produced: {i}")
        time.sleep(0.5)

    buffer.put(None)  # Signal completion

def consumer():
    while True:
        item = buffer.get()

        if item is None:
            break

        print(f"Consumed: {item}")
        buffer.task_done()
        time.sleep(1)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Production and Consumption Completed")