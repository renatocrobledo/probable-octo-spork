import logging
from datetime import datetime

logging.basicConfig(filename='test.log', level=logging.INFO)

def logger(fun):
    def log_func(*args):
        now = datetime.now().isoformat() 
        logging.info(f'{now} Running {fun.__name__} with params {args}') # create a file and push the logs there
        fun(*args)
    return log_func

@logger
def add(a,b):
    print(a + b)

@logger
def mul(a,b):
    print(a * b)


add(2,4)
mul(5,4)
