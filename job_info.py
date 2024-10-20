from constant import JobStatus
from utils.time_util import get_now_time_str


class JobInfo:
    def __init__(self):
        self.name = ''
        self.data = ''
        self.queue = ''

        # 需要初始化
        self.submit_time = ''
        self.status = ''

        # 任务开始时间
        self.start_time = ''
        self.finish_time = ''

    def init(self, name, data, queue):
        self.name = name
        self.data = data
        self.queue = queue

        self.submit_time = get_now_time_str()
        self.status = JobStatus.Queued

    def to_dict(self) -> dict:
        return vars(self)

    def to_obj(self, result: dict):
        for k, v in result.items():
            self.__setattr__(k, v)
