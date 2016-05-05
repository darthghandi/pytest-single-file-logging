# -*- coding: utf-8 -*-


# def test_bar_fixture(testdir):
#     """Make sure that pytest accepts our fixture."""
#
#     # create a temporary pytest test module
#     testdir.makepyfile("""
#         def test_sth(bar):
#             assert bar == "europython2015"
#     """)
#
#     # run pytest with the following cmd args
#     result = testdir.runpytest(
#         '--foo=europython2015',
#         '-v'
#     )
#
#     # fnmatch_lines does an assertion internally
#     result.stdout.fnmatch_lines([
#         '*::test_sth PASSED',
#     ])
#
#     # make sure that that we get a '0' exit code for the testsuite
#     assert result.ret == 0


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'pytest-single_file_logging:',
    ])


# def test_hello_ini_setting(testdir):
#     testdir.makeini("""
#         [pytest]
#         HELLO = world
#     """)
#
#     testdir.makepyfile("""
#         import pytest
#
#         @pytest.fixture
#         def hello(request):
#             return request.config.getini('HELLO')
#
#         def test_hello_world(hello):
#             assert hello == 'world'
#     """)
#
#     result = testdir.runpytest('-v')
#
#     # fnmatch_lines does an assertion internally
#     result.stdout.fnmatch_lines([
#         '*::test_hello_world PASSED',
#     ])
#
#     # make sure that that we get a '0' exit code for the testsuite
#     assert result.ret == 0

# TODO: need to figure out how to make this work
# def test_log_to_file(testdir):
#     testdir.makepyfile("""
#         def test_info_log(logger):
#             logger.info('Hello!')
#             assert True
#
#         def test_error_log(logger):
#             logger.info('Goodbye!')
#             assert True
#     """)
#     config = '''{
#     "version": 1,
#     "formatters": {
#         "default": {"format": "%(asctime)s %(name)s %(levelname)s: %(message)s", "datefmt": "%Y-%m-%d %H:%M:%S"}
#     },
#     "handlers": {
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.handlers.RotatingFileHandler",
#             "formatter": "default",
#             "filename": "t.log",
#             "maxBytes": 10485760,
#             "mode": "a",
#             "backupCount": 5
#         }
#     },
#     "loggers": {
#         "": {
#             "level": "DEBUG",
#             "handlers": ["file"]
#         }
#     },
#     "disable_existing_loggers": true
# }'''
#     testdir.makefile('.config', log=config)
#
#     result = testdir.runpytest(
#         '-n 2',
#         '--logconfig "log.config"'
#     )
#
#     print(result)
