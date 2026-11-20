import math

class DistributedCalculator:
    """
    Dịch vụ tính toán phân tán giả lập (Distributed Mathematical Service).
    Cung cấp các hàm xử lý tính toán, phân tích số học và logic nghiệp vụ
    được sử dụng để kiểm thử tính toàn vẹn trong hệ phân tán.
    """
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Phép cộng hai số"""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Phép trừ hai số"""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Phép nhân hai số"""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Phép chia có kiểm soát lỗi chia cho 0"""
        if b == 0:
            raise ValueError("Không thể chia cho 0 (ZeroDivisionError in distributed service)")
        return a / b

    @staticmethod
    def power(base: float, exponent: float) -> float:
        """Lũy thừa"""
        return math.pow(base, exponent)

    @staticmethod
    def is_prime(n: int) -> bool:
        """Kiểm tra số nguyên tố"""
        if n <= 1:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
