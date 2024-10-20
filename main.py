import redis

from redis_queue import Queue
from tasks import sleep
from worker import Worker


def main():
    redis_conn = redis.Redis(host='localhost', port=6379, db=0)
    queue = Queue(redis_conn)
    queue.submit(sleep, 1)
    worker = Worker(queue)
    worker.run()


if __name__ == '__main__':
    main()
