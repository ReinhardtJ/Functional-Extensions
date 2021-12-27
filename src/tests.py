from unittest import TestCase

import attr

import src.functional_extensions as fe


class TestList(TestCase):
    def test_ctor(self) -> None:
        expected = [1, 2, 3, 4]
        actual = fe.List([1, 2, 3, 4])
        self.assertEquals(expected, actual)

    def test_init(self) -> None:
        expected = [1, 2, 3, 4]
        actual = fe.List.init([1, 2, 3, 4])
        self.assertEquals(expected, actual)

    def test_from_values(self) -> None:
        expected = [1, 2, 3, 4]
        actual = fe.List.from_values(1, 2, 3, 4)
        self.assertEquals(expected, actual)

    def test_fe_sort_with_ints(self) -> None:
        expected = [1, 2, 3, 4]
        actual = fe.List.from_values(3, 4, 1, 2).fe_sort()
        self.assertEquals(expected, actual)

        expected = [4, 3, 2, 1]
        actual = fe.List.from_values(3, 4, 1, 2).fe_sort(reverse=True)
        self.assertEquals(expected, actual)

    def test_fe_sort_with_predicate(self) -> None:
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
        actual = fe.List.init(students).fe_sort(key=lambda student: student.age)
        self.assertEquals(expected, actual)

    def test_filter(self) -> None:
        numbers = [1, 2, 3, 4]
        def is_even(number):
            return number % 2 == 0

        expected = [2, 4]
        actual = fe.List.init(numbers).filter(is_even)
        self.assertEquals(expected, actual)

    def test_map_with_int_list(self) -> None:
        l = fe.List.from_values(-1, 0, 1, 2)

        def square(x: int) -> int: return x ** 2

        expected = [1, 0, 1, 4]
        actual = l.map(square).to_list()
        self.assertEqual(expected, actual)

    def test_map_with_string_list(self) -> None:
        l = fe.List.from_values('hello', 'world')
        expected = ['HELLO', 'WORLD']
        actual = l.map(str.upper).to_list()
        self.assertEqual(expected, actual)


class TestForEach(TestCase):
    def test_for_each_with_ints(self) -> None:
        class ReduceBySum:
            def __init__(self):
                self.sum = 0

            def __call__(self, summand: int) -> None:
                self.sum += summand

        l = fe.List.from_values(-1, 0, 1, 2)

        reduce_by_sum_regular = ReduceBySum()
        for element in l:
            reduce_by_sum_regular(element)

        reduce_by_sum_extended = ReduceBySum()
        l.for_each(reduce_by_sum_extended)

        self.assertTrue(reduce_by_sum_regular.sum ==
                        reduce_by_sum_extended.sum ==
                        2)


class TestFromValues(TestCase):
    def test_from_values_with_ints(self) -> None:
        l = fe.List.from_values(-1, 0, 1, 2)
        self.assertEquals(l, [-1, 0, 1, 2])


class TestPipe(TestCase):
    def test_pipe_with_ints(self) -> None:
        l = fe.List.from_values(1, 2, 3, 4)
        expected = [2, 4, 6, 8]
        actual = l.pipe(l.map, lambda x: x * 2)
        self.assertEquals(expected, actual)

    def test_pipe_with_object(self) -> None:
        @attr.s(auto_attribs=True)
        class Dog(src.functional_extensions.Object):
            name: str
            age: int

        def rename_dog(dog: Dog, new_name: str):
            dog.name = new_name

        expected = Dog(name='Jack', age=4)
        actual = Dog(name='Nick', age=4)
        actual.pipe(rename_dog, 'Jack')

        self.assertEquals(expected, actual)


class TestInteropWithList(TestCase):
    def test_equals_with_ints(self) -> None:
        normal = [1, 2, 3, 4]
        extended = fe.List([1, 2, 3, 4])
        self.assertEqual(normal, extended)

    def test_extended_list_object_is_list_instance(self) -> None:
        self.assertTrue(isinstance(fe.List(), list))
