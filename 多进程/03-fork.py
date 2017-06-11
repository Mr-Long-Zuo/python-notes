import os

"""
os.fork()的返回值是生成的子进程的pid
os.getpid()获取本进程的pid
os.getppid()获取本进程的父pid
"""

ret = os.fork()
print("haha")
if ret > 0:
    print("---父进程---%d" % os.getpid())
else:
    print("---子进程---%d---%d" % (os.getpid(), os.getppid()))
print(ret)
