
redis_key_prefix = 'RedisQueue'

queue_key_prefix = ':'.join([redis_key_prefix, 'queue'])
job_key_prefix = ':'.join([redis_key_prefix, 'job'])


class JobStatus:
    Queued = 'Queued'
    Started = 'Started'
    Finished = 'Finished'
    Failed = 'Failed'



