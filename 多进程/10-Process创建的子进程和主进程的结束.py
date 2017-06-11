from multiprocessing import Process
import time

"""
主进程不会等着所有的子进程结束才结束
"""

def test():
    for i in range(5):
        print("---test---")
        time.sleep(1)

p = Process(target=test)
p.start() # 让这个进程开始执行test函数里的代码

print("结束")
