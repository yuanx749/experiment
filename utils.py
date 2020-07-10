import logging
import inspect
import json
import os
import time
from functools import wraps

def get_logger(name=None):
    file_name = inspect.stack()[1].filename
    if name is None:
        name = os.path.basename(file_name)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(name)
    logger.info(file_name)
    return logger

def get_params(json_path=None):
    if json_path is None:
        file_name = inspect.stack()[1].filename
        json_path = os.path.splitext(file_name)[0]+ '.json'
    with open(os.path.abspath(json_path)) as file_:
        params = json.load(file_)
    print(params)
    return params

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        print('{} {} {} {:f} seconds'.format(func.__name__, args, kwargs, time.time() - start))
        return value
    return wrapper