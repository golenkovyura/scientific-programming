def cmp_to_key(comparator):
    class Key:
        def __init__(self, obj):
            self.obj = obj

        def __eq__(self, second):
            return comparator(self.obj, second.obj) == 0

        def __gt__(self, second):
            return comparator(self.obj, second.obj) > 0

        def __lt__(self, second):
            return comparator(self.obj, second.obj) < 0

        def __ne__(self, other):
            return comparator(self.obj, other.arg) != 0

    return Key
