# type: ignore

"""
01_single_responsibility.py

Demonstrates the Single Responsibility Principle (SRP).

A class should have one clear reason to change.
It should focus on one responsibility instead of doing many unrelated jobs.
"""


# ============================================================
# 1. GOOD DESIGN: ONE RESPONSIBILITY
# ============================================================

class Invoice:
    """Responsible for invoice data."""

    def __init__(self, total: float) -> None:
        self.total = total

    def get_total(self) -> float:
        return self.total


class InvoicePrinter:
    """Responsible for printing the invoice."""

    def print_invoice(self, invoice: Invoice) -> None:
        print(f"Invoice total: {invoice.get_total()}")


invoice = Invoice(2500.0)
printer = InvoicePrinter()
printer.print_invoice(invoice)

"""
The invoice stores data.
The printer prints it.
Each class has a single purpose.
"""


# ============================================================
# 2. BAD DESIGN: MULTIPLE RESPONSIBILITIES
# ============================================================

class InvoiceManager:
    """This class does too much at once."""

    def __init__(self, total: float) -> None:
        self.total = total

    def get_total(self) -> float:
        return self.total

    def print_invoice(self) -> None:
        print(f"Invoice total: {self.total}")

    def save_to_database(self) -> None:
        print("Saving invoice to database.")

"""
This class mixes responsibilities such as:
- storing invoice details
- printing
- database persistence

This violates SRP.
"""


# ============================================================
# 3. WHY SRP MATTERS
# ============================================================

# - easier to understand
# - easier to maintain
# - lower risk of accidental changes
# - improved testing and modularity


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - A class should ideally do one thing well.
# - It should have one reason to change.
# - Strong class design leads to cleaner code.
# - SRP improves long-term maintainability.
