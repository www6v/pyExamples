from gevent import monkey; monkey.patch_all()
import gevent
from gevent.queue import Queue  # 队列 gevent中的队列
import random
 
task_queue = Queue(3)
 
 
def producer(index=1):
    while True:
        print(f'生产者 [{index}]', end='')
        item = random.randint(0, 99)
        task_queue.put(item)
        print(f"生产 ---> {item}")
 
 
def consumer(index=1):
    while True:
        print(f'消费者 [{index}]', end='')
        item = task_queue.get()
        print(f"消费 ---> {item}")
 
 
def main():
    job_1 = gevent.spawn(producer)
    job_2 = gevent.spawn(consumer)
    job_3 = gevent.spawn(consumer, 2)
    job_list = [job_1, job_2, job_3]
    gevent.joinall(job_list)
 
 
if __name__ == '__main__':
    main()
    pass