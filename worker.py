from typing import Optional

from constant import JobStatus
from job import Job
from job_info import JobInfo
from redis_queue import Queue
from utils.queue_util import get_queue_job_redis_key


class Worker:
    def __init__(self, queue: Queue):
        self.queue = queue
        self.conn = self.queue.redis_conn

    def run(self):
        while True:
            job = self.get_queue_first_queued_job()
            if job:
                job.run()
                self.conn.lrem(self.queue.queue_redis_key, 1, job.job_info.name)

    def get_queue_first_queued_job(self) -> Optional[Job]:
        all_job = self.conn.lrange(self.queue.queue_redis_key, 0, -1)
        for job_name in all_job:
            job_name = job_name.decode('utf-8')
            job_redis_key = get_queue_job_redis_key(self.queue.queue_name, job_name)
            job_redis_info = self.conn.hgetall(job_redis_key)
            new_job_redis_info = {}
            for key, value in job_redis_info.items():
                key = key.decode('utf-8')
                value = value.decode('utf-8')
                new_job_redis_info[key] = value
            job_info = JobInfo()
            job_info.to_obj(new_job_redis_info)
            if job_info.status == JobStatus.Queued:
                job = Job(job_info, self.conn)
                return job

        return None
