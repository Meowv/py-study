import threading
import time

class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("coding %s" % threading.current_thread())
            time.sleep(1)

class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("drawing %s" % threading.current_thread())
            time.sleep(1)

def main():
    t1 = CodingThread()
    t2 = DrawingThread()

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()