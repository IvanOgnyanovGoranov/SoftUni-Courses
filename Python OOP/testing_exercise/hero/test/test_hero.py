from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 100, 50)
        self.enemy = Hero("Enemy", 1, 50, 25)

    def test_correct_init_(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(6.0, self.hero.health)
        self.assertEqual(3.0, self.hero.damage)

    def test_same_username_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_raises_value_error_if_health_less_than_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))




if __name__ == "__main__":
    main()