from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car1 = SecondHandCar("Mercedes", "Sedan", 100000, 10000)

    def test_init_(self):
        self.assertEqual("Mercedes", self.car1.model)
        self.assertEqual("Sedan", self.car1.car_type)
        self.assertEqual(100000, self.car1.mileage)
        self.assertEqual(10000, self.car1.price)
        self.assertEqual([], self.car1.repairs)

    def test_low_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.price = 1
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car1.price = 0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_less_or_equal_to_100_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car1.mileage = 99
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_promotional_price_less_than_actual(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.set_promotional_price(12000)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_change_promo_price_successfully(self):
        result = self.car1.set_promotional_price(9000)
        self.assertEqual(result, 'The promotional price has been successfully set.')

    def test_high_repair_price_returns_string(self):
        result = self.car1.need_repair(6000, "change engine")
        self.assertEqual(result, 'Repair is impossible!')

    def test_successful_repair(self):
        result = self.car1.need_repair(3000, "new roof")
        self.assertEqual(self.car1.price, 13000)
        self.assertEqual(str(self.car1.repairs[0]), "new roof")
        self.assertEqual(result, 'Price has been increased due to repair charges.')

    def test_greater_than_when_mismatch_returns_str(self):
        car2 = SecondHandCar("Mercedes", "SUV", 100000, 8000)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car1.__gt__(car2))

    def test_returns_True_car_is_greater_price(self):
        car2 = SecondHandCar("Mercedes", "Sedan", 100000, 8000)
        self.assertEqual(True, self.car1.__gt__(car2))

    def test_returns_correct_string__str__(self):
        expected = f"""Model Mercedes | Type Sedan | Milage 100000km
Current price: 10000.00 | Number of Repairs: 0"""
        result = self.car1.__str__()
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()