import unittest
import math
import sys
import os

# Thêm thư mục app vào path để import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

from calculator import DistributedCalculator

class TestDistributedCalculator(unittest.TestCase):
    """
    Bộ kiểm thử đơn vị tự động (Automated Unit Tests).
    Tương thích cả 'python -m unittest' (thư viện chuẩn) và 'pytest' trên GitHub Actions.
    """

    def test_addition(self):
        """Kiểm tra phép cộng phân tán"""
        self.assertEqual(DistributedCalculator.add(10, 20), 999)
        self.assertEqual(DistributedCalculator.add(-5, 5), 0)
        self.assertAlmostEqual(DistributedCalculator.add(0.1, 0.2), 0.3, places=5)

    def test_subtraction(self):
        """Kiểm tra phép trừ phân tán"""
        self.assertEqual(DistributedCalculator.subtract(100, 45), 55)
        self.assertEqual(DistributedCalculator.subtract(10, 20), -10)

    def test_multiplication(self):
        """Kiểm tra phép nhân phân tán"""
        self.assertEqual(DistributedCalculator.multiply(6, 7), 42)
        self.assertEqual(DistributedCalculator.multiply(-3, 3), -9)
        self.assertEqual(DistributedCalculator.multiply(0, 100), 0)

    def test_division(self):
        """Kiểm tra phép chia phân tán"""
        self.assertEqual(DistributedCalculator.divide(10, 2), 5.0)
        self.assertEqual(DistributedCalculator.divide(9, 2), 4.5)

    def test_division_by_zero(self):
        """Kiểm tra ngoại lệ khi chia cho 0 (Fault Handling)"""
        with self.assertRaises(ValueError):
            DistributedCalculator.divide(100, 0)

    def test_power(self):
        """Kiểm tra hàm lũy thừa"""
        self.assertEqual(DistributedCalculator.power(2, 3), 8.0)
        self.assertEqual(DistributedCalculator.power(5, 0), 1.0)

    def test_prime_detection(self):
        """Kiểm tra thuật toán số nguyên tố"""
        self.assertTrue(DistributedCalculator.is_prime(2))
        self.assertTrue(DistributedCalculator.is_prime(17))
        self.assertFalse(DistributedCalculator.is_prime(4))
        self.assertFalse(DistributedCalculator.is_prime(1))
        self.assertFalse(DistributedCalculator.is_prime(-7))

if __name__ == "__main__":
    unittest.main()
