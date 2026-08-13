# type: ignore

"""
04_concrete_implementations.py

Shows concrete subclasses that implement an abstract interface.

The abstract base class defines the required behaviour. Each
subclass provides its own real implementation.
"""

from abc import ABC, abstractmethod


# ============================================================
# 1. ABSTRACT INTERFACE
# ============================================================

class PaymentMethod(ABC):
    """Abstract payment interface."""

    @abstractmethod
    def pay(self, amount: float) -> str:
        """Handle a payment."""
        pass


# ============================================================
# 2. CONCRETE CLASS 1: CREDIT CARD
# ============================================================

class CreditCardPayment(PaymentMethod):
    """Pay with a credit card."""

    def pay(self, amount: float) -> str:
        return f"Paid {amount} using Credit Card"


# ============================================================
# 3. CONCRETE CLASS 2: UPI
# ============================================================

class UpiPayment(PaymentMethod):
    """Pay with UPI."""

    def pay(self, amount: float) -> str:
        return f"Paid {amount} using UPI"


# ============================================================
# 4. CONCRETE CLASS 3: CASH
# ============================================================

class CashPayment(PaymentMethod):
    """Pay with cash."""

    def pay(self, amount: float) -> str:
        return f"Paid {amount} using Cash"


# ============================================================
# 5. SAME METHOD NAME, DIFFERENT IMPLEMENTATION
# ============================================================

payments = [
    CreditCardPayment(),
    UpiPayment(),
    CashPayment(),
]

for payment in payments:
    print(payment.pay(250.0))

"""
Each object belongs to a different subclass, but all share the
same pay() method contract.
This is the essence of abstraction plus polymorphism.
"""


# ============================================================
# 6. ABSTRACT BASE CLASS PROVIDES COMMON RULES
# ============================================================

# A PaymentMethod instance cannot be created directly.
# But each subclass can define a useful real implementation.

# This is important because the system can work with a list of
# PaymentMethod objects without caring which exact payment type it is.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Concrete classes implement the abstract contract.
# - The same method name can behave differently in each subclass.
# - Abstraction helps keep code flexible and reusable.
# - This pattern is very common in real-world applications.
# - It supports maintainable design and polymorphic behavior.
