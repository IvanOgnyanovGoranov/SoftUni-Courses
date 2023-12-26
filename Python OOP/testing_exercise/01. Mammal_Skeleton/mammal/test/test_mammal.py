from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Rocky", "Dog", "Bau Bau..")

    def test_if_animal_makes_sound(self):
        result = self.mammal.make_sound()
        expected_result = "Rocky makes Bau Bau.."
        self.assertEqual(result, expected_result)

    def test_find_kingdom(self):
        result = self.mammal.get_kingdom()
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_gets_info(self):
        result = self.mammal.info()
        expected_result = "Rocky is of type Dog"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
