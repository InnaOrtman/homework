

def oops():
    raise IndexError


def oops_inside():
    try:
        oops()
    except IndexError:
        print('caught an index error!')
    else:
        print('no error caught...')


oops_inside()
