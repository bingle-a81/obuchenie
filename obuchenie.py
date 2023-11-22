def foo():
    print('1')
    yield
    print('2')
    yield


for i in range(2):
    next(foo())

