import logging
import os
from functools import partial
from multiprocessing.pool import Pool
from time import time

from download import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

def main():
    ts = time()
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("IMGUR_CLIENT_ID env variable does not exist")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    download = partial(download_link, download_dir)
    with Pool(4) as p:
        p.map(download, links)
    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()