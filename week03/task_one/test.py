import os
import time
from multiprocessing import Process
import multiprocessing

# test1

"""
res = os.fork()
print(f'res = {res}')

if res == 0:
    print(f"i'm zi process, my pid is {os.getpid()}, my father process pid is {os.getppid()}")
else:
    print(f"i'm father process,my pid is {os.getpid()}")
"""

# test2

"""
def t(name):

    print(name)


if __name__ == '__main__':

    p = Process(target=t, args=('curry',))
    p.start()
    p.join()
"""

# test3

"""
def run():
    print('紫禁城启动')
    time.sleep(2)
    print('紫禁城结束')


if __name__ == '__main__':
    print('父进程启动')
    p = Process(target=run)
    p.start()
    # p.join()
    print('附近成结束')
"""

# test4

'''
def setting(name):
    print('__'*10)
    print(name)
    print('模块名称', __name__)
    print('附近成：', os.getppid())
    print('当前进程：', os.getpid())
    print('__'*10)


def run(name):
    setting(name)
    print(f'hello {name}')


if __name__ == '__main__':
    setting('main')
    p = Process(target=run, args=('john',))
    p.start()

    for p in multiprocessing.active_children():
        print(f'有紫禁城：{p.name} id: {str(p.pid)}')
    print('进程结束')
    print(f'CPU核心数量: {str(multiprocessing.cpu_count())}')

    p.join()
'''

# test5


class NewProcess(Process):
    def __init__(self, num):
        self.num = num
        super().__init__()

    def run(self):
        while True:
            print(f'我是进城 {self.num}, 我的pid是: {os.getpid()}')
            time.sleep(2)


for i in range(2):
    p = NewProcess(i)

    p.start()
