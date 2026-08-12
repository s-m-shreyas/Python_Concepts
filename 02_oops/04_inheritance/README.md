# 04 — Inheritance

Inheritance is an Object-Oriented Programming mechanism that allows one class to reuse and extend the attributes and methods of another class.

This folder covers inheritance from its basic forms through Method Resolution Order (MRO) and `super()`.

---

## Learning Objectives

By completing this folder, you should understand:

- What inheritance is
- Parent and child classes
- Single inheritance
- Multilevel inheritance
- Multiple inheritance
- Hierarchical inheritance
- Method inheritance
- Attribute inheritance
- Method overriding
- Attribute shadowing
- Method Resolution Order (MRO)
- `__mro__`
- `mro()`
- `super()`
- Cooperative multiple inheritance

---

# 1. Single Inheritance

**File:** `01_single_inheritance.py`

Single inheritance occurs when one child class inherits from one parent class.

```python
class Parent:
    pass


class Child(Parent):
    pass
```

Structure:

```text
Parent
   ↓
Child
```

Example:

```python
class Animal:
    def speak(self) -> None:
        print("Animal speaks.")


class Dog(Animal):
    pass


dog = Dog()

dog.speak()
```

`Dog` does not define `speak()`, but it can use the method because it inherits it from `Animal`.

A useful mental model is:

```text
Dog IS-A Animal
```

---

# 2. Multilevel Inheritance

**File:** `02_multilevel_inheritance.py`

Multilevel inheritance occurs when inheritance happens through multiple levels.

```python
class Animal:
    pass


class Mammal(Animal):
    pass


class Dog(Mammal):
    pass
```

Structure:

```text
Animal
   ↓
Mammal
   ↓
Dog
```

`Dog` inherits from `Mammal`, while `Mammal` inherits from `Animal`.

Therefore, `Dog` can access functionality inherited from both `Mammal` and `Animal`.

Conceptually:

```text
Dog
 ↓
Mammal
 ↓
Animal
 ↓
object
```

Example:

```python
class Animal:
    def breathe(self) -> None:
        print("Breathing")


class Mammal(Animal):
    def walk(self) -> None:
        print("Walking")


class Dog(Mammal):
    def bark(self) -> None:
        print("Barking")


dog = Dog()

dog.breathe()
dog.walk()
dog.bark()
```

Here:

- `breathe()` comes from `Animal`
- `walk()` comes from `Mammal`
- `bark()` comes from `Dog`

This demonstrates inheritance across multiple levels.

---

# 3. Multiple Inheritance

**File:** `03_multiple_inheritance.py`

Multiple inheritance occurs when one class inherits from more than one parent class.

```python
class Flyer:
    def fly(self) -> None:
        print("Flying")


class Swimmer:
    def swim(self) -> None:
        print("Swimming")


class Duck(Flyer, Swimmer):
    pass
```

Structure:

```text
Flyer ───┐
         ├──> Duck
Swimmer ─┘
```

Therefore:

```python
duck = Duck()

duck.fly()
duck.swim()
```

works because `Duck` inherits from both classes.

Multiple inheritance introduces an important question:

> What happens when both parent classes define an attribute or method with the same name?

Python solves this using **Method Resolution Order (MRO)**.

---

# 4. Hierarchical Inheritance

**File:** `04_hierarchical_inheritance.py`

Hierarchical inheritance occurs when multiple child classes inherit from the same parent.

```python
class Animal:
    def breathe(self) -> None:
        print("Breathing")


class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

Structure:

```text
        Animal
        /    \
      Dog    Cat
```

Both `Dog` and `Cat` inherit from `Animal`.

Example:

```python
dog = Dog()
cat = Cat()

dog.breathe()
cat.breathe()
```

The parent functionality is shared by multiple child classes.

---

# 5. Method Inheritance

**File:** `05_method_inheritance.py`

A child class can use methods defined in its parent without redefining them.

```python
class Animal:
    def speak(self) -> None:
        print("Animal speaks.")


class Dog(Animal):
    pass


dog = Dog()

dog.speak()
```

Python searches for `speak()` through the class hierarchy.

Conceptually:

```text
dog.speak()
     ↓
   Dog
     ↓
  Animal
     ↓
  speak()
```

The method is found in `Animal`.

---

## Method Overriding

A child class can provide its own implementation of a method inherited from the parent.

```python
class Animal:
    def speak(self) -> None:
        print("Animal speaks.")


class Dog(Animal):
    def speak(self) -> None:
        print("Dog barks.")


dog = Dog()

dog.speak()
```

Output:

```text
Dog barks.
```

The method in `Dog` overrides the method inherited from `Animal`.

The parent implementation still exists and can be reached using `super()`.

---

# 6. Attribute Inheritance

**File:** `06_attribute_inheritance.py`

Attributes can also be inherited.

```python
class Animal:
    kingdom = "Animalia"


class Dog(Animal):
    pass


dog = Dog()

print(dog.kingdom)
```

Output:

```text
Animalia
```

`Dog` can access `kingdom`, even though `kingdom` is defined in `Animal`.

An important point:

> The inherited attribute is not copied into the child class.

For example:

```python
print("kingdom" in Animal.__dict__)
print("kingdom" in Dog.__dict__)
```

Output:

```text
True
False
```

The attribute remains defined in `Animal`.

Python finds it through attribute lookup.

---

## Attribute Lookup

A simplified model of attribute lookup is:

```text
instance
   ↓
instance attributes
   ↓
class
   ↓
parent class
   ↓
next class according to MRO
   ↓
object
```

For example:

```python
class Animal:
    species = "Animal"


class Dog(Animal):
    pass


dog = Dog()

print(dog.species)
```

Python eventually finds:

```text
Animal.species
```

---

## Attribute Shadowing

An instance attribute can shadow a class attribute.

```python
class Person:
    name = "Class Name"


person = Person()

print(person.name)

person.name = "Alice"

print(person.name)
print(Person.name)
```

Output:

```text
Class Name
Alice
Class Name
```

Before assignment:

```text
person.name
    ↓
Person.name
```

After assignment:

```text
person.name
    ↓
person.__dict__["name"]
```

The instance attribute takes precedence over the class attribute for that instance.

---

## Removing the Shadowing Attribute

If the instance attribute is deleted:

```python
del person.name
```

the class attribute becomes visible again:

```python
print(person.name)
```

Output:

```text
Class Name
```

---

## Mutable Inherited Class Attributes

Be careful with mutable class attributes.

```python
class Parent:
    items: list[str] = []


class Child(Parent):
    pass


child = Child()

child.items.append("Python")

print(Parent.items)
print(Child.items)
print(child.items)
```

All three can refer to the same inherited list.

This happens because `items` is a class attribute defined by `Parent`.

This is different from:

```python
child.items = ["Python"]
```

Assignment creates an instance attribute instead of modifying the inherited class attribute.

---

# 7. Method Resolution Order

**File:** `07_method_resolution_order.py`

Method Resolution Order, or **MRO**, is the order in which Python searches classes when looking for an attribute or method.

For:

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

the MRO is:

```text
Dog
Animal
object
```

You can inspect it using:

```python
print(Dog.__mro__)
```

or:

```python
print(Dog.mro())
```

---

## MRO and Method Lookup

Consider:

```python
class Animal:
    def speak(self) -> None:
        print("Animal")


class Dog(Animal):
    pass


dog = Dog()

dog.speak()
```

Python searches according to the MRO:

```text
Dog
 ↓
Animal
 ↓
object
```

`speak()` is not found in `Dog`, so Python continues to `Animal`.

The method is found there.

---

## MRO and Method Overriding

Consider:

```python
class Animal:
    def speak(self) -> None:
        print("Animal")


class Dog(Animal):
    def speak(self) -> None:
        print("Dog")
```

The MRO is:

```text
Dog
Animal
object
```

When:

```python
Dog().speak()
```

is executed, Python finds `speak()` in `Dog` first.

Output:

```text
Dog
```

The first matching implementation in the MRO is used.

---

## MRO and Multiple Inheritance

Consider:

```python
class ParentA:
    value = "A"


class ParentB:
    value = "B"


class Child(ParentA, ParentB):
    pass
```

The MRO is:

```text
Child
ParentA
ParentB
object
```

Therefore:

```python
print(Child.value)
```

outputs:

```text
A
```

because `ParentA` appears before `ParentB`.

If the inheritance order is changed:

```python
class Child(ParentB, ParentA):
    pass
```

the MRO becomes:

```text
Child
ParentB
ParentA
object
```

and:

```python
print(Child.value)
```

outputs:

```text
B
```

Therefore:

> Parent order matters in multiple inheritance.

---

# Diamond Inheritance

A common multiple-inheritance structure is called **diamond inheritance**.

```text
        A
       / \
      B   C
       \ /
        D
```

Example:

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
```

The MRO is:

```text
D
B
C
A
object
```

Notice that `A` appears only once.

Python uses **C3 linearization** to calculate a consistent MRO.

You normally inspect the result using:

```python
print(D.__mro__)
```

rather than manually calculating it.

---

# 8. super()

**File:** `08_super_function.py`

`super()` provides access to the next implementation according to the Method Resolution Order.

A common beginner explanation is:

```text
super() = parent
```

This is useful initially, but it is not technically complete.

A better mental model is:

> `super()` continues attribute lookup from the next class in the MRO.

---

## Basic super()

```python
class Parent:
    def show(self) -> None:
        print("Parent")


class Child(Parent):
    def show(self) -> None:
        print("Child")
        super().show()


child = Child()

child.show()
```

Output:

```text
Child
Parent
```

The child performs its own behaviour and then delegates to the next implementation.

---

## super() With __init__()

One of the most common uses of `super()` is calling parent initialization.

```python
class Person:
    def __init__(self, name: str) -> None:
        self.name = name


class Student(Person):
    def __init__(self, name: str, grade: int) -> None:
        super().__init__(name)
        self.grade = grade


student = Student("Alice", 90)

print(student.__dict__)
```

Output:

```text
{'name': 'Alice', 'grade': 90}
```

The parent handles initialization of `name`.

The child handles initialization of `grade`.

---

## super() Extending Parent Behaviour

A child can extend the parent's behaviour instead of completely replacing it.

```python
class Animal:
    def speak(self) -> None:
        print("Animal sound")


class Dog(Animal):
    def speak(self) -> None:
        super().speak()
        print("Dog bark")


dog = Dog()

dog.speak()
```

Output:

```text
Animal sound
Dog bark
```

---

# super() and Multiple Inheritance

This is where `super()` becomes particularly powerful.

```python
class A:
    def show(self) -> None:
        print("A")


class B(A):
    def show(self) -> None:
        print("B")
        super().show()


class C(A):
    def show(self) -> None:
        print("C")
        super().show()


class D(B, C):
    def show(self) -> None:
        print("D")
        super().show()
```

The MRO is:

```text
D
B
C
A
object
```

Calling:

```python
D().show()
```

produces:

```text
D
B
C
A
```

Each class calls:

```python
super().show()
```

and Python continues through the MRO.

This is called **cooperative multiple inheritance**.

---

# super() vs Explicit Parent Calls

These two approaches are different.

An explicit parent call:

```python
Parent.show(self)
```

directly targets a specific class.

`super()`:

```python
super().show()
```

continues lookup according to the MRO.

This distinction becomes important in multiple inheritance.

Consider:

```text
D
↓
B
↓
C
↓
A
```

If `B` directly calls:

```python
A.show(self)
```

then `C` can be skipped.

If `B` calls:

```python
super().show()
```

Python continues according to the MRO.

Therefore, cooperative multiple inheritance generally relies on `super()`.

---

# Cooperative Multiple Inheritance

A cooperative inheritance structure allows every class to participate in the method chain.

```python
class A:
    def show(self) -> None:
        print("A")


class B(A):
    def show(self) -> None:
        print("B")
        super().show()


class C(A):
    def show(self) -> None:
        print("C")
        super().show()


class D(B, C):
    def show(self) -> None:
        print("D")
        super().show()


D().show()
```

MRO:

```text
D
B
C
A
object
```

Execution:

```text
D
B
C
A
```

This is one of the most important practical uses of `super()`.

---

# Inheritance vs MRO vs super()

These three concepts should be understood together.

## Inheritance

Defines the relationship between classes.

```python
class Child(Parent):
    pass
```

Inheritance creates the class hierarchy.

---

## MRO

Defines the lookup order.

```text
Child
Parent
object
```

Inspect it using:

```python
Child.__mro__
```

or:

```python
Child.mro()
```

---

## super()

Continues lookup from the next class in the MRO.

```python
super().method()
```

Therefore:

```text
Inheritance
    ↓
creates the class hierarchy
    ↓
MRO
    ↓
defines the lookup order
    ↓
super()
    ↓
continues through that lookup order
```

---

# Useful Introspection

Python provides several useful attributes and methods for understanding inheritance.

## __bases__

`__bases__` shows the direct parent classes.

```python
class Animal:
    pass


class Dog(Animal):
    pass


print(Dog.__bases__)
```

---

## __mro__

`__mro__` shows the complete Method Resolution Order.

```python
print(Dog.__mro__)
```

---

## mro()

`mro()` returns the MRO as a list.

```python
print(Dog.mro())
```

---

## __dict__

`__dict__` shows attributes defined directly by a class or instance.

```python
print(Dog.__dict__)
```

Important:

> `__dict__` does not contain inherited attributes simply because they are accessible.

---

# Common Mistakes

## 1. Thinking inherited attributes are copied

They generally are not.

```python
class Parent:
    value = 10


class Child(Parent):
    pass
```

This:

```python
print("value" in Child.__dict__)
```

returns:

```text
False
```

But:

```python
print(Child.value)
```

still works because Python finds `value` through inheritance.

---

## 2. Thinking super() simply means parent

A more accurate mental model is:

```text
super()
    ↓
continue lookup from the next class in the MRO
```

---

## 3. Thinking super() creates a parent object

It does not.

`super()` provides a proxy for accessing attributes and methods according to the MRO.

---

## 4. Confusing inheritance with overriding

Inheritance allows the child to reuse functionality.

Overriding occurs when the child provides its own implementation of an inherited method.

```python
class Parent:
    def show(self) -> None:
        print("Parent")


class Child(Parent):
    def show(self) -> None:
        print("Child")
```

`Child.show()` overrides `Parent.show()`.

The parent implementation still exists and can be reached using:

```python
super().show()
```

---

## 5. Ignoring parent order

With:

```python
class Child(A, B):
    pass
```

the order:

```text
A → B
```

matters.

Changing it to:

```python
class Child(B, A):
    pass
```

can change the MRO and therefore change which method or attribute Python finds first.

---

# Folder Structure

```text
04_inheritance/
│
├── 01_single_inheritance.py
├── 02_multilevel_inheritance.py
├── 03_multiple_inheritance.py
├── 04_hierarchical_inheritance.py
├── 05_method_inheritance.py
├── 06_attribute_inheritance.py
├── 07_method_resolution_order.py
├── 08_super_function.py
└── README.md
```

Recommended learning order:

```text
01_single_inheritance
        ↓
02_multilevel_inheritance
        ↓
03_multiple_inheritance
        ↓
04_hierarchical_inheritance
        ↓
05_method_inheritance
        ↓
06_attribute_inheritance
        ↓
07_method_resolution_order
        ↓
08_super_function
```

The progression is intentional:

```text
Basic inheritance
        ↓
Different inheritance structures
        ↓
Method inheritance
        ↓
Attribute inheritance
        ↓
MRO
        ↓
super()
        ↓
Cooperative multiple inheritance
```

---

# Final Mental Model

The entire folder can be reduced to this:

```text
                    Inheritance
                         │
                         ▼
                 Class hierarchy
                         │
                         ▼
            Attribute / Method lookup
                         │
                         ▼
                       MRO
                         │
                         ▼
                 First match wins
                         │
                         ▼
                      super()
                         │
                         ▼
             Continue through the MRO
```

For simple inheritance:

```text
Child
  ↓
Parent
  ↓
object
```

For multiple inheritance:

```text
        A
       / \
      B   C
       \ /
        D
```

Python calculates an MRO such as:

```text
D
B
C
A
object
```

If Python needs to find a method or attribute, it searches according to that order.

If a class wants to continue to the next implementation, it can use:

```python
super()
```

Therefore the three most important ideas are:

```text
Inheritance
    =
class relationship

MRO
    =
lookup order

super()
    =
continue lookup through the MRO
```

Once these three concepts are clear, Python's multiple inheritance behaviour becomes much easier to reason about.