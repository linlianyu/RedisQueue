import uuid
from typing import Optional

from job_info import JobInfo
from utils.func_util import dumps_func
from utils.queue_util import get_queue_redis_key, get_queue_job_redis_key


class Queue:
    def __init__(self, redis_conn, queue_name='default'):
        self.redis_conn = redis_conn
        self.queue_name = queue_name
        self.queue_redis_key = get_queue_redis_key(queue_name)

    def submit(self, f, *args, name: Optional[str] = None, **kwargs):
        with self.redis_conn as conn:
            # todo check 是否已经存在
            if not name:
                name = str(uuid.uuid4()).replace('-', '')
            job = JobInfo()
            data = dumps_func(f, *args, **kwargs)
            job.init(name, data, self.queue_name)
            conn.rpush(self.queue_redis_key, name)
            job_redis_key = get_queue_job_redis_key(self.queue_name, name)
            for key, value in job.to_dict().items():
                conn.hset(job_redis_key, key, str(value))
