from multiprocessing import Process
import time
import random

"""
等到所有子进程结束，主进程才会结束
"""

def test():
    for i in range(random.randint(1,5)):
        print("---%d---" % i)
        time.sleep(1)

p = Process(target = test)
p.start()
p.join() # 堵塞 主进程执行到join，会等子进程结束再往下执行
print("---main---")
