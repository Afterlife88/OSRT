import sys
import traceback

def exceptions_handler(func):
    def wrapper(*args, **opts):
        try:
            func(*args, **opts)
        except:
            exc_info = sys.exc_info()
            e = exc_info[0]
            print('Error: %s\n%s' % (e, traceback.format_exc()))

    return wrapper
