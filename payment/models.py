"""
Payment processing models for e-commerce platform.
Handles transaction records and payment methods.
"""

class PaymentTransaction:
    """Stores payment transaction records"""
    transaction_id: str
    amount: float
    currency: str
    status: str  # pending, completed, failed
    created_at: str

class PaymentMethod:
    """Stores customer payment methods"""
    card_last_four: str
    card_type: str
    expiry_month: int
    expiry_year: int
