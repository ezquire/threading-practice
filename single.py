import logging
import os
from time import time

from download import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    ts = time()
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("IMGUR_CLIENT_ID env variable does not exist")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    for link in links:
        download_link(download_dir, link)
    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()