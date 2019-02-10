class Statics:
    """Derived from object class by default."""

    def __init__(self, name):
        """Mandatory constructor."""
        self._name = name

    def __repr__(self):
        """String representation of instance - java toString() equivalent."""
        return self._name

    @staticmethod
    def sum(a, b):
        """No self argument. Use regulare package method instead."""
        return a + b

    @classmethod
    def describeClass(cls):
        """cls instead of self"""
        print(cls.__name__)


if __name__ == '__main__':
    s = Statics('foo')

    print('Statics is derived from object: %s' % isinstance(s, object))
    print('Conversion to string by __repr__: %s' % s)
    print('Static method execution without instance: %s' % Statics.sum(1, 2))

    print('Class method execution without instance: ', end='')
    Statics.describeClass()
