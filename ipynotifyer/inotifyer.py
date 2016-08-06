from pync import Notifier
import time


def notifyMe(txt, act='com.google.Chrome', title='Jupyter Nb'):
    '''
    rises notification with text passed, opens safary on click
    '''
    Notifier.notify(txt, activate=act, title=title)


def notifyOnComplete(timer=False):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if timer:
                start = time.now()
            try:
                r = f(*args, **kwargs)
                if timer:
                    delta = (time.now() - start).total_seconds()
                    notifyMe('Job complete in {0} seconds'.format(delta))
                else:
                    notifyMe('Job complete!')
                return r
            except Exception, e:
                notifyMe('Exception raised:{}'.format(e))
        return wrapper
    return decorator
