import unittest
from bublesort import bubble_sort  # Импортируем функцию bubble_sort из файла lib.py

class TestBubbleSort(unittest.TestCase):

    def test_ascending_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        bubble_sort(arr, ascending=True)
        self.assertEqual(arr, expected)

    def test_descending_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [90, 64, 34, 25, 22, 12, 11]
        bubble_sort(arr, ascending=False)
        self.assertEqual(arr, expected)

    def test_empty_list(self):
        arr = []
        expected = []
        bubble_sort(arr, ascending=True)
        self.assertEqual(arr, expected)

    def test_single_element(self):
        arr = [1]
        expected = [1]
        bubble_sort(arr, ascending=True)
        self.assertEqual(arr, expected)

    def test_all_equal_elements(self):
        arr = [7, 7, 7, 7]
        expected = [7, 7, 7, 7]
        bubble_sort(arr, ascending=True)
        self.assertEqual(arr, expected)

    def test_ascending_with_negative_numbers(self):
        arr = [3, -2, -1, 0, 2, 1]
        expected = [-2, -1, 0, 1, 2, 3]
        bubble_sort(arr, ascending=True)
        self.assertEqual(arr, expected)

    def test_descending_with_negative_numbers(self):
        arr = [3, -2, -1, 0, 2, 1]
        expected = [3, 2, 1, 0, -1, -2]
        bubble_sort(arr, ascending=False)
        self.assertEqual(arr, expected)

if __name__ == '__main__':
    unittest.main()
