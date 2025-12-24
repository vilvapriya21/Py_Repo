from multiprocessing import Pool
import time

def square(x):
    time.sleep(1)
    return x*x

if __name__=="__main__":
    li=range(10)
    with Pool(2) as p:
        result = p.map(square, li)
    print(result)