pytest_plugins = ['pytester', 'xdist']


def pytest_generate_tests(metafunc):
    if 'times' in metafunc.fixturenames:
        times = [i for i in range(1, 1000)]
        metafunc.parametrize("times", times)
