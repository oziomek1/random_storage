import inspect


def decorator(fun):
    def wrapper(*args):
        value = args[0].attributes[fun.__code__.co_varnames[1]]
        if value is None:
            print(fun.__code__.co_varnames[1], ': Not available')
        else:
            return fun(*args)
    return wrapper


class Clazz:
    def __init__(self, path):
        self.path = path
        self.attributes = {
            'angle': None,
            'x': None,
            'y': None,
        }

    @decorator
    def show_angle(self, angle=None):
        frame = inspect.currentframe()
        args, _, _, _ = inspect.getargvalues(frame)
        print(args[1], ':', self.attributes['angle'])

    @decorator
    def show_x(self, x=None):
        frame = inspect.currentframe()
        args, _, _, _ = inspect.getargvalues(frame)
        print(args[1], ':', self.attributes['x'])


clazz = Clazz('/home/')
clazz.show_angle()
clazz.attributes['angle'] = 1.5
clazz.show_angle()

clazz.show_x()
clazz.attributes['x'] = -0.3
clazz.show_x()

