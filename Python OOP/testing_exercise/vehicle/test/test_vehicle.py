from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(40.0, 150.0)

    def test_correct_init(self):
        self.assertEqual(40.0, self.vehicle.fuel)
        self.assertEqual(40.0, self.vehicle.capacity)
        self.assertEqual(150.0, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_if_fuel_is_enough_for_a_drive(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(45)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_fuel_decrease_after_drive(self):
        self.vehicle.drive(20)
        self.assertEqual(15, self.vehicle.fuel)

    def test_refuel_car_raises_exception_if_not_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_fuel_increase_after_refuel(self):
        self.vehicle.capacity = 60
        self.vehicle.refuel(20)
        self.assertEqual(60, self.vehicle.fuel)

    def test__str__returns_as_expected(self):
        result = str(self.vehicle)
        expected = f"The vehicle has 150.0 " \
               f"horse power with 40.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, expected)




if __name__ == '__main__':
    main()