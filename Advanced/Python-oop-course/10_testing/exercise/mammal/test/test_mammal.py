from exercise.mammal.project.mammal import Mammal
import unittest


class MammalTests(unittest.TestCase):
    def setUp(self):
        self.dog = Mammal("Bob", "Dog", "Bark")

    def test_mammal_init__expect_parameters_to_be_set(self):
        self.assertEqual("Bob", self.dog.name)
        self.assertEqual("Dog", self.dog.type)
        self.assertEqual("Bark", self.dog.sound)
        self.assertEqual("animals", self.dog._Mammal__kingdom)

    def test_mammal_make_sound__expect_correct_string_format_output(self):
        expected = "Bob makes Bark"
        actual = self.dog.make_sound()
        self.assertEqual(expected, actual)

    def test_mammal_get_kingdom__expect_animals(self):
        expected = "animals"
        actual = self.dog.get_kingdom()
        self.assertEqual(expected, actual)

    def test_mammal_info__expect_correct_string_format_output(self):
        expected = "Bob is of type Dog"
        actual = self.dog.info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()