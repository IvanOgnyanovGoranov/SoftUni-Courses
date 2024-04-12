from unittest import TestCase, main

from testing_lab.car_manager.car_manager import Car


class TestCarManager(TestCase):

    def setUp(self) -> None:
        self.car = Car('Mazda', '3', 10, 50)

    def test_correct_initialization(self):
        self.assertEqual('Mazda', self.car.make)
        self.assertEqual('3', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            car_no_make = Car('', '3', 10, 50)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            car_no_model = Car('Mazda', '', 10, 50)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_zero_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            car = Car('Mazda', '3', 0, 50)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_zero_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            car = Car('Mazda', '3', 10, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_less_than_zero_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_raises_ex_when_fuel_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_when_fuel_is_more_than_capacity(self):
        self.car.refuel(60)
        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_checks_if_fuel_is_taken_out_when_enough(self):
        self.car.refuel(60)
        self.car.drive(100)

        self.assertEqual(40, self.car.fuel_amount)

    def test_drive_when_not_enough_fuel(self):

        with self.assertRaises(Exception) as ex:
            self.car.refuel(5)
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()