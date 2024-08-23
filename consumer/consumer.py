import threading
from multiprocessing import Process, Lock, Pipe
from threading import Lock, Thread


def process_connect_with_admin(connect_with_admin_recv: Pipe, lock: Lock):

    while True:
        try:
            with lock:
                object = connect_with_admin_recv.recv()
                print(object + 10)
        except:
            print("False")
            break


def main(mutex: Lock, connect_with_admin_recv: Pipe):

    lock = threading.Lock()

    # создаем поток для чтения сообщений от admin
    #connect_with_admin = Thread(target=process_connect_with_admin, args=(connect_with_admin_recv, lock, ))
    #connect_with_admin.start()
