def favSkill(skill):
    return f"My favourite skill is {skill} !"

def finalPrice(amount, discountPercentage):
    """
    Calculates final Price after applying discount of <discountPercentage> on it.
    
    Args:
    amount(int): Original Price
    discountPercentage(int): Percentage Discount
    
    Returns:
    finalAmount(float): Price after applying Discount
    
    """
    discountAmt = (discountPercentage / 100) * amount
    finalAmount = amount - discountAmt
    return finalAmount

def greet(name):
    return f"Welcome to Data Analysis, {name} !"

