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
