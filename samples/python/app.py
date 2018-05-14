import logging
from util import log

#logging.basicConfig(level=logging.DEBUG)

log.setup_logging()
logger = logging.getLogger(__name__)

def main():
    logger.debug('hello, world')
    logger.info('this is for informational purposes only')
    logger.warning('warning!')
    logger.error('problem')
    logger.debug('goodbye, blue sky')
    return 0

if __name__ == '__main__':
    main()
