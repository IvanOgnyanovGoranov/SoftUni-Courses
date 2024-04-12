from unittest import TestCase, main

from testing_lab.worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker('Test', 1000, 50)

    def test_correct_initialization(self):
        self.assertEqual('Test', self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_decrease_energy_when_worker_has_enough_and_money_increase(self):
        expected_energy = self.worker.energy - 1
        expected_money = self.worker.salary

        self.worker.work()

        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_work_when_worker_does_not_have_energy_raises_exception(self):
        self.worker.energy = 0 #arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work() #act

        self.assertEqual('Not enough energy.', str(ex.exception)) #assert

    def test_energy_increase_when_resting(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returns_valid_string(self):
        expected_string = self.worker.get_info()

        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', expected_string)



if __name__ == '__main__':
    main()