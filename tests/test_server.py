import logging
import logging.handlers
import socket
from multiprocessing import Pool, current_process

default_port = logging.handlers.DEFAULT_TCP_LOGGING_PORT


def log(num):
    logger_name = current_process().name
    root_logger = logging.getLogger(logger_name)
    root_logger.setLevel(logging.DEBUG)
    socket_handler = logging.handlers.SocketHandler('localhost', default_port)
    root_logger.addHandler(socket_handler)
    root_logger.info('will this work? {}'.format(num))
    root_logger.warn('If this doesnt work, I will kick your nose')
    root_logger.debug('maybe I need to debug')
    root_logger.error('I have gas')


with Pool(processes=200) as pool:
    pool.map(log, range(1, 300))

# Now, define a couple of other loggers which might represent areas in your
# application:

# logger1 = logging.getLogger('area1')
# logger2 = logging.getLogger('area2')
# logger3 = logging.getLogger(__name__)
#
# logger1.debug('Quick zephyrs blow, vexing daft Jim.')
# logger1.info('How quickly daft jumping zebras vex.')
# logger2.warning('Jail zesty vixen who grabbed pay from quack.')
# logger2.error('The five boxing wizards jump quickly.')
# logger3.critical('I have bad gas')

# try closing socket with 4 bytes of 0's
end = bytes.fromhex('0000 0000')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', default_port))
s.send(end)
s.close()
