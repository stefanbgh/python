### 64 ###
# multithreading

import threading
import time

def fn1():
    time.sleep(2)
    print("- Function 1")

def fn2():
    time.sleep(1)
    print("- Function 2")

def fn3():
    time.sleep(3)
    print("- Function 3")

print("# Executed: line by line ")
fn1()
fn2()
fn3()

print()

th1 = threading.Thread(target=fn1)
th2 = threading.Thread(target=fn2)
th3 = threading.Thread(target=fn3)

print("# Executed: at the same time")
th1.start()
th2.start()
th3.start()