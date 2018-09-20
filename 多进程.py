# import json,pickle
# a={"q":1,"w":2,"e":3}
# b=pickle.dumps(a)
# print(b)
# print(pickle.loads(b))
#import threading,time
# def task():
#     time.sleep(1)
#     print("开始运行第一行")
# def task2():
#     time.sleep(13)
#     print("开始运行第二行")
# t1=threading.Thread(target=task)
# t2=threading.Thread(target=task2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
from multiprocessing import pool
import threading,time
def loop():
    print("开始执行%s线程------"%(threading.current_thread().name))
    n=0
    while n<6:
        n+=1
        print("正在执行%s线程------》%s"%(threading.current_thread().name,n))
        time.sleep(2)
    print("线程%s结束"%threading.current_thread().name)
m=threading.Thread(target=loop,name="lLoop")
m.start()
m.join()
