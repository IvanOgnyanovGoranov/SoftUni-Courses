from unittest import TestCase, main

#from testing_lab.list.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.list = IntegerList(1, 2, 3, False, 1.5, '30')

    def test_correct_initialization(self):
        self.assertEqual([1, 2, 3], self.list.get_data())

    def test_element_gets_added_to_the_list_when_integer(self):
        self.list.add(4)

        self.assertEqual([1, 2, 3, 4], self.list.get_data())

    def test_raises_value_error_if_added_element_is_not_an_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add('3')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_raises_index_error_when_removes_index_oor(self):
        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_successfully_when_in_range_returns_deleted_element(self):
        expected_result = 1
        result = self.list.remove_index(0)

        expected_list = [2, 3]
        actual_list = self.list.get_data()

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_list, actual_list)

    def test_get_returns_value_error_when_index_oor(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index_returns_the_index_and_check_the_list(self):
        expected_result = 1
        result = self.list.get(0)

        self.assertEqual(expected_result, result)

    def test_insert_raises_index_err_when_index_oor(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(5, 100)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_raises_value_err_when_type_is_not_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(1, '100')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_inserts_integer_at_given_index_when_correct(self):
        self.list.insert(1, 5)

        actual = self.list.get_data()
        expected = [1, 5, 2, 3]

        self.assertEqual(expected, actual)

    def test_gt_biggest_from_list(self):
        self.list.add(0)

        expected = 3
        actual = self.list.get_biggest()

        self.assertEqual(expected, actual)

    def test_get_index_returns_the_index_of_the_element(self):
        self.assertEqual(0, self.list.get_index(1))



if __name__ == '__main__':
    main()
