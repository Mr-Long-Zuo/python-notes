### fork方式创建进程

> 简单的fork

```
import os

ret = os.fork()
print("haha")
```

> 主进程fork时返回值大于0，子进程fork时返回值等于0

```
import os
import time

ret = os.fork()
if ret == 0:
    while True:
        print("----1----")
        time.sleep(1)
else:
    while True:
        print("----2----")
        time.sleep(1)
```

> os.getpid()获取本进程pid，os.getppid()获取本进程的父pid，os.fork()返回值是生成的子进程的pid

```
import os

ret = os.fork()
print("haha")
if ret > 0:
    print("---父进程---%d" % os.getpid())
else:
    print("---子进程---%d---%d" % (os.getpid(), os.getppid()))
print(ret)

```

> 主进程结束不会等子进程

```
import os
import time

"""
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
```

> 全局变量在多个进程中不共享

```
import os
import time

g_num = 100

ret = os.fork()

if ret == 0:
    print("---process-1---")
    g_num += 1 
    print("---process-1 g_num=%d---" % g_num)
else:
    time.sleep(3)
    print("---process-2---")
    print("---process-2 g_num=%d---" % g_num)
```
```
输出：
---process-1---
---process-1 g_num=101---
---process-2---
---process-2 g_num=100---
```

> 多次fork

```

"""
2*2*2 = 8 
8个进程
"""
import os

os.fork()
os.fork()
os.fork()

print("1111")
```

### Process方式创建进程

Process([target,[group[,name[,args[,kwargs]]]]])
- target：调用的对象
- args：调用对象的参数元组
- kwargs：调用对象的参数字典
- name：当前进程实例的别名
- group

类方法：
- is_alive() 判断进程实例是否还在执行
- join([timeout]) 是否等待子进程执行结束或等待多少秒
- start() 启动进程实例，即开始创建子进程
- run() 如果没有给定target参数，对这个对象调用start()方法时，就将执行对象中的run()方法
- terminate() 不管任务是否完成，立即终止

Process类常用属性：
- name：当前进程实例别名，默认为Process-N，N为从1开始递增的整数
- pid：当前进程实例的PID值

```
from multiprocessing import Process
import time

def test():
    while True:
        print("---test---")
        time.sleep(1)

p = Process(target=test)
# 让这个进程开始执行test函数里的代码
p.start() 

while True:
    print("---main---")
    time.sleep(1)
```

> 一般情况下主进程不会等子进程结束再结束，而是直结束

```
from multiprocessing import Process
import time

def test():
    for i in range(5):
        print("---test---")
        time.sleep(1)

p = Process(target=test)
p.start() # 让这个进程开始执行test函数里的代码

print("结束")
```
```
输出：
结束
---test---
---test---
---test---
---test---
---test---

```

> 使用join方法，可以让主进程堵塞，等待所有子进程结束后，主进程结束

```
from multiprocessing import Process
import time
import random

def test():
    for i in range(random.randint(1,5)):
        print("---%d---" % i)
        time.sleep(1)

p = Process(target = test)
p.start()
p.join()
print("---main---")
```
```
输出：
---0---
---1---
---2---
---3---
---4---
---main---
```

> 通过Process子类的方式创建进程

```
from multiprocessing import Process
import time

class MyNewProcess(Process):
    def run(self):
        while True:
            print("---1---")
            time.sleep(1)

p = MyNewProcess()
p.start()

while True:
    print("---main---")
    time.sleep(1)
```

### 进程池

当需要创建的进程数量不多时，可以直接使用multiprocessing中的Process创建多个进程，如果是成百上千的目标，可以利用multiprocessing中Pool进程池的方法提高效率

multiprocessing.Pool常用方法：
- apply_async(func[,args[,kwds]])：使用非阻塞方式调用func
- apply(func[,args[,kwds]])：使用阻塞方式调用func
- terminate()：不管任务是否完成，立即终止
- join()：主进程阻塞，等待子进程的退出，必须在close或terminate之后使用

> apply_async方式

```
from multiprocessing import Pool
import os
import time

def worker(n):
    for i in range(n):
        time.sleep(1)
        print("---pid = %d---n = %d" % (os.getpid(), i))

pool = Pool(5)

for i in range(10):
    print("---%d---" % i)
    pool.apply_async(worker,(5,))

print("---start---")
pool.close() # 关闭进程池，相当于不能够再添加新任务了
pool.join() 
print("---end---")

```

> apply方式

```
from multiprocessing import Pool
import os
import time

def worker(n):
    for i in range(n):
        time.sleep(1)
        print("---pid = %d---n = %d" % (os.getpid(), i))

pool = Pool(5)

for i in range(10):
    print("---%d---" % i)
    # 堵塞的方式
    pool.apply(worker,(5,))

print("---start---")
pool.close() # 关闭进程池，相当于 不能够再添加新任务了
pool.join()
print("---end---")
```

### 进程间通信-Queue

Queue本身是一个消息队列程序，可以利用它进行进程间通信

- Queue.size() 返回当前队列包含的消息数量（mac用不了）
- Queue.empty() 队列为空返回True，反之返回False
- Queue.full() 队列满了返回True，反之返回False
- Queue.get([block[,timeout]]) 获取队列中一条消息，然后将其从队列中移除，block默认为True
    - block默认为True，如果消息队列为空，且没有设置timeout，则程序被阻塞，直到消息队列读到消息为止
    - block为False时，如果消息队列为空，立即抛出Queue.Empty异常
    - timeout，超时时间，没有读到消息时会等待timeout秒，如果还没读到，就抛出Queue.Empty异常
- Queue.get_nowait() 相当于Queue.get(False)
- Queue.put(item[,block[,timeout]]) 将消息写入队列，block默认为True
    - block默认为True，如果消息队列没有写入空间，且没有设置timeout，则程序被阻塞，直到消息队列能写入为止
    - block为False时，如果消息队列没有写入空间，立即抛出Queue.Full异常
    - timeout，超时时间，没有写入空间时时会等待timeout秒，如果还没有写入空间，就抛出Queue.Full异常
- Queue.put_nowait() 相当于Queue.put(item, False)

> Process 下的Queue通信

```
from multiprocessing import Queue, Process
import os, time

# 写数据
def write(q):
    for value in ["A", "B", "C"]:
        q.put(value)
        print("put queue %s" % value)
        time.sleep(1)

# 读数据
def read(q):
    while True:
        if not q.empty():
            value = q.get()
            print("get queue %s " % value)
            time.sleep(1)
        else:
            break

if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pw.join()

    pr.start()
    pr.join()

    print("结束")
```

> Pool下的Queue通信

> 进程池中的Queue需要使用multiprocess.Manager()中的Queue，而不是multiprocess.Queue()

```
from multiprocessing import Manager, Pool
import os, time

def write(q):
    for value in ["A", "B", "C"]:
        q.put(value)
        time.sleep(1)
        print("queue put %s " % value)

def read(q):
    while True:
        if not q.empty():
            value = q.get()
            time.sleep(1)
            print("queue get %s " % value)
        else:
            break

if __name__ == "__main__":
    q = Manager().Queue()
    pool = Pool()

    pool.apply_async(write, (q,))
    pool.apply_async(read, (q,))

    pool.close()
    pool.join()

    print("结束")
```
