import queue
import threading
import time

def process_task(task_queue):
    # while True:
        task = task_queue.get()
        print(f"Processing task: {task}")

        time.sleep(1)
        task_queue.task_done()



if __name__ == "__main__":

    task_queue = queue.Queue()

    for _ in range(3):
        worker = threading.Thread(target=process_task, args=(task_queue,))
        worker.daemon = True
        worker.start()


    for task_id in range(5):
        task_queue.put(task_id)


    task_queue.join()