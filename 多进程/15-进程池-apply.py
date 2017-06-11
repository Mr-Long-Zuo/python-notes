from multiprocessing import Pool
import os
import time

def worker(n):
    for i in range(n):
        time.sleep(1)
        print("---pid = %d---n = %d" % (os.getpid(), i))

# 5表示进程池中最多有5个进程一起执行
pool = Pool(5)

for i in range(10):
    print("---%d---" % i)
    # 堵塞的方式
    pool.apply(worker,(5,))

print("---start---")
pool.close() # 关闭进程池，相当于 不能够再添加新任务了
pool.join() # 主进程 创建/添加 任务后，主进程默认不会等待进程池中的任务执行完成后才结束，而是当主进程的任务做完之后，立马结束，如果这个地方没join，会导致进程池中的任务不会执行
print("---end---")
