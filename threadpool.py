import logging
import os
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from time import time

from download import *

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(level=logging.DEBUG, format=FORMAT)
request_logger = logging.getLogger('requests').setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    ts = time()
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("IMGUR_CLIENT_ID env variable does not exist")
    download_dir = setup_download_dir()
    links = get_links(client_id)

    with ThreadPoolExecutor() as executor:
        fn = partial(download_link, download_dir)
        executor.map(fn, links, timeout=30)
    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()