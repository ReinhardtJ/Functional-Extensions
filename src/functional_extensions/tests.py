import copy
import typing
from unittest import TestCase

import attr

from src.functional_extensions import fe
from src.functional_extensions.fe import _l, _o


class TestList(TestCase):
    def test_ctor(self) -> None:
        expected = [1, 2, 3, 4]
        actual = _l([1, 2, 3, 4])
        actual2 = _l(1, 2, 3, 4)
        self.assertTrue(expected == actual == actual2)

    def test_sort_inplace_with_ints(self) -> None:
        expected = [1, 2, 3, 4]
        actual = _l(3, 4, 1, 2)
        actual2 = actual._sort_inplace()
        self.assertEqual(expected, actual)
        self.assertIs(actual, actual2)

        expected = [4, 3, 2, 1]
        actual = _l(3, 4, 1, 2)
        actual2 = actual._sort_inplace(reverse=True)
        self.assertEqual(expected, actual)
        self.assertIs(actual, actual2)

    def test_sort_with_ints(self) -> None:
        expected = [1, 2, 3, 4]
        unsorted = _l(3, 4, 1, 2)
        sorted = unsorted._sort()
        self.assertEqual(expected, sorted)
        self.assertIsNot(unsorted, sorted)

        expected = [4, 3, 2, 1]
        unsorted = _l(3, 4, 1, 2)
        sorted = unsorted._sort(reverse=True)
        self.assertEqual(expected, sorted)
        self.assertIsNot(unsorted, sorted)

    def test_any_with_bools(self) -> None:
        self.assertTrue(_l(True, False, False)._any())
        self.assertFalse(_l(False, False, False)._any())

    def test_sort_with_predicate(self) -> None:
        @attr.s(auto_attribs=True)
        class Student:
            name: str
            grade: str
            age: int

        john = Student('john', 'A', 15)
        jane = Student('jane', 'B', 12)
        dave = Student('dave', 'B', 10)
        students = [john, jane, dave]

        expected = [dave, jane, john]
        actual = _l(students)._sort_inplace(key=lambda student: student.age)
        self.assertEqual(expected, actual)

    def test_filter(self) -> None:
        numbers = [1, 2, 3, 4]

        def is_even(number): return number % 2 == 0

        expected = [2, 4]
        actual = _l(numbers)._filter(is_even)
        self.assertEqual(expected, actual)

    def test_filterfalse(self) -> None:
        numbers = [1, 2, 3, 4]

        def is_even(number): return number % 2 == 0

        expected = [1, 3]
        actual = _l(numbers)._filterfalse(is_even)
        self.assertEqual(expected, actual)

    def test_map_with_int_list(self) -> None:
        def square(x): return x ** 2

        expected = [1, 0, 1, 4]
        actual = _l(-1, 0, 1, 2)._map(square)._to_list()
        self.assertEqual(expected, actual)

        expected = _l(-1, 0, 1, 2)
        actual = expected._map(square).to_list()
        self.assertNotEqual(expected, actual)

    def test_map_with_int_list(self) -> None:
        def multiply(x, y): return x * y

        expected = [2, 4, 6, 8]
        actual = _l(1, 2, 3, 4)._map(multiply, 2)
        self.assertEqual(expected, actual)

    def test_map_inplace_with_int_list(self) -> None:
        def square(x): return x ** 2

        expected = [1, 0, 1, 4]
        actual = _l(-1, 0, 1, 2)._map_inplace(square)
        self.assertEqual(expected, actual)

        expected = _l(-1, 0, 1, 2)
        actual = expected._map_inplace(square)
        self.assertEqual(expected, actual)

    def test_for_each_with_int_list(self) -> None:
        class ReduceBySum:
            def __init__(self):
                self.sum = 0

            def __call__(self, summand: int) -> None:
                self.sum += summand

        reduce_by_sum_regular = ReduceBySum()
        for element in [-1, 0, 1, 2]:
            reduce_by_sum_regular(element)

        reduce_by_sum_extended = ReduceBySum()
        _l(-1, 0, 1, 2)._for_each(reduce_by_sum_extended)

        self.assertTrue(reduce_by_sum_regular.sum ==
                        reduce_by_sum_extended.sum ==
                        2)

    def test_pipe_with_int_list(self) -> None:
        class CollectSum:
            def __init__(self):
                self.sum = 0

            def __call__(self, l: typing.List) -> None:
                self.sum = sum(l)

        collect_sum = CollectSum()
        _l(-1, 0, 1, 2)._pipe(collect_sum)
        expected = 2
        actual = collect_sum.sum
        self.assertEqual(expected, actual)

    def test_min_with_int_list(self) -> None:
        expected = -1
        actual = _l(4, 2, -1, 1)._min()
        self.assertEqual(expected, actual)

    def test_max_with_int_list(self) -> None:
        expected = 4
        actual = _l(4, 2, -1, 1)._max()
        self.assertEqual(expected, actual)

    def test_sum_with_int_list(self) -> None:
        expected = 6
        actual = _l(4, 2, -1, 1)._sum()
        self.assertEqual(expected, actual)

    def test_reverse_with_int_list(self) -> None:
        expected = [4, 3, 2, 1]
        actual = _l(1, 2, 3, 4)._reverse()
        self.assertEqual(expected, actual)

    def test_zip(self) -> None:
        expected = [(1, 'sugar'), (2, 'spice'), (3, 'everything nice')]

        actual = _l(1, 2, 3)._zip(['sugar', 'spice', 'everything nice']) \
                            ._to_list()

        self.assertEqual(expected, actual)


class TestObject(TestCase):
    def test_init_helper(self) -> None:
        @attr.s(auto_attribs=True)
        class Dog():
            name: str
            age: int

        def rename_dog(dog: Dog, new_name: str):
            dog.name = new_name
            return dog

        dog = Dog('Nick', 4)
        try:
            extended_dog = _o(dog)

            expected_renamed_dog = Dog('Jack', 4)
            actual_renamed_dog = extended_dog._pipe(rename_dog, 'Jack')
            self.assertEqual(expected_renamed_dog, actual_renamed_dog)

            copied_dog = extended_dog._copy()
            self.assertEqual(dog, copied_dog)
            self.assertIsNot(dog, copied_dog)

            deep_copied_dog = extended_dog._deepcopy()
            self.assertEqual(dog, deep_copied_dog)
            self.assertIsNot(dog, deep_copied_dog)

            dog_type = extended_dog._type()
            self.assertEqual(dog_type, Dog)
        except BaseException:
            self.fail(BaseException)

    def test_pipe_with_object(self) -> None:
        @attr.s(auto_attribs=True)
        class Dog(fe.Object):
            name: str
            age: int

        def rename_dog(dog: Dog, new_name: str):
            dog.name = new_name

        expected = Dog(name='Jack', age=4)
        actual = Dog(name='Nick', age=4)
        actual._pipe(rename_dog, 'Jack')

        self.assertEqual(expected, actual)
