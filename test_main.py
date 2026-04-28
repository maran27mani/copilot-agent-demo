#!/usr/bin/env python3
"""
Unit tests for main.py calculator application.
Tests cover arithmetic operations, input validation, and edge cases.
"""

import pytest
from unittest.mock import patch
from main import add, subtract, multiply, divide, is_numeric, get_numeric_input


class TestArithmeticOperations:
    """Test suite for basic arithmetic operations."""
    
    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        assert add(5, 3) == 8
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, 5) == -5
    
    def test_add_with_decimals(self):
        """Test addition with decimal numbers."""
        assert add(5.5, 3.2) == pytest.approx(8.7)
        assert add(0.1, 0.2) == pytest.approx(0.3)
    
    def test_add_with_zero(self):
        """Test addition with zero."""
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        assert subtract(10, 3) == 7
        assert subtract(20, 5) == 15
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(5, -3) == 8
    
    def test_subtract_with_decimals(self):
        """Test subtraction with decimal numbers."""
        assert subtract(10.5, 3.2) == pytest.approx(7.3)
        assert subtract(5.5, 5.5) == pytest.approx(0.0)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        assert multiply(5, 3) == 15
        assert multiply(10, 20) == 200
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-5, -3) == 15
        assert multiply(-5, 3) == -15
    
    def test_multiply_with_decimals(self):
        """Test multiplication with decimal numbers."""
        assert multiply(5.5, 2) == pytest.approx(11.0)
        assert multiply(2.5, 4.0) == pytest.approx(10.0)
    
    def test_multiply_with_zero(self):
        """Test multiplication with zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0


class TestDivision:
    """Test suite for division operation and edge cases."""
    
    def test_divide_positive_numbers(self):
        """Test division of two positive numbers."""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-10, 2) == -5
        assert divide(-10, -2) == 5
    
    def test_divide_with_decimals(self):
        """Test division with decimal numbers."""
        assert divide(10.0, 2.5) == pytest.approx(4.0)
        assert divide(7.5, 2.5) == pytest.approx(3.0)
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a non-zero number."""
        assert divide(0, 5) == 0


class TestInputValidation:
    """Test suite for is_numeric() input validation function."""
    
    def test_is_numeric_with_integer_string(self):
        """Test validation with integer strings."""
        assert is_numeric("5") is True
        assert is_numeric("42") is True
        assert is_numeric("0") is True
    
    def test_is_numeric_with_negative_integer(self):
        """Test validation with negative integer strings."""
        assert is_numeric("-5") is True
        assert is_numeric("-100") is True
    
    def test_is_numeric_with_float_string(self):
        """Test validation with float strings."""
        assert is_numeric("5.5") is True
        assert is_numeric("3.14159") is True
        assert is_numeric("0.0") is True
    
    def test_is_numeric_with_negative_float(self):
        """Test validation with negative float strings."""
        assert is_numeric("-5.5") is True
        assert is_numeric("-3.14") is True
    
    def test_is_numeric_with_scientific_notation(self):
        """Test validation with scientific notation."""
        assert is_numeric("1e5") is True
        assert is_numeric("1.5e-3") is True
    
    def test_is_numeric_with_invalid_string(self):
        """Test validation with non-numeric strings."""
        assert is_numeric("hello") is False
        assert is_numeric("abc123") is False
        assert is_numeric("12.34.56") is False
    
    def test_is_numeric_with_empty_string(self):
        """Test validation with empty string."""
        assert is_numeric("") is False
    
    def test_is_numeric_with_special_characters(self):
        """Test validation with special characters."""
        assert is_numeric("!@#$") is False
        assert is_numeric("5!") is False
        assert is_numeric("$100") is False
    
    def test_is_numeric_with_whitespace(self):
        """Test validation with whitespace."""
        assert is_numeric("   ") is False
        assert is_numeric(" 5 ") is True  # float() can handle leading/trailing whitespace
    
    def test_is_numeric_with_none(self):
        """Test validation with None type."""
        assert is_numeric(None) is False


class TestGetNumericInput:
    """Test suite for get_numeric_input() function with mocked input."""
    
    @patch('builtins.input', return_value='42')
    def test_get_numeric_input_valid_integer(self, mock_input):
        """Test getting valid integer input."""
        result = get_numeric_input("Enter a number: ")
        assert result == 42.0
        mock_input.assert_called_once()
    
    @patch('builtins.input', return_value='3.14')
    def test_get_numeric_input_valid_float(self, mock_input):
        """Test getting valid float input."""
        result = get_numeric_input("Enter a number: ")
        assert result == pytest.approx(3.14)
    
    @patch('builtins.input', side_effect=['invalid', 'not_a_number', '99'])
    def test_get_numeric_input_retry_on_invalid(self, mock_input):
        """Test that function retries on invalid input."""
        result = get_numeric_input("Enter a number: ")
        assert result == 99.0
        assert mock_input.call_count == 3
    
    @patch('builtins.input', return_value='  -42.5  ')
    def test_get_numeric_input_with_whitespace(self, mock_input):
        """Test that whitespace is stripped from input."""
        result = get_numeric_input("Enter a number: ")
        assert result == -42.5


class TestEdgeCases:
    """Test suite for edge cases and boundary conditions."""
    
    def test_add_very_large_numbers(self):
        """Test addition with very large numbers."""
        result = add(1e308, 1e308)
        assert result == pytest.approx(2e308)
    
    def test_multiply_very_small_decimals(self):
        """Test multiplication with very small decimals."""
        result = multiply(0.0001, 0.0001)
        assert result == pytest.approx(1e-8)
    
    def test_divide_resulting_in_very_small_number(self):
        """Test division resulting in very small number."""
        result = divide(1, 1e308)
        assert result == pytest.approx(1e-308)
    
    def test_arithmetic_with_mixed_types(self):
        """Test that arithmetic works with mixed int and float types."""
        assert add(5, 2.5) == 7.5
        assert subtract(10.0, 3) == 7.0
        assert multiply(4, 2.5) == 10.0
        assert divide(10.0, 2) == 5.0


if __name__ == "__main__":
    # Run tests with: pytest test_main.py -v
    pytest.main([__file__, "-v"])
