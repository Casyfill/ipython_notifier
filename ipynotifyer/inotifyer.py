from pync import Notifier
from datetime import datetime
from functools import wraps


def _notifyMe(txt, act='com.google.Chrome', title='Jupyter Nb'):
    '''
    rises notification with text passed, opens chrome on click
    '''
    Notifier.notify(txt, activate=act, title=title)


def notifyOnComplete(timer=None):
    def decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            if timer:
                start = datetime.now()

            try:
                r = func(*args, **kwargs)
                if timer:
                    delta = (datetime.now() - start).total_seconds()
                    _notifyMe('Job complete in {:.3f} seconds'.format(delta))
                else:
                    _notifyMe('Job complete!')
                return r
            except Exception, e:
                _notifyMe('Exception raised:{}'.format(e))
                raise Exception(e)
        return func_wrapper
    return decorator


if __name__ == '__main__':
    @notifyOnComplete(timer=True)
    def get_text(a, b):
        """returns some text"""
        return a/b

    print get_text(1, 0)
