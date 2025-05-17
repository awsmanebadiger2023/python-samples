print('####################Learning how to USER context in Python')
# file_descriptors = []
# for x in range(100000):
#     file_descriptors.append(open('test.txt', 'w'))


# Python program creating a
# context manager

class ContextManager():

    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


with ContextManager() as manager:
    print('with statement block')