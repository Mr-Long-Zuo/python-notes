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


    
