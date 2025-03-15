"""
A decorator is a function that takes another function as input and extends or modifies its behavior without explicitly
changing its code.

It is a way to add functionality to existing functions or methods.

Decorators are commonly used for:

        Logging

        Timing function execution

        Access control (e.g., authentication)

        Caching

"""
import logging
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# without parameters
def test_decorator():
    def my_decorator(func):
        def wrapper():
            print('\nbefore the operation')
            result = func()
            print(result)
            print('after the operation')
        return wrapper

    @my_decorator
    def add():
        return 2+3

    add()


# with parameters
def test_decorator_with_parameters():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('starting the decorator')
    time.sleep(20)
    def my_decorator(func):
        logging.info('executing inner function')
        time.sleep(20)
        def wrapper(*args,**kwargs):
            logging.info('printing the logs before execution')
            time.sleep(20)
            print('\nbefore the operation')
            logging.info('executing the actual function')
            result = func(*args,**kwargs)
            print(result)
            print('after the operation')
            logging.info('printing the logs after execution')
        return wrapper

    @my_decorator
    def add(a,b):
        return a+b

    add(2,3)