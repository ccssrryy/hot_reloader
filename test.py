from hot_reloader import run_with_reloader
import threading, logging, os
logging.basicConfig(level=logging.DEBUG)
def m():
    while 1:
        print(threading.current_thread())
        print("main thread", threading.current_thread() == threading.main_thread())
        print('pid', os.getpid())
        import time
        time.sleep(1)
run_with_reloader(m, extra_files="./")
