from pync import Notifier
from datetime import datetime


def _notifyMe(txt, act='com.google.Chrome', title='Jupyter Nb'):
    '''
    rises notification with text passed, opens safary on click
    '''
    Notifier.notify(txt, activate=act, title=title)


def notifyOnComplete(timer=None):
    def decorator(f):
        f.timer = timer

        def wrapper(*args, **kwargs):
            timer = f.timer
            if timer:
                start = datetime.now()
            try:
                r = f(*args, **kwargs)
                if timer:
                    delta = (datetime.now() - start).total_seconds()
                    _notifyMe('Job complete in {:.3f} seconds'.format(delta))
                else:
                    _notifyMe('Job complete!')
                return r
            except Exception, e:
                _notifyMe('Exception raised:{}'.format(e))
        return wrapper
    return decorator
