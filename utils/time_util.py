from datetime import datetime


def get_now_time_str(t_format='%Y-%m-%d %H:%M:%S'):
    now = datetime.now()
    time_str = now.strftime(t_format)
    return time_str
