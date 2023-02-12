def get_objects():
    import random

    def any_function():
        pass

    def gen(n):
        return (n ** 3 for n in range(5))

    types = (5.5, 'string', [-7, 0], None,
             complex(1, 1), True, iter({'key': 'value'}), {'key': 'value'}, b'string',
             (1,), range(1), frozenset({2}), gen(5), random,
             {'a'}, memoryview(b'abc'), len, any_function,
             object(), type(object()), Exception(), ValueError(),
             iter([1, 2, 3]), bytearray(b'string'), str.center)
    
    def key():
        return lambda x: type(x).__name__
    
    return sorted(types, key=key())
