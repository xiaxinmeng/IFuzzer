import sys


def func(a, b, c, d):

    frame = sys._getframe(1)

    print('call: %s' % (a))
    print('frame:                %s' % (frame))
    print('frame.f_code.co_name: %s' % (frame.f_code.co_name))
    print('frame.f_lineno:       %s' % (frame.f_lineno))


func('call 1, 1 line', 0, 1, 2)

func('call 2, 2 lines',
     0, 1, 2)

func('call 3, 4 lines',
     0,
     1,
     2)