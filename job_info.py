from constant import JobStatus
from utils.time_util import get_now_time_str


class JobInfo:
    def __init__(self):
        self.name = None
        self.data = None
        self.queue = None

        # 需要初始化
        self.submit_time = None
        self.status = None

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
