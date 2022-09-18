IMMUTABLE_BUILT_IN_TYPES = (
    str,
    tuple,
    frozenset,
    int,
    float,
)


class Hash:
    def __call__(self, key):
        if self._is_unhashable(key):
            raise ValueError(str(key) + 'is not hashable')
        return self._hash(key)

    def _is_unhashable(self, key):
        return type(key) not in IMMUTABLE_BUILT_IN_TYPES and hasattr(key, '__hash__') is not None

    def _hash(self, key):
        """
        - _hash(abc) != _hash(cba) -> index별 가중치를 곱하여 구분
        - _hash('123') != _hash(123) -> repr로 구분
        """
        return sum(
            index * ord(character)
            for index, character
            in enumerate(repr(key), start=1)
        )


hash = Hash()
