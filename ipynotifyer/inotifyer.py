from pync import Notifier
import time

def notifyMe(txt, act='com.google.Chrome', title='Jupyter Nb'):
    '''
    rises notification with text passed, opens safary on click
    '''
    Notifier.notify(txt, activate=act, title=title)


def notifyOnComplete(func, timer=False):
    '''function used to decorate another
    long function in python notebook:
    prints a notifier on complete

    Args:
        func(obj): function to run
        timer(bool): if true, will print time spent on function
    '''
    def notifyOnFinish(timer=timer, *args, **kwargs):
        if timer:
            start = time.now()
        try:
            r = func(*args, **kwargs)
            if timer:
                delta = time.now() - start
                notifyMe('Job complete in {0} seconds'.format(delta.total_seconds()))
            else:
                notifyMe('Job complete!')
            return r
        except Exception, e:
            notifyMe('Exception raised:{}'.format(e))

    return notifyOnFinish
