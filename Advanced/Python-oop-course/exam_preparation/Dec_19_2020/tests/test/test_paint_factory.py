from project.factory.paint_factory import PaintFactory
import unittest


class PaintFactoryTests(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("Factory", 100)

    def test_init__expect_attributes_to_be_set(self):
        self.assertEqual("Factory", self.paint_factory.name)
        self.assertEqual(100, self.paint_factory.capacity)
        # self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual({}, self.paint_factory.products)

    def test_add_ingredient__when_ingredient_is_not_valid_expect_type_error(self):
        with self.assertRaises(TypeError) as err:
            self.paint_factory.add_ingredient("purple", 10)
        expected_msg = "Ingredient of type purple not allowed in PaintFactory"
        self.assertEqual(expected_msg, str(err.exception))

    def test_add_ingredient__when_capacity_is_not_enough_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.paint_factory.add_ingredient("white", 105)
        expected_msg = "Not enough space in factory"
        self.assertEqual(expected_msg, str(err.exception))

    def test_add_ingredient__when_ingredient_is_not_in_ingredients_expect_to_add_it(self):
        self.paint_factory.add_ingredient("white", 10)
        expected = {"white": 10}
        self.assertEqual(expected, self.paint_factory.products)

    def test_add_ingredient__when_ingredient_is_in_ingredients_expect_to_raise_it_s_value(self):
        self.paint_factory.add_ingredient("white", 10)
        self.paint_factory.add_ingredient("white", 10)
        expected = {"white": 20}
        self.assertEqual(expected, self.paint_factory.products)

    def test_remove_ingredient__when_ingredient_type_not_in_ingredients_expect_key_error(self):
        with self.assertRaises(KeyError) as err:
            self.paint_factory.remove_ingredient("white", 10)
        expected_msg = "'No such ingredient in the factory'"
        self.assertEqual(expected_msg, str(err.exception))

    def test_remove_ingredient__when_quantity_exceeds_ingredient_quantity_expect_value_error(self):
        self.paint_factory.add_ingredient("white", 5)
        with self.assertRaises(ValueError) as err:
            self.paint_factory.remove_ingredient("white", 10)
        expected_msg = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected_msg, str(err.exception))

    def test_remove_ingredient__expect_to_decrease_ingredient_quantity_with_given(self):
        self.paint_factory.add_ingredient("white", 10)
        self.paint_factory.remove_ingredient("white", 5)
        expected = {"white": 5}
        self.assertEqual(expected, self.paint_factory.products)


if __name__ == "__main__":
    unittest.main()
