from mcp.server.fastmcp import FastMCP
import math
from typing import Union

mcp=FastMCP("MathServer")




Number = Union[int, float]



@mcp.tool()
def add(a: Number, b: Number) -> Number:
    """Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b.
    """
    return a + b


@mcp.tool()
def subtract(a: Number, b: Number) -> Number:
    """Subtract two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The result of a - b.
    """
    return a - b


@mcp.tool()
def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b.
    """
    return a * b


@mcp.tool()
def divide(a: Number, b: Number) -> Number:
    """Divide two numbers.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        The result of a / b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


@mcp.tool()
def power(base: Number, exponent: Number) -> Number:
    """Raise a number to a power.

    Args:
        base: The base number
        exponent: The exponent

    Returns:
        base raised to the power of exponent.
    """
    return math.pow(base, exponent)


@mcp.tool()
def square_root(x: Number) -> float:
    """Compute the square root of a number.

    Args:
        x: Input number (must be non-negative)

    Returns:
        The square root of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("Square root of negative number is not allowed.")
    return math.sqrt(x)


@mcp.tool()
def factorial(n: int) -> int:
    """Compute the factorial of an integer.

    Args:
        n: Non-negative integer

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial of negative number is not defined.")
    return math.factorial(n)


@mcp.tool()
def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor (GCD).

    Args:
        a: First integer
        b: Second integer

    Returns:
        The greatest common divisor of a and b.
    """
    return math.gcd(a, b)


@mcp.tool()
def lcm(a: int, b: int) -> int:
    """Compute the least common multiple (LCM).

    Args:
        a: First integer
        b: Second integer

    Returns:
        The least common multiple of a and b.
    """
    return abs(a * b) // math.gcd(a, b) if a and b else 0


@mcp.tool()
def sine(x: Number) -> float:
    """Compute the sine of an angle (in radians).

    Args:
        x: Angle in radians

    Returns:
        The sine of x.
    """
    return math.sin(x)


@mcp.tool()
def cosine(x: Number) -> float:
    """Compute the cosine of an angle (in radians).

    Args:
        x: Angle in radians

    Returns:
        The cosine of x.
    """
    return math.cos(x)


@mcp.tool()
def tangent(x: Number) -> float:
    """Compute the tangent of an angle (in radians).

    Args:
        x: Angle in radians

    Returns:
        The tangent of x.
    """
    return math.tan(x)

if __name__=='__main__':
    mcp.run(transport='stdio')
