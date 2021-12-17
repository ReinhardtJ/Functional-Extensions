from unittest import TestCase

from src.list_extensions import List


class TestMap(TestCase):
    def test_map_with_ints(self) -> None:
        l = List.from_values(-1, 0, 1, 2)

        def square(x: int) -> int: return x ** 2

        expected = [1, 0, 1, 4]
        actual = l.map(square)
        self.assertEqual(expected, actual)

    def test_map_with_string(self) -> None:
        l = List.from_values('hello', 'world')
        expected = ['HELLO', 'WORLD']
        actual = l.map(str.upper)
        self.assertEqual(expected, actual)


class TestFromValues(TestCase):
    def test_from_values_with_ints(self) -> None:
        l = List.from_values(-1, 0, 1, 2)
        self.assertEquals(l, [-1, 0, 1, 2])


class TestCompatibilityWithList(TestCase):
    def test_equals_with_ints(self) -> None:
        normal = [1, 2, 3, 4]
        extended = List([1, 2, 3, 4])
        self.assertEqual(normal, extended)

    def test_extended_list_object_is_list_instance(self) -> None:
        self.assertTrue(isinstance(List(), list))
