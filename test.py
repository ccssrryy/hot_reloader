from hot_reloader import run_with_reloader
import threading, logging
logging.basicConfig(level=logging.DEBUG)
def m():
    while 1:
        print(threading.current_thread())
        import time
        time.sleep(1)
run_with_reloader(m)
