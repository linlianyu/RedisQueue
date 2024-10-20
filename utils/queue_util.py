from constant import queue_key_prefix, job_key_prefix


def get_queue_redis_key(queue_name:  str) -> str:
    """
    获取存放队列任务列表的 redis key
    :param queue_name:
    :return:
    """
    return ':'.join([queue_key_prefix, queue_name])


def get_queue_job_redis_key(queue_name: str, job_name: str) -> str:
    return ':'.join([job_key_prefix, queue_name, job_name])