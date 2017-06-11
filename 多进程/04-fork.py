import os
import time

"""
主进程结束不会等子进程
begin会执行一次
over会执行两次
"""
print("---begin---")

ret = os.fork()

if ret == 0:
    print("---子进程---")
    time.sleep(1)
    print("---子进程over---")
else:
    print("---父进程---")
    time.sleep(3)
    print("---主进程over---")

print("---over----")
