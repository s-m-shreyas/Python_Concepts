# type: ignore
"""
05_class_attributes.py

Introduces class attributes.

This file focuses on:

    - What class attributes are
    - Creating class attributes
    - Accessing class attributes
    - Sharing class attributes across instances
    - Modifying class attributes
    - Instance attributes vs class attributes
    - Attribute lookup
    - Shadowing class attributes with instance attributes

Instance attributes were covered in:

    04_instance_attributes.py

Object and class namespaces are covered separately in:

    06_object_namespace.py
    07_class_namespace.py
"""


# ============================================================
# 1. WHAT IS A CLASS ATTRIBUTE?
# ============================================================

"""
A class attribute is an attribute defined directly inside a
class body.

Unlike an instance attribute, it belongs to the class itself.

Example:

    class Employee:
        company = "ABC"

Here, 'company' is a class attribute.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


print(Employee.company)


# ============================================================
# 2. ACCESSING A CLASS ATTRIBUTE THROUGH AN INSTANCE
# ============================================================

"""
A class attribute can also be accessed through an instance.

Python can look for the attribute on the class when it is not
found directly on the instance.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


employee = Employee()

print(employee.company)
print(Employee.company)


# ============================================================
# 3. CLASS ATTRIBUTES ARE SHARED
# ============================================================

"""
A class attribute represents data associated with the class
rather than with one particular instance.

Therefore, instances can access the same class attribute.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


first = Employee()
second = Employee()

print(first.company)
print(second.company)

print(first.company == second.company)


# ============================================================
# 4. INSTANCE ATTRIBUTES VS CLASS ATTRIBUTES
# ============================================================

"""
Consider:

    self.name

and:

    company = "ABC"

The first is an instance attribute.

The second is a class attribute.

Instance attribute:
    belongs to an individual instance.

Class attribute:
    belongs to the class.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"

    def __init__(self, name: str) -> None:
        self.name = name


first = Employee("Shreyas")
second = Employee("Rahul")

print(first.name)
print(second.name)

print(first.company)
print(second.company)


# ============================================================
# 5. CLASS ATTRIBUTE REPRESENTS SHARED INFORMATION
# ============================================================

"""
Class attributes are useful when information is common to all
instances of a class.

For example, all employees may belong to the same company.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"

    def __init__(self, name: str) -> None:
        self.name = name


first = Employee("Shreyas")
second = Employee("Rahul")

print(first.company)
print(second.company)


# ============================================================
# 6. CLASS ATTRIBUTE CAN BE MODIFIED THROUGH THE CLASS
# ============================================================

"""
A class attribute can be reassigned through the class.

Existing instances that do not have an instance attribute
with the same name will observe the new class-level value.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


first = Employee()
second = Employee()

print(first.company)
print(second.company)

Employee.company = "XYZ"

print(first.company)
print(second.company)


# ============================================================
# 7. CLASS ATTRIBUTE IS NOT COPIED INTO EACH INSTANCE
# ============================================================

"""
A class attribute is not automatically copied into every
instance's own namespace.

The instance can access it through attribute lookup.

This distinction becomes clearer when inspecting __dict__.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"

    def __init__(self, name: str) -> None:
        self.name = name


employee = Employee("Shreyas")

print(employee.__dict__)
print(Employee.__dict__["company"])


# ============================================================
# 8. CLASS ATTRIBUTE LOOKUP
# ============================================================

"""
When accessing:

    employee.company

Python first looks for 'company' on the instance.

If it does not find the attribute there, Python can continue
looking at the class.

Therefore, the class attribute can be found.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


employee = Employee()

print(employee.company)


# ============================================================
# 9. INSTANCE ATTRIBUTE CAN SHADOW A CLASS ATTRIBUTE
# ============================================================

"""
An instance can have an attribute with the same name as a
class attribute.

The instance attribute then takes precedence when accessed
through that instance.

This is called attribute shadowing.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


employee = Employee()

employee.company = "XYZ"

print(employee.company)
print(Employee.company)


# ============================================================
# 10. SHADOWING DOES NOT CHANGE THE CLASS ATTRIBUTE
# ============================================================

"""
Creating an instance attribute with the same name does not
modify the original class attribute.

It creates a separate attribute on the instance.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


employee = Employee()

employee.company = "XYZ"

print("Instance:", employee.company)
print("Class:", Employee.company)


# ============================================================
# 11. DIFFERENT INSTANCES CAN SHADOW DIFFERENTLY
# ============================================================

"""
One instance can shadow a class attribute while another
instance continues using the class attribute.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


first = Employee()
second = Employee()

first.company = "XYZ"

print(first.company)
print(second.company)
print(Employee.company)


# ============================================================
# 12. INSTANCE ATTRIBUTE HAS PRIORITY
# ============================================================

"""
When an instance has its own attribute, that value is found
before the class attribute for normal instance access.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


employee = Employee()

employee.company = "XYZ"

print(employee.company)


# ============================================================
# 13. DELETING THE INSTANCE ATTRIBUTE REVEALS THE CLASS
# ============================================================

"""
If the instance attribute is deleted, the class attribute
becomes visible again through the instance.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


employee = Employee()

employee.company = "XYZ"

print(employee.company)

del employee.company

print(employee.company)


# ============================================================
# 14. CLASS ATTRIBUTES CAN BE USED FOR CONSTANT-LIKE DATA
# ============================================================

"""
Class attributes are sometimes used for values that are
intended to be shared by every instance.

By convention, constant-like class attributes are often
written using uppercase names.
"""


class Employee:
    """Represent an employee."""

    COMPANY_NAME = "ABC"
    MAX_WORKING_HOURS = 8


print(Employee.COMPANY_NAME)
print(Employee.MAX_WORKING_HOURS)


# ============================================================
# 15. CLASS ATTRIBUTES CAN REPRESENT CONFIGURATION
# ============================================================

"""
Class attributes can also hold configuration shared by
instances.
"""


class Server:
    """Represent a server configuration."""

    default_port = 8080


first_server = Server()
second_server = Server()

print(first_server.default_port)
print(second_server.default_port)


# ============================================================
# 16. CLASS ATTRIBUTES CAN BE MUTABLE
# ============================================================

"""
A class attribute can refer to a mutable object such as a list.

In that case, all instances accessing that class attribute
can refer to the same mutable object.

This is sometimes useful, but it can also cause unintended
shared state.
"""


class Team:
    """Represent a team."""

    members: list[str] = []


first = Team()
second = Team()

first.members.append("Shreyas")

print(first.members)
print(second.members)


# ============================================================
# 17. WHY SHARED MUTABLE CLASS ATTRIBUTES CAN BE DANGEROUS
# ============================================================

"""
The previous example demonstrates that the list belongs to
the class-level state.

Both instances see the same list.

If each instance needs its own list, the list should instead
be created as an instance attribute.
"""


class ShoppingCart:
    """Represent an independent shopping cart."""

    def __init__(self) -> None:
        self.items: list[str] = []


first_cart = ShoppingCart()
second_cart = ShoppingCart()

first_cart.items.append("Laptop")

print(first_cart.items)
print(second_cart.items)


# ============================================================
# 18. CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE
# ============================================================

"""
Consider this class:

    class Employee:
        company = "ABC"

        def __init__(self, name):
            self.name = name

Here:

    company
        -> class attribute

    name
        -> instance attribute

company is shared conceptually.

name belongs to each individual employee.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"

    def __init__(self, name: str) -> None:
        self.name = name


employee = Employee("Shreyas")

print("Name:", employee.name)
print("Company:", employee.company)


# ============================================================
# 19. CLASS ATTRIBUTE ACCESS THROUGH THE CLASS
# ============================================================

"""
Class attributes can be accessed directly through the class.

This makes the ownership explicit.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


print(Employee.company)


# ============================================================
# 20. CLASS ATTRIBUTE ACCESS THROUGH AN INSTANCE
# ============================================================

"""
The same class attribute can be accessed through an instance
when the instance does not have its own attribute with that
name.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


employee = Employee()

print(employee.company)


# ============================================================
# 21. CLASS ATTRIBUTE AND INSTANCE ATTRIBUTE CAN HAVE
#     THE SAME NAME
# ============================================================

"""
The same attribute name can exist at both levels:

    class
        company = "ABC"

    instance
        employee.company = "XYZ"

The instance-level attribute shadows the class-level one.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


employee = Employee()

print(employee.company)

employee.company = "XYZ"

print(employee.company)
print(Employee.company)


# ============================================================
# 22. CLASS ATTRIBUTES ARE AVAILABLE BEFORE INSTANCES EXIST
# ============================================================

"""
Because class attributes belong to the class, they can be
accessed without creating an instance.
"""


class Configuration:
    """Store application configuration."""

    version = "1.0"
    debug = False


print(Configuration.version)
print(Configuration.debug)


# ============================================================
# 23. CLASS ATTRIBUTES CAN BE MODIFIED THROUGH CLASS METHODS
#     PREVIEW
# ============================================================

"""
A class can provide behavior that changes class-level data.

This is only a preview of class methods.

Class methods are covered in detail in:

    02_classes/06_class_methods.py
"""


class Counter:
    """Represent a class-level counter."""

    total = 0

    def __init__(self) -> None:
        Counter.total += 1


first = Counter()
second = Counter()
third = Counter()

print(Counter.total)


# ============================================================
# 24. INSTANCE STATE VS CLASS STATE
# ============================================================

"""
We can now distinguish:

    Instance state
        -> data belonging to one particular object.

    Class state
        -> data associated with the class and potentially
           shared by its instances.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"

    def __init__(self, name: str) -> None:
        self.name = name


first = Employee("Shreyas")
second = Employee("Rahul")

print("First name:", first.name)
print("Second name:", second.name)

print("Company:", Employee.company)


# ============================================================
# 25. CONCEPTUAL MODEL
# ============================================================

"""
The object model can now be extended:

    Class
       |
       +-- Class Attributes
       |       |
       |       +-- class-level data
       |
       +-- Methods
       |
       |
       +------ creates ------+
                           |
                           v
                       Instance
                           |
                           +-- Instance Attributes
                           |       |
                           |       +-- instance-level state
                           |
                           +-- Methods

Important distinction:

    Instance attribute
        belongs to an individual object.

    Class attribute
        belongs to the class and can be accessed by instances.
"""


# ============================================================
# 26. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. A class attribute is defined directly in the class body.

2. Class attributes belong to the class.

3. Instances can access class attributes.

4. Class attributes can represent information shared by
   instances.

5. Class attributes are not automatically copied into each
   instance's namespace.

6. If an instance does not contain an attribute, Python can
   find the corresponding class attribute.

7. An instance attribute can shadow a class attribute with
   the same name.

8. Shadowing does not modify the class attribute.

9. Deleting the instance attribute can reveal the class
   attribute again.

10. Mutable class attributes can create shared mutable state.

11. Class attributes can be accessed directly through the
    class.

12. Instance attributes represent individual object state.

13. Class attributes represent class-level or shared state.

The next file focuses on namespaces and how Python stores
and organizes these attributes.
"""