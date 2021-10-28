"""
saving central savings
"""

def money_growth(amount, years=10):
    """
    Calculates the money growth
    Returns the amount
    """
    if years < 0:
        raise ValueError("Can't turn back time")
    interest = 0.0078

    growth = amount * interest * years

    return round(growth, 2)
