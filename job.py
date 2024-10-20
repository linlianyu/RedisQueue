from redis import Redis

from redis import Redis

from constant import JobStatus
from job_info import JobInfo
from utils.func_util import loads_func
from utils.queue_util import get_queue_job_redis_key


class Job:
    def __init__(self, job_info: JobInfo, conn: Redis):
        self.job_info = job_info
        self.conn = conn

    def run(self):
        is_finished = False
        try:
            self.update(status=JobStatus.Started)
            data = self.job_info.data
            func, args, kwargs = loads_func(data)
            print(func, args, kwargs)
            func(*args, **kwargs)
            is_finished = True
        except Exception as e:
            self.update(status=JobStatus.Failed)
        finally:
            if is_finished:
                self.update(status=JobStatus.Finished)

    def update(self, *args, **kwargs):
        job_redis_key = get_queue_job_redis_key(self.job_info.queue, self.job_info.name)
        job_info_dict = self.job_info.to_dict()
        for key, value in kwargs.items():
            if key in job_info_dict:
                self.conn.hset(job_redis_key, key, str(value))
