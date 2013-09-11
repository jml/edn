from collections import namedtuple

from parsley import makeGrammar

class Symbol(namedtuple("Symbol", "name prefix type")):
    _MARKER = object()

    def __new__(cls, name, prefix=None):
        return super(Symbol, cls).__new__(cls, name, prefix, Symbol._MARKER)


class Keyword(namedtuple("Keyword", "name prefix type")):
    _MARKER = object()

    def __new__(cls, name_or_symbol, prefix=None):
        name = name_or_symbol

        if isinstance(name_or_symbol, Symbol):
            name = name_or_symbol.name
            prefix = name_or_symbol.prefix

        return super(Keyword, cls).__new__(cls, name, prefix, Keyword._MARKER)


class Vector(tuple):
    pass


class Map(object):
    """
    TODO XXX FIXME: THIS IS TERRIBLE.
    """
    def __init__(self, pairs):
        self._pairs = pairs

    def __getitem__(self, key):
        for k, v in self._pairs:
            if key == k:
                return v

    def __eq__(self, other):
        if not isinstance(other, Map):
            return False

        return self._pairs == other._pairs

    def __repr__(self):
        return '<{self.__class__.__name__} pairs={self._pairs!r}>'.format(
            self=self
        )


TaggedValue = namedtuple("TaggedValue", "tag value")

edn = makeGrammar(open('edn.parsley').read(),
                  {
                    'Symbol': Symbol,
                    'Keyword': Keyword,
                    'Vector': Vector,
                    'TaggedValue': TaggedValue,
                    'Map': Map,
                  },
                  name='edn')
