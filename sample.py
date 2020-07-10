from utils import get_logger, get_params, timer
logger = get_logger(__name__)

globals().update(get_params())

import urllib.request
from concurrent.futures import ThreadPoolExecutor

@timer
def download(url):
    response = urllib.request.urlopen(url)
    return response

@timer
def multithreading(func, args, n_workers=8):
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        results = executor.map(func, args)
    return list(results)

multithreading(download, urls * n_workers, n_workers=n_workers)

logger.info('Done')
