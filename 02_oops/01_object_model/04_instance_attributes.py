# type: ignore
"""
04_instance_attributes.py

Introduces instance attributes.

This file focuses on:

    - What instance attributes are
    - Creating instance attributes
    - Accessing instance attributes
    - Modifying instance attributes
    - Different objects having different instance state
    - Adding attributes after object creation
    - Removing instance attributes
    - Instance attributes and object identity
    - Instance attributes vs local variables

Class attributes are covered separately in:

    05_class_attributes.py
"""


# ============================================================
# 1. WHAT IS AN INSTANCE ATTRIBUTE?
# ============================================================

"""
An instance attribute is an attribute associated with a
particular object (instance).

For example:

    self.name

creates an attribute named 'name' on the current instance.

Each instance can have its own value for that attribute.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.name)


# ============================================================
# 2. INSTANCE ATTRIBUTES REPRESENT INSTANCE STATE
# ============================================================

"""
Instance attributes commonly represent the state of an
individual object.

For example, different Person objects can have different
names.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


first_person = Person("Shreyas")
second_person = Person("Rahul")

print(first_person.name)
print(second_person.name)


# ============================================================
# 3. EACH INSTANCE HAS ITS OWN ATTRIBUTE VALUE
# ============================================================

"""
Although both objects are created from the same class,
their instance attributes can contain different values.
"""

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


first_person = Person("Shreyas")
second_person = Person("Rahul")

print(first_person.name)
print(second_person.name)

print(first_person.name == second_person.name)


# ============================================================
# 4. self REFERS TO THE CURRENT INSTANCE
# ============================================================

"""
Inside an instance method, 'self' refers to the instance on
which that method is operating.

Therefore:

    self.name

means:

    "the name attribute belonging to this particular instance."
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def show_name(self) -> None:
        """Display the person's name."""
        print(self.name)


first_person = Person("Shreyas")
second_person = Person("Rahul")

first_person.show_name()
second_person.show_name()


# ============================================================
# 5. INSTANCE ATTRIBUTES ARE STORED PER OBJECT
# ============================================================

"""
Each object maintains its own instance attributes.

Changing an instance attribute on one object does not
automatically change the corresponding attribute on another
object.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


first_person = Person("Shreyas")
second_person = Person("Rahul")

first_person.name = "Arjun"

print(first_person.name)
print(second_person.name)


# ============================================================
# 6. MODIFYING AN INSTANCE ATTRIBUTE
# ============================================================

"""
An existing instance attribute can be reassigned.

The attribute remains associated with the same instance, but
its value changes.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print("Before:", person.name)

person.name = "Arjun"

print("After:", person.name)


# ============================================================
# 7. INSTANCE ATTRIBUTES CAN HAVE DIFFERENT TYPES
# ============================================================

"""
Instance attributes do not all have to contain the same type
of value.

However, in well-designed Python code, an attribute should
normally have a consistent meaning and expected type.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person("Shreyas", 29)

print(person.name)
print(person.age)


# ============================================================
# 8. MULTIPLE INSTANCE ATTRIBUTES
# ============================================================

"""
A class can initialize multiple instance attributes.

Each attribute contributes to the state of an individual
object.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int, city: str) -> None:
        self.name = name
        self.age = age
        self.city = city


person = Person("Shreyas", 29, "Bengaluru")

print(person.name)
print(person.age)
print(person.city)


# ============================================================
# 9. INSTANCE ATTRIBUTES CAN BE USED BY METHODS
# ============================================================

"""
Instance methods can read and use instance attributes through
'self'.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """Return a short introduction."""
        return f"My name is {self.name} and I am {self.age} years old."


person = Person("Shreyas", 29)

print(person.introduce())


# ============================================================
# 10. METHODS CAN MODIFY INSTANCE ATTRIBUTES
# ============================================================

"""
An instance method can also modify the state of its instance.

The method uses self to access the attribute belonging to
that particular object.
"""


class Counter:
    """Represent a simple counter."""

    def __init__(self, value: int) -> None:
        self.value = value

    def increment(self) -> None:
        """Increase the counter by one."""
        self.value += 1


counter = Counter(0)

print(counter.value)

counter.increment()

print(counter.value)


# ============================================================
# 11. DIFFERENT INSTANCES CAN CHANGE INDEPENDENTLY
# ============================================================

"""
Each instance has independent state.

Changing the counter value of one object does not change the
value stored by another object.
"""


class Counter:
    """Represent a simple counter."""

    def __init__(self, value: int) -> None:
        self.value = value

    def increment(self) -> None:
        """Increase the counter by one."""
        self.value += 1


first_counter = Counter(0)
second_counter = Counter(10)

first_counter.increment()
first_counter.increment()

print(first_counter.value)
print(second_counter.value)


# ============================================================
# 12. INSTANCE ATTRIBUTES CAN BE CREATED AFTER INITIALIZATION
# ============================================================

"""
Python allows an instance to receive a new attribute after
the object has already been created.

This attribute will belong only to that particular instance.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


first_person = Person("Shreyas")
second_person = Person("Rahul")

first_person.city = "Bengaluru"

print(first_person.city)


# ============================================================
# 13. A NEW ATTRIBUTE DOES NOT AUTOMATICALLY APPEAR
#    ON OTHER INSTANCES
# ============================================================

"""
The dynamically added attribute belongs only to the instance
on which it was created.

It does not automatically become an attribute of every
instance of the class.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


first_person = Person("Shreyas")
second_person = Person("Rahul")

first_person.city = "Bengaluru"

print(first_person.city)

print(hasattr(second_person, "city"))


# ============================================================
# 14. INSTANCE ATTRIBUTES CAN BE REMOVED
# ============================================================

"""
An instance attribute can be removed using del.

After deletion, accessing that attribute raises AttributeError.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.name)

del person.name

print(hasattr(person, "name"))


# ============================================================
# 15. INSTANCE ATTRIBUTES AND OBJECT IDENTITY
# ============================================================

"""
Changing an instance attribute does not normally create a
different instance.

The object keeps the same identity while its state changes.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

identity_before = id(person)

person.name = "Arjun"

identity_after = id(person)

print(person.name)
print(identity_before == identity_after)


# ============================================================
# 16. INSTANCE ATTRIBUTE VS LOCAL VARIABLE
# ============================================================

"""
An instance attribute and a local variable have different
roles.

    self.name

is associated with the object.

    name

inside a method can simply be a local variable.

The 'self.' prefix is what makes the attribute belong to the
instance.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        """Return a description using local and instance data."""
        message = f"Person: {self.name}"
        return message


person = Person("Shreyas")

print(person.describe())


# ============================================================
# 17. SAME ATTRIBUTE NAME, DIFFERENT INSTANCE STATE
# ============================================================

"""
The class can define the same attribute concept for every
instance while each instance stores its own value.
"""


class Employee:
    """Represent an employee."""

    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department


employee_one = Employee("Shreyas", "Data Engineering")
employee_two = Employee("Rahul", "Analytics")

print(employee_one.name)
print(employee_one.department)

print(employee_two.name)
print(employee_two.department)


# ============================================================
# 18. INSTANCE ATTRIBUTES CAN HOLD MUTABLE OBJECTS
# ============================================================

"""
An instance attribute can refer to a mutable object such as
a list.

Each instance can therefore have its own mutable state.
"""


class ShoppingCart:
    """Represent a shopping cart."""

    def __init__(self) -> None:
        self.items: list[str] = []

    def add_item(self, item: str) -> None:
        """Add an item to the cart."""
        self.items.append(item)


first_cart = ShoppingCart()
second_cart = ShoppingCart()

first_cart.add_item("Laptop")

print(first_cart.items)
print(second_cart.items)


# ============================================================
# 19. IMPORTANT: INSTANCE MUTABLE STATE MUST BE CREATED
#     PER INSTANCE
# ============================================================

"""
The list above is created inside __init__:

    self.items = []

Therefore, every ShoppingCart instance receives its own list.

This prevents different instances from unintentionally sharing
the same mutable state.

Shared mutable class attributes are a separate topic covered
in the class attributes section.
"""


class ShoppingCart:
    """Represent a shopping cart."""

    def __init__(self) -> None:
        self.items: list[str] = []


first_cart = ShoppingCart()
second_cart = ShoppingCart()

first_cart.items.append("Laptop")

print(first_cart.items)
print(second_cart.items)


# ============================================================
# 20. INSTANCE STATE CAN BE INSPECTED
# ============================================================

"""
An object's instance attributes can be inspected through
its __dict__ when the object provides an instance dictionary.

This reveals the attributes stored directly on that instance.

The mechanics of namespaces and __dict__ are covered in more
detail later.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person("Shreyas", 29)

print(person.__dict__)


# ============================================================
# 21. INSTANCE ATTRIBUTES BELONG TO INSTANCES
# ============================================================

"""
The key distinction is:

    Class
        defines what objects can have and do.

    Instance
        contains the state of one particular object.

Instance attributes therefore belong to individual instances.
"""


class Account:
    """Represent a simple account."""

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance


first_account = Account("Shreyas", 5000.0)
second_account = Account("Rahul", 3000.0)

print(first_account.__dict__)
print(second_account.__dict__)


# ============================================================
# 22. CONCEPTUAL MODEL
# ============================================================

"""
The object model can now be extended:

    Class
       |
       | creates
       v
    Instance
       |
       +-- Instance Attributes
       |       |
       |       +-- represent instance state
       |
       +-- Methods
               |
               +-- operate on instance state

For example:

    person = Person("Shreyas", 29)

The instance contains:

    name -> "Shreyas"
    age  -> 29

Another Person instance can contain different values.
"""


# ============================================================
# 23. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. An instance attribute belongs to a particular object.

2. Instance attributes commonly represent object state.

3. Instance attributes are commonly created using self.

4. self refers to the current instance inside an instance
   method.

5. Different instances can have different attribute values.

6. Changing an instance attribute changes that instance's
   state.

7. Changing one instance does not automatically change
   another instance.

8. New instance attributes can be added after object creation.

9. Instance attributes can be removed using del.

10. Instance identity normally remains unchanged when its
    attributes change.

11. Instance attributes can contain mutable objects.

12. Mutable instance state should normally be created per
    instance.

13. __dict__ can expose an object's instance namespace when
    available.

14. Instance attributes represent the state of individual
    objects.

The next file introduces class attributes and explains how
they differ from instance attributes.
"""