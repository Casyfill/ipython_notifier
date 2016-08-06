from pync import Notifier
import time

def notifyMe(txt, act='com.google.Chrome', title='Jupyter Nb'):
    '''
    rises notification with text passed, opens safary on click
    '''
    Notifier.notify(txt, activate=act, title=title)


class notifyOnComplete(object):

    def __init__(self, timer=False):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.timer = timer

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def finish(*args, **kwargs):

            if self.timer:
                start = time.now()
            try:
                r = f(*args, **kwargs)
                if self.timer:
                    delta = (time.now() - start).total_seconds()
                    notifyMe('Job complete in {0} seconds'.format(delta))
                else:
                    notifyMe('Job complete!')
                return r
            except Exception, e:
                notifyMe('Exception raised:{}'.format(e))

        return finish
