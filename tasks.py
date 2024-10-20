import pickle
import time


def sleep(seconds):
    print(seconds, 'start')
    time.sleep(seconds)
    print(seconds, 'end')


def main():
    data = pickle.dumps((sleep, (1, ), {}))
    func_data = pickle.loads(data)
    func, args, kwargs = func_data
    func(*args, **kwargs)


if __name__ == '__main__':
    main()


