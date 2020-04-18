# This Python file uses the following encoding: utf-8
#
import psutil
import time
import os

def show_memory(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        before = proc.memory_info().rss / 1000000
        f(*args, **kwargs)
        after = proc.memory_info().rss / 1000000
        print('Использовано {} памяти'.format(after - before))
    return wrapper

# декоратор, замеряющий время выполнение функции.
def showTime(f):
    def wrapper(*args, **kwargs):
        start=time.process_time()
        f(*args, **kwargs)
        stop=time.process_time()
        print("Заняло {} секунд".format(stop-start))
    return wrapper


@showTime
@show_memory
def numbers(num):
    print('Series:')
    naturalNumb = [n+1 for n in range(num)]
    return naturalNumb

print('Generator:')
@showTime
@show_memory
def generator(num):
    for i in range(num):
        yield i


generator(1000000)
numbers(1000000)
