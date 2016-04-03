from pync import Notifier


def notifyMe(txt, act='com.google.Chrome', title='Jupyter Nb'):
    '''
    rises notification with text passed, opens safary on click
    '''
    Notifier.notify(txt, activate=act, title=title)


def notifyOnComplete(func):
    '''
    function used to decorate another
    long function in python notebook:
    prints a notifier on complete
    '''
    def notifyOnFinish(*args, **kwargs):
        r = func(*args, **kwargs)
        notifyMe('Job complete!')
        return r

    return notifyOnFinish
