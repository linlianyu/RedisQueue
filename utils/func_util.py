import base64
import pickle

from tasks import sleep


def dumps_func(func, *args, **kwargs):
    # 使用 pickle 序列化
    data = pickle.dumps((func, args, kwargs))

    # 将二进制数据转换为 base64 编码的字符串
    encoded_data = base64.b64encode(data).decode('utf-8')
    return encoded_data


def loads_func(data):
    # 反序列化的过程
    decoded_data = base64.b64decode(data)
    unserialized_task = pickle.loads(decoded_data)

    # 执行解包后的函数
    func, args, kwargs = unserialized_task
    return func, args, kwargs


def main():
    data = dumps_func(sleep, 1)
    func, args, kwargs = loads_func(data)
    func(*args, **kwargs)


if __name__ == '__main__':
    main()
