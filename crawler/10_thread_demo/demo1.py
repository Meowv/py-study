import threading
import time

# def coding():
#     for x in range(3):
#         print("coding %s" % x)
#         time.sleep(1)

# def drawing():
#     for x in range(3):
#         print("drawing %s" % x)
#         time.sleep(1)

# def main():
#     coding()
#     drawing()

# if __name__ == "__main__":
#     main()

# 多线程
def coding():
    for x in range(3):
        print("coding %s" % x)
        time.sleep(1)

def drawing():
    for x in range(3):
        print("drawing %s" % x)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()