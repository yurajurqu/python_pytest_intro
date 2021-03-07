def setup_function(function):
    if function == test_one:
        print('setting up test_one')
    if function == test_two:
        print('setting up test_two')

def teardown_function(function):
    if function == test_one:
        print('tearing down test_one')
    if function == test_two:
        print('tearing down test_two')

def setup_module(module):
    print('Setup module')
def teardown_module(module):
    print('Teardown module')

def test_one():
    print('Test one')
    assert 10>8
def test_two():
    print('Test two')
    assert 100>80