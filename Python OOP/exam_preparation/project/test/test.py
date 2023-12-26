from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self) -> None:
        self.t3t = Trip(10000, 3, True)
        self.t2f = Trip(10000, 2, False)
        self.t1f = Trip(10000, 1, False)

    def test_correct_init_(self):
        self.assertEqual(10000, self.t3t.budget)
        self.assertEqual(3, self.t3t.travelers)
        self.assertEqual(True, self.t3t.is_family)
        self.assertEqual({}, self.t3t.booked_destinations_paid_amounts)

    def test_travelers_less_than_one_returns_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.t3t.travelers = 0
        self.assertEqual('At least one traveler is required!', str(error.exception))

    def test_family_setter(self):
        self.t2f.is_family = True
        self.assertTrue(self.t2f.is_family)

    def test_book_a_trip_if_destination_not_in_destination_dictionary(self):
        self.assertEqual('This destination is not in our offers, please choose a new one!', self.t3t.book_a_trip("Dublin"))

    def test_returns_budget_not_enough_after_booking_(self):
        self.assertEqual(self.t3t.book_a_trip("Australia"), 'Your budget is not enough!')

    def test_correct_budget_for_family_trip(self):
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 8650.00', self.t3t.book_a_trip("Bulgaria"))

    def test_booked_trip_no_family_discount(self):
        self.assertEqual(f'Successfully booked destination Australia! Your budget left is 4300.00', self.t1f.book_a_trip("Australia"))
        self.assertEqual({'Australia': 5700}, self.t1f.booked_destinations_paid_amounts)

    def test_booking_status_no_booking(self):
        self.assertEqual(self.t3t.booking_status(), 'No bookings yet. Budget: 10000.00')

    def test_booking_status_with_booking(self):
        self.t1f.book_a_trip("Bulgaria")
        self.t1f.book_a_trip("Australia")
        result = self.t1f.booking_status()
        expected_result = "Booked Destination: Australia\n" \
                          "Paid Amount: 5700.00\n" \
                          "Booked Destination: Bulgaria\n" \
                          "Paid Amount: 500.00\n" \
                          "Number of Travelers: 1\n" \
                          "Budget Left: 3800.00"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
