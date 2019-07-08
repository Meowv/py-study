import threading

VALUE = 0

lock =  threading.Lock()

def add_value():
    global VALUE
    lock.acquire()
    for x in range(1000000):
        VALUE += 1
    lock.release()
    
    print(VALUE)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == "__main__":
    main()