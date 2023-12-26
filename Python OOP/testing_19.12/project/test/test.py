from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Alpine', "AI", 1000, 1000)

    def test_init_(self):
        self.assertEqual('Alpine', self.robot.category)
        self.assertEqual("AI", self.robot.part_type)
        self.assertEqual(1000, self.robot.capacity)
        self.assertEqual(1000, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_allowed_categories(self):
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'], self.robot.ALLOWED_CATEGORIES)

    def test_check_category_setter_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Other"
        self.assertEqual(f"Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']", str(ve.exception))

    def test_correct_capacity_consumption(self):
        self.robot.installed_software.append({"name": "Microsoft", 'capacity_consumption': 100, 'memory_consumption': 100})
        result = self.robot.get_used_capacity()
        expected = 100
        self.assertEqual(expected, result)

    def test_correct_available_capacity(self):
        self.robot.installed_software.append(
            {"name": "Microsoft", 'capacity_consumption': 100, 'memory_consumption': 100})
        self.assertEqual(900, self.robot.get_available_capacity())

    def test_get_used_memory(self):
        self.robot.installed_software.append(
            {"name": "Microsoft", 'capacity_consumption': 100, 'memory_consumption': 100})
        self.assertEqual(900, self.robot.get_available_memory())

    def test_get_available_memory(self):
        self.robot.installed_software.append(
            {"name": "Microsoft", 'capacity_consumption': 100, 'memory_consumption': 100})
        self.assertEqual(900, self.robot.get_available_memory())

    def test_software_can_be_installed_returns_string(self):
        result = self.robot.install_software(
            {"name": "Microsoft", 'capacity_consumption': 100, 'memory_consumption': 100})
        expected = "Software 'Microsoft' successfully installed on Alpine part."
        self.assertEqual(expected, result)

    def test_appends_software(self):
        self.robot.install_software(
            {"name": "Microsoft", 'capacity_consumption': 100, 'memory_consumption': 100})
        result = 1
        expected = len(self.robot.installed_software)
        self.assertEqual(expected, result)


    def test_software_cannot_be_installed(self):
        result = self.robot.install_software(
            {"name": "Microsoft", 'capacity_consumption': 1100, 'memory_consumption': 1100})
        expected = "Software 'Microsoft' cannot be installed on Alpine part."
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()