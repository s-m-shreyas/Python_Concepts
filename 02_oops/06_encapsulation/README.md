# Encapsulation

"""
Encapsulation is the idea of restricting direct access to
internal details of an object and exposing only the required
interface.

In Python, encapsulation is mostly implemented by convention,
with a strong emphasis on clear design rather than strict
private access control.
"""

# ============================================================
# KEY IDEA
# ============================================================

# Public members: accessible everywhere
# Protected members: intended for internal use (single underscore)
# Private members: hidden by name mangling (double underscore)

# ============================================================
# TOPICS IN THIS FOLDER
# ============================================================

# 1. Public members
# 2. Protected convention
# 3. Private members
# 4. Name mangling

# ============================================================
# WHY ENCAPSULATION MATTERS
# ============================================================

# - Protects the internal state of an object
# - Prevents accidental misuse of attributes
# - Encourages controlled access through methods
# - Improves maintainability and readability

# ============================================================
# NOTE
# ============================================================

# Python does not enforce encapsulation as strictly as some
# languages such as Java or C++. Instead, it relies on naming
# conventions, method design, and the runtime name-mangling
# behavior for private members.
