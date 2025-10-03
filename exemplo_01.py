# USANDO O DECORATOR DO <utils_log.py>

#from utils_log import log_decorator
import time
from decorator_inutil import hello
from timer_decorator import time_measure_decorator

#@log_decorator
@hello
@time_measure_decorator
def soma(x, y):
    time.sleep(2)
    return x + y

soma(2,3)
soma(2,8)
#soma(2,"3")