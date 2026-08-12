# type: ignore
"""
06_object_namespace.py

Introduces the object namespace.

This file focuses on:

    - What an object namespace is
    - Instance namespace
    - __dict__
    - Storing instance attributes
    - Reading and modifying __dict__
    - Relationship between attributes and namespaces
    - Instance namespace vs class namespace
    - Attribute lookup at a conceptual level

Class namespaces are covered separately in:

    07_class_namespace.py
"""


# ============================================================
# 1. WHAT IS A NAMESPACE?
# ============================================================

"""
A namespace is a mapping between names and the objects those
names refer to.

In the context of an object, its namespace contains attributes
directly associated with that object.
"""


# ============================================================
# 2. INSTANCE OBJECTS CAN HAVE A __dict__
# ============================================================

"""
Many ordinary Python objects have a __dict__ attribute.

The __dict__ provides access to the object's instance namespace.

For example, if an object has:

    name
    age

its __dict__ can show those attributes.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person("Shreyas", 29)

print(person.__dict__)


# ============================================================
# 3. INSTANCE ATTRIBUTES APPEAR IN __dict__
# ============================================================

"""
When an instance attribute is created using:

    self.name = value

the attribute is normally stored in the instance's namespace.

That namespace can be observed through __dict__.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person("Shreyas", 29)

print(person.name)
print(person.age)

print(person.__dict__)


# ============================================================
# 4. __dict__ IS A DICTIONARY
# ============================================================

"""
For ordinary objects that provide __dict__, the instance
namespace is represented by a dictionary.

The keys are attribute names.

The values are the corresponding objects.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person("Shreyas", 29)

print(type(person.__dict__))
print(person.__dict__)


# ============================================================
# 5. ATTRIBUTE NAMES BECOME DICTIONARY KEYS
# ============================================================

"""
If an instance contains:

    self.name = "Shreyas"

the namespace conceptually contains:

    "name": "Shreyas"
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.__dict__["name"])


# ============================================================
# 6. ATTRIBUTE ACCESS AND __dict__ ACCESS
# ============================================================

"""
These two expressions access the same stored instance
attribute in an ordinary object:

    person.name

    person.__dict__["name"]

The first uses normal attribute syntax.

The second directly accesses the instance namespace.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.name)
print(person.__dict__["name"])


# ============================================================
# 7. ADDING AN ATTRIBUTE UPDATES THE NAMESPACE
# ============================================================

"""
Adding a new instance attribute causes the instance namespace
to contain another entry.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.__dict__)

person.age = 29

print(person.__dict__)


# ============================================================
# 8. MODIFYING AN ATTRIBUTE UPDATES ITS NAMESPACE ENTRY
# ============================================================

"""
Reassigning an instance attribute changes the corresponding
value in the instance namespace.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.__dict__)

person.name = "Arjun"

print(person.__dict__)


# ============================================================
# 9. DELETING AN ATTRIBUTE REMOVES IT FROM THE NAMESPACE
# ============================================================

"""
Deleting an instance attribute removes its entry from the
instance namespace.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.__dict__)

del person.name

print(person.__dict__)


# ============================================================
# 10. DIFFERENT INSTANCES HAVE DIFFERENT NAMESPACES
# ============================================================

"""
Each ordinary instance has its own instance namespace.

Therefore, two objects created from the same class can have
different namespace contents.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


first = Person("Shreyas", 29)
second = Person("Rahul", 30)

print(first.__dict__)
print(second.__dict__)


# ============================================================
# 11. INSTANCE NAMESPACES ARE INDEPENDENT
# ============================================================

"""
Changing one instance's attributes changes its namespace,
not another instance's namespace.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


first = Person("Shreyas")
second = Person("Rahul")

first.name = "Arjun"

print(first.__dict__)
print(second.__dict__)


# ============================================================
# 12. ADDING DIFFERENT ATTRIBUTES TO DIFFERENT INSTANCES
# ============================================================

"""
Different instances can even have different sets of
instance attributes.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


first = Person("Shreyas")
second = Person("Rahul")

first.age = 29
second.city = "Bengaluru"

print(first.__dict__)
print(second.__dict__)


# ============================================================
# 13. __dict__ CAN BE MODIFIED DIRECTLY
# ============================================================

"""
For ordinary objects with a writable __dict__, entries can
also be added directly to the namespace dictionary.

This is useful for understanding the relationship between
attributes and the namespace.

Normal application code should generally prefer normal
attribute assignment.
"""


class Person:
    """Represent a person."""


person = Person()

person.__dict__["name"] = "Shreyas"

print(person.name)
print(person.__dict__)


# ============================================================
# 14. DIRECT __dict__ MODIFICATION
# ============================================================

"""
Changing a value through __dict__ affects the corresponding
attribute.
"""


class Person:
    """Represent a person."""


person = Person()

person.__dict__["name"] = "Shreyas"

print(person.name)

person.__dict__["name"] = "Arjun"

print(person.name)


# ============================================================
# 15. __dict__ IS NOT THE OBJECT ITSELF
# ============================================================

"""
The __dict__ is a representation of the object's namespace.

It should not be confused with the object itself.

The object still has its own identity and type.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print("Object identity:", id(person))
print("Object type:", type(person))
print("Object namespace:", person.__dict__)


# ============================================================
# 16. METHODS ARE NOT STORED IN EACH INSTANCE'S __dict__
# ============================================================

"""
Consider:

    person.greet()

The method is defined by the class.

It normally does not appear as a separate entry inside every
instance's __dict__.

This distinction is important:

    Instance namespace
        -> instance-specific attributes

    Class namespace
        -> class-defined attributes and methods
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a greeting."""
        return f"Hello, {self.name}!"


person = Person("Shreyas")

print(person.__dict__)

print(person.greet())


# ============================================================
# 17. ATTRIBUTE LOOKUP: INSTANCE FIRST
# ============================================================

"""
When accessing an attribute through an instance, Python can
look for the attribute in the instance's namespace.

For example:

    person.name

can find 'name' directly in:

    person.__dict__
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.__dict__)
print(person.name)


# ============================================================
# 18. CLASS ATTRIBUTES ARE NOT NORMALLY IN INSTANCE __dict__
# ============================================================

"""
A class attribute belongs to the class.

Therefore, it does not normally appear in the instance's
__dict__ simply because the instance can access it.
"""


class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.__dict__)

print(person.name)
print(person.species)


# ============================================================
# 19. INSTANCE SHADOWING CHANGES THE INSTANCE NAMESPACE
# ============================================================

"""
Suppose the class has:

    species = "Human"

If we then execute:

    person.species = "Robot"

the instance receives its own 'species' attribute.

That attribute appears in the instance namespace and shadows
the class attribute for that instance.
"""


class Person:
    """Represent a person."""

    species = "Human"


person = Person()

print(person.__dict__)
print(person.species)

person.species = "Robot"

print(person.__dict__)
print(person.species)

print(Person.species)


# ============================================================
# 20. __dict__ AND ATTRIBUTE EXISTENCE
# ============================================================

"""
The __dict__ can help demonstrate whether an attribute is
stored directly on an instance.

For example:

    "name" in person.__dict__

checks whether 'name' is directly stored in the instance
namespace.
"""


class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print("name" in person.__dict__)
print("species" in person.__dict__)


# ============================================================
# 21. INSTANCE NAMESPACE VS CLASS NAMESPACE
# ============================================================

"""
Consider:

    class Person:
        species = "Human"

        def __init__(self, name):
            self.name = name

The namespaces conceptually look like:

    Instance namespace:
        {
            "name": "Shreyas"
        }

    Class namespace:
        {
            "species": "Human",
            ...
        }

The class namespace is explored in detail in the next file.
"""


class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print("Instance namespace:", person.__dict__)
print("Class namespace contains species:", "species" in Person.__dict__)


# ============================================================
# 22. INSTANCE NAMESPACE CAN CONTAIN MUTABLE STATE
# ============================================================

"""
An instance namespace can contain references to mutable
objects.

Each instance can have its own mutable object.
"""


class ShoppingCart:
    """Represent a shopping cart."""

    def __init__(self) -> None:
        self.items: list[str] = []


first = ShoppingCart()
second = ShoppingCart()

print(first.__dict__)
print(second.__dict__)

first.items.append("Laptop")

print(first.__dict__)
print(second.__dict__)


# ============================================================
# 23. INSTANCE NAMESPACE IS OBJECT-SPECIFIC
# ============================================================

"""
The most important idea:

    Each ordinary instance has its own namespace.

Therefore:

    instance_1.__dict__

and:

    instance_2.__dict__

represent different namespaces.
"""


class Account:
    """Represent an account."""

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance


first = Account("Shreyas", 5000.0)
second = Account("Rahul", 3000.0)

print(first.__dict__)
print(second.__dict__)


# ============================================================
# 24. NAMESPACE AND OBJECT STATE
# ============================================================

"""
For ordinary objects, the instance namespace provides a useful
way to observe instance state.

For example:

    account.__dict__

shows the instance attributes currently stored on the object.
"""


class Account:
    """Represent an account."""

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance


account = Account("Shreyas", 5000.0)

print(account.__dict__)

account.balance = 7500.0

print(account.__dict__)


# ============================================================
# 25. IMPORTANT LIMITATION OF __dict__
# ============================================================

"""
Not every Python object necessarily has a __dict__.

Some objects use other mechanisms for storing attributes.

For example, certain built-in objects do not expose an
instance __dict__.

Therefore:

    __dict__

should be understood as the namespace dictionary available
on many ordinary Python objects, not as a universal property
of every object.
"""


numbers = [10, 20, 30]

print(hasattr(numbers, "__dict__"))


# ============================================================
# 26. __dict__ DOES NOT MEAN "ALL ATTRIBUTES"
# ============================================================

"""
An object's __dict__ contains attributes stored directly in
that object's namespace.

It does not necessarily contain every attribute that can be
accessed through the object.

Class attributes and inherited attributes are examples of
attributes that may be accessible without appearing in the
instance's __dict__.
"""


class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.__dict__)

print(person.name)
print(person.species)


# ============================================================
# 27. CONCEPTUAL ATTRIBUTE LOOKUP
# ============================================================

"""
A simplified conceptual model is:

    object.attribute

        |
        v
    Check instance namespace
        |
        |-- found --> use instance attribute
        |
        |-- not found
                |
                v
          Continue lookup through
          the class and inheritance
          hierarchy

The complete attribute lookup algorithm is more detailed and
will be studied later.
"""


# ============================================================
# 28. OBJECT NAMESPACE MODEL
# ============================================================

"""
We can now visualize the relationship:

    Class
       |
       +-- Class Namespace
       |       |
       |       +-- class attributes
       |       +-- methods
       |
       | creates
       v
    Instance
       |
       +-- Instance Namespace
               |
               +-- instance attributes

For:

    person = Person("Shreyas")

we can think of:

    person.__dict__
        ->
        {
            "name": "Shreyas"
        }

while the class contains its own namespace.
"""


# ============================================================
# 29. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. A namespace maps names to objects.

2. An ordinary Python instance commonly has an instance
   namespace exposed through __dict__.

3. Instance attributes are normally stored in that namespace.

4. __dict__ is a dictionary for objects that provide it.

5. Attribute names become keys in the instance namespace.

6. Attribute values become the corresponding dictionary values.

7. Adding an attribute adds an entry to the namespace.

8. Modifying an attribute changes its namespace entry.

9. Deleting an attribute removes its namespace entry.

10. Different instances have independent namespaces.

11. Class attributes do not normally appear in an instance's
    __dict__.

12. An instance can shadow a class attribute by creating an
    instance attribute with the same name.

13. __dict__ does not necessarily contain every attribute
    accessible through an object.

14. Not every Python object provides __dict__.

15. The instance namespace represents an important part of
    an object's state.

The next file focuses specifically on the class namespace and
how classes store attributes and methods.
"""