# type: ignore

"""
04_interface_design.py

Demonstrates interface design principles.

A good interface should be clear, focused, and easy to use.
"""


# ============================================================
# 1. GOOD INTERFACE DESIGN
# ============================================================

class PaymentService:
    """Interface for payment processing."""

    def pay(self, amount: float) -> str:
        """Process a payment and return a status message."""
        raise NotImplementedError


class CreditCardPayment(PaymentService):
    """Concrete implementation for card payments."""

    def pay(self, amount: float) -> str:
        return f"Paid {amount} via Credit Card"


class UpiPayment(PaymentService):
    """Concrete implementation for UPI payments."""

    def pay(self, amount: float) -> str:
        return f"Paid {amount} via UPI"


payments = [CreditCardPayment(), UpiPayment()]
for payment in payments:
    print(payment.pay(500.0))

"""
The interface is simple and consistent.
Clients can call pay() without caring about the exact implementation.
"""


# ============================================================
# 2. POOR INTERFACE DESIGN
# ============================================================

class BadPaymentService:
    """This interface mixes many unrelated responsibilities."""

    def pay(self, amount: float) -> str:
        raise NotImplementedError

    def connect_to_database(self) -> None:
        pass

    def log_metrics(self) -> None:
        pass

    def send_email_notification(self) -> None:
        pass

"""
This is harder to understand because one interface is doing too much.
"""


# ============================================================
# 3. PRINCIPLES OF GOOD INTERFACE DESIGN
# ============================================================

# - keep it focused and minimal
# - expose only essential behavior
# - avoid mixing unrelated concerns
# - prefer clear method names
# - make implementations predictable and consistent


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - good interfaces are simple and coherent
# - bad interfaces become hard to use and maintain
# - interface design matters for scalability and readability
# - separation of concerns leads to better class design
