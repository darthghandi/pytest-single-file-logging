
def test_info_log(logger):
    logger.info('Hello!')
    assert True


def test_error_log(logger):
    logger.error('Goodbye!')
    assert True


def test_warning_log(logger):
    logger.warning('this is your last warning!')


def test_debug_log(logger):
    logger.debug('oh look! It\'s debug!')


def test_parameterized_log(times, logger):
    logger.info('Just informing you I have logged {} times'.format(times))


def test_results(logger):
    logger.info('Cheking to see if log messages made it to the log file')
    log_file = 't.log'
    with open(log_file) as f:
        contents = f.read()
    assert 'Hello!' in contents
    assert 'Goodbye!' in contents
    assert '999 times' in contents
