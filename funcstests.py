# Project 2 - Moonlander
#
# Author: Abbey Towse
# Section: CPE 101-11
# Date: 4/16/2021

import unittest
from landerFuncs import *


class TestCases(unittest.TestCase):
    def test_update_acc_1(self):
        self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)

    def test_update_acc_2(self):
        self.assertAlmostEqual(updateAcceleration(1.62, -4.567), -3.099708)

    def test_update_acc_3(self):
        self.assertAlmostEqual(updateAcceleration(1.62, 50.678), 14.799672)

    def test_update_acc_4(self):
        self.assertAlmostEqual(updateAcceleration(0, 0), 0)

    def test_update_acc_5(self):
        self.assertAlmostEqual(updateAcceleration(-11.623, -34.56), 91.961176)

    def test_update_alt_1(self):
        self.assertAlmostEqual(updateAltitude(0, 0, 0), 0)

    def test_update_alt_2(self):
        self.assertAlmostEqual(updateAltitude(1300, 0, 15), 1307.5)

    def test_update_alt_3(self):
        self.assertAlmostEqual(updateAltitude(1260.31, -9.72, -3.2), 1248.99)

    def test_update_vel_1(self):
        self.assertAlmostEqual(updateVelocity(0, 0), 0)

    def test_update_vel_2(self):
        self.assertAlmostEqual(updateVelocity(-24.567, -9.55), -34.117)

    def test_update_vel_3(self):
        self.assertAlmostEqual(updateVelocity(20, 78), 98)

    def test_update_fuel_1(self):
        self.assertAlmostEqual(updateFuel(0, 0), 0)

    def test_update_fuel_2(self):
        self.assertAlmostEqual(updateFuel(500, 9), 491)

    def test_update_fuel_3(self):
        self.assertAlmostEqual(updateFuel(30.456, 2.345), 28.111)


if __name__ == '__main__':
    unittest.main()
