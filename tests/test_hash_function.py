import unittest

from hash_function import hash


class TestHash(unittest.TestCase):
    def test_hash_mutable_objects_error_raised(self):
        with self.assertRaises(ValueError):
            hash(list())

    def test_hash_immutable_object_error_not_raised(self):
        hash(tuple())

    def test_pair_of_anagram_has_different_hash_value(self):
        self.assertNotEqual(
            hash('abc'),
            hash('cba'),
        )

    def test_quote_makes_distinguishable_hash_value(self):
        self.assertNotEqual(
            hash('123'),
            hash(123),
        )
