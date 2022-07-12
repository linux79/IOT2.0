from conf import barshrc
import multiprocessing
processes = ()
def boot1():
    boot1 = multiprocessing.Process(target=barshrc)
boot1.start()
boot1.join()