from project.list import IntegerList
import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3, 4, "a", True)

    def test_list_get_data__expect_init_to_store_only_int_values(self):
        expected_result = [1, 2, 3, 4]
        actual_result = self.integer_list.get_data()
        self.assertEqual(expected_result, actual_result)

    def test_list_add__when_element_is_not_int_expect_value_error(self):
        with self.assertRaises(ValueError):
            self.integer_list.add(5.5)

    def test_list_add__when_element_is_int_expect_to_add_it_and_return_the_list(self):
        expected_result = [1, 2, 3, 4, 5]
        actual_result = self.integer_list.add(5)
        self.assertEqual(expected_result, actual_result)

    def test_list_remove_index__when_index_is_invalid_expect_index_error(self):
        with self.assertRaises(IndexError):
            self.integer_list.remove_index(5)

    def test_list_remove_index__when_index_is_valid_expect_to_remove_element_on_it_and_return_that_element(self):
        expected_element = 3
        actual_element = self.integer_list.remove_index(2)
        self.assertEqual(expected_element, actual_element)

    def test_list_get__when_index_is_invalid_expect_index_error(self):
        with self.assertRaises(IndexError):
            self.integer_list.get(5)

    def test_list_get__when_index_is_valid_expect_to_return_element_on_it(self):
        expected_element = 4
        actual_element = self.integer_list.get(3)
        self.assertEqual(expected_element, actual_element)

    def test_list_insert__when_index_is_invalid_expect_index_error(self):
        with self.assertRaises(IndexError):
            self.integer_list.insert(5, 1)

    def test_list_insert__when_element_is_not_int_expect_value_error(self):
        with self.assertRaises(ValueError):
            self.integer_list.insert(0, "a")

    def test_list_insert__when_index_is_valid_and_element_is_int_expect_to_add_element_on_index(self):
        self.integer_list.insert(0, 50)
        expected_result = [50, 1, 2, 3, 4]
        actual_result = self.integer_list.get_data()
        self.assertEqual(expected_result, actual_result)

    def test_list_get_bigger__expect_to_return_biggest_element(self):
        expected_element = 4
        actual_element = self.integer_list.get_biggest()
        self.assertEqual(expected_element, actual_element)

    def test_list_get_index__expect_to_return_index_of_a_given_element(self):
        expected_index = 1
        actual_index = self.integer_list.get_index(2)
        self.assertEqual(expected_index, actual_index)


if __name__ == "__main__":
    unittest.main()
