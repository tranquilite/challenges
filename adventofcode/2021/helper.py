def fprint(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        if isinstance(ret, list):
            print(f'>{func.__name__}:')
            for _ in ret:
                print(_, end='')
        else:
            print(f'>{func.__name__} {ret}')
        return ret
    return wrapper


def lp(lst):
    if isinstance(lst, list):
        for e in lst:
            print(e)