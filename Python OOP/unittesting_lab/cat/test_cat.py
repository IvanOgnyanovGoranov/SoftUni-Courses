from unittest import TestCase, main

from testing_lab.cat.cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat('Kitty')

    def test_correct_initialization(self):
        self.assertEqual('Kitty', self.cat.name)

    def test_raises_exception_when_already_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_fed_equals_true_when_fed(self):
        self.cat.eat()
        result = self.cat.fed

        self.assertTrue(result)

    def test_cat_sleepy_equals_true_when_fed(self):
        self.cat.eat()
        result = self.cat.sleepy

        self.assertTrue(result)

    def test_cat_increases_size_by_one_when_fed(self):
        self.cat.eat()
        expected_result = 1

        self.assertEqual(expected_result, self.cat.size)

    def test_cat_cannot_sleep_when_not_fed_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleepy_equals_false_after_slept(self):
        self.cat.eat()
        self.cat.sleep()
        result = self.cat.sleepy

        self.assertFalse(result)


if __name__ == '__main__':
    main()