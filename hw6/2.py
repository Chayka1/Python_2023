from threading import Thread
from time import sleep, perf_counter

def main():
    def ku(name, n):
        for i in range(1, n+1):
            print(f'{name}: {i}')
            sleep(0.5)


    th1 = Thread(target=ku, args=('t1', 20))
    th2 = Thread(target=ku, args=('t2', 20))
    th1.start()
    th2.start()
    th1.join()
    th2.join()


if __name__ == "__main__":
    start = perf_counter()
    main()
    print(f"⛳Cooking time: {perf_counter() - start}")