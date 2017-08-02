from scipy.misc import imresize

def imresizef(screen, size, preserve_range=True):
    screen = imresize(screen, size, interp='nearest', mode='F')
    return screen