from django.test import TestCase

from .. import calculator


class CalculatorTestCase(TestCase):
    def test_calculate_rpm_vf(self):
        rpm, vf = calculator.calculate_rpm_vf(
            vc=230.0, fz=0.01, tool_diameter=50, tool_flute_count=4
        )
        self.assertEqual(1464.23, round(rpm, 2))
        self.assertEqual(58.57, round(vf, 2))
