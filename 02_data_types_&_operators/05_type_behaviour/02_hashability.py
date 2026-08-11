"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Special Data Types

Subcategory
-----------
Type Behaviour

Topic
-----
Hashability

Overview
--------
Hashability determines whether an object can provide a stable hash value.

A hashable object:

    - has a hash value that does not change during its lifetime
    - can be used as a dictionary key
    - can be stored as an element of a set

Common hashable types:

    - int
    - float
    - complex
    - bool
    - str
    - bytes
    - tuple (when all elements are hashable)
    - frozenset (when all elements are hashable)
    - None

Common unhashable types:

    - list
    - set
    - dict
    - bytearray

Important:
-----------
Hashability and immutability are strongly related, but they are not exactly
the same concept.

A tuple is immutable, but it is hashable only when all of its elements are
hashable.

A frozenset is immutable and hashable when all of its elements are hashable.

This file covers:

    - hash()
    - Hashable objects
    - Unhashable objects
    - Hashability and dictionary keys
    - Hashability and sets
    - Immutable types
    - Mutable types
    - Tuple hashability
    - Frozenset hashability
    - Nested hashability
    - Equality and hashing
    - Hash stability
    - Custom classes
    - __hash__
    - __eq__
    - Hashable vs immutable
"""


# =============================================================================
# 01. Basic hash()
# =============================================================================

hash_integer_value: int = 100

hash_integer_result: int = hash(
    hash_integer_value
)

print(
    f"Value: "
    f"{hash_integer_value!r}"
)

print(
    f"Hash: "
    f"{hash_integer_result}"
)


# hash() returns an integer hash value for a hashable object.


# =============================================================================
# 02. Hashing a String
# =============================================================================

hash_string_value: str = "Python"

hash_string_result: int = hash(
    hash_string_value
)

print(
    f"String: "
    f"{hash_string_value!r}"
)

print(
    f"Hash: "
    f"{hash_string_result}"
)


# Strings are hashable.


# =============================================================================
# 03. Hashing a Float
# =============================================================================

hash_float_value: float = 25.5

hash_float_result: int = hash(
    hash_float_value
)

print(
    f"Float: "
    f"{hash_float_value!r}"
)

print(
    f"Hash: "
    f"{hash_float_result}"
)


# Floats are hashable.


# =============================================================================
# 04. Hashing a Complex Number
# =============================================================================

hash_complex_value: complex = 3 + 4j

hash_complex_result: int = hash(
    hash_complex_value
)

print(
    f"Complex: "
    f"{hash_complex_value!r}"
)

print(
    f"Hash: "
    f"{hash_complex_result}"
)


# Complex numbers are hashable.


# =============================================================================
# 05. Hashing a Boolean
# =============================================================================

hash_boolean_value: bool = True

hash_boolean_result: int = hash(
    hash_boolean_value
)

print(
    f"Boolean: "
    f"{hash_boolean_value!r}"
)

print(
    f"Hash: "
    f"{hash_boolean_result}"
)


# bool is hashable.


# =============================================================================
# 06. Hashing None
# =============================================================================

hash_none_value: None = None

hash_none_result: int = hash(
    hash_none_value
)

print(
    f"None: "
    f"{hash_none_value!r}"
)

print(
    f"Hash: "
    f"{hash_none_result}"
)


# None is hashable.


# =============================================================================
# 07. Hashing Bytes
# =============================================================================

hash_bytes_value: bytes = b"Python"

hash_bytes_result: int = hash(
    hash_bytes_value
)

print(
    f"Bytes: "
    f"{hash_bytes_value!r}"
)

print(
    f"Hash: "
    f"{hash_bytes_result}"
)


# bytes objects are hashable.


# =============================================================================
# 08. Hashing a Tuple
# =============================================================================

hash_tuple_value: tuple[int, ...] = (
    10,
    20,
    30,
)

hash_tuple_result: int = hash(
    hash_tuple_value
)

print(
    f"Tuple: "
    f"{hash_tuple_value!r}"
)

print(
    f"Hash: "
    f"{hash_tuple_result}"
)


# A tuple can be hashable when all of its elements are hashable.


# =============================================================================
# 09. Hashing a Frozenset
# =============================================================================

hash_frozenset_value: frozenset[int] = frozenset(
    {10, 20, 30}
)

hash_frozenset_result: int = hash(
    hash_frozenset_value
)

print(
    f"Frozenset: "
    f"{hash_frozenset_value!r}"
)

print(
    f"Hash: "
    f"{hash_frozenset_result}"
)


# frozenset is hashable when all of its elements are hashable.


# =============================================================================
# 10. List Is Unhashable
# =============================================================================

hash_list_value: list[int] = [
    10,
    20,
    30,
]

print(
    f"List: "
    f"{hash_list_value!r}"
)


# The following would raise:
#
#     TypeError: unhashable type: 'list'
#
# hash(hash_list_value)
#
# It is intentionally not executed here so the teaching file continues.


# =============================================================================
# 11. Set Is Unhashable
# =============================================================================

hash_set_value: set[int] = {
    10,
    20,
    30,
}

print(
    f"Set: "
    f"{hash_set_value!r}"
)


# A normal set is mutable and therefore unhashable.


# =============================================================================
# 12. Dictionary Is Unhashable
# =============================================================================

hash_dictionary_value: dict[str, int] = {
    "Python": 100,
    "SQL": 90,
}

print(
    f"Dictionary: "
    f"{hash_dictionary_value!r}"
)


# Dictionaries are mutable and unhashable.


# =============================================================================
# 13. Bytearray Is Unhashable
# =============================================================================

hash_bytearray_value: bytearray = bytearray(
    b"Python"
)

print(
    f"Bytearray: "
    f"{hash_bytearray_value!r}"
)


# bytearray is mutable and therefore unhashable.


# =============================================================================
# 14. Hashability and Dictionary Keys
# =============================================================================

hash_dictionary_integer_key: dict[int, str] = {
    100: "Python",
}

hash_dictionary_string_key: dict[str, str] = {
    "Python": "Language",
}

hash_dictionary_tuple_key: dict[tuple[int, int], str] = {
    (10, 20): "Coordinate",
}

print(
    f"Integer key: "
    f"{hash_dictionary_integer_key!r}"
)

print(
    f"String key: "
    f"{hash_dictionary_string_key!r}"
)

print(
    f"Tuple key: "
    f"{hash_dictionary_tuple_key!r}"
)


# Dictionary keys must be hashable.


# =============================================================================
# 15. Hashability and Set Elements
# =============================================================================

hash_set_integer_values: set[int] = {
    10,
    20,
    30,
}

hash_set_string_values: set[str] = {
    "Python",
    "SQL",
}

hash_set_tuple_values: set[tuple[int, int]] = {
    (10, 20),
    (30, 40),
}

print(
    f"Integer set: "
    f"{hash_set_integer_values!r}"
)

print(
    f"String set: "
    f"{hash_set_string_values!r}"
)

print(
    f"Tuple set: "
    f"{hash_set_tuple_values!r}"
)


# Set elements must be hashable.


# =============================================================================
# 16. Tuple Hashability Depends on Its Elements
# =============================================================================

hash_tuple_hashable: tuple[int, str] = (
    100,
    "Python",
)

hash_tuple_hashable_result: int = hash(
    hash_tuple_hashable
)

print(
    f"Hashable tuple: "
    f"{hash_tuple_hashable!r}"
)

print(
    f"Hash: "
    f"{hash_tuple_hashable_result}"
)


# Every element is hashable.
#
# Therefore the tuple is hashable.


# =============================================================================
# 17. Tuple Containing a List
# =============================================================================

hash_tuple_with_list: tuple[list[int], ...] = (
    [10, 20],
)

print(
    f"Tuple containing list: "
    f"{hash_tuple_with_list!r}"
)


# The tuple itself is immutable.
#
# But its list element is mutable.
#
# Therefore the tuple is not hashable.
#
# hash(hash_tuple_with_list)
#
# would raise:
#
#     TypeError: unhashable type: 'list'


# =============================================================================
# 18. Tuple Containing a Set
# =============================================================================

hash_tuple_with_set: tuple[set[int], ...] = (
    {10, 20},
)

print(
    f"Tuple containing set: "
    f"{hash_tuple_with_set!r}"
)


# The tuple is not hashable because its element is unhashable.


# =============================================================================
# 19. Nested Hashable Tuple
# =============================================================================

hash_nested_tuple: tuple[tuple[int, int], ...] = (
    (10, 20),
    (30, 40),
)

hash_nested_tuple_result: int = hash(
    hash_nested_tuple
)

print(
    f"Nested tuple: "
    f"{hash_nested_tuple!r}"
)

print(
    f"Hash: "
    f"{hash_nested_tuple_result}"
)


# All nested elements are hashable.
#
# Therefore the outer tuple is hashable.


# =============================================================================
# 20. Frozenset With Hashable Elements
# =============================================================================

hash_frozen_numbers: frozenset[int] = frozenset(
    {10, 20, 30}
)

hash_frozen_numbers_result: int = hash(
    hash_frozen_numbers
)

print(
    f"Frozenset: "
    f"{hash_frozen_numbers!r}"
)

print(
    f"Hash: "
    f"{hash_frozen_numbers_result}"
)


# =============================================================================
# 21. Frozenset With Unhashable Elements
# =============================================================================

# The following would fail during construction:
#
#     frozenset(
#         {[10, 20]}
#     )
#
# because a list is unhashable and cannot be an element of a frozenset.


# =============================================================================
# 22. Hash Value Is an Integer
# =============================================================================

hash_integer_type_value: str = "Data"

hash_integer_type_result: int = hash(
    hash_integer_type_value
)

print(
    f"Hash: "
    f"{hash_integer_type_result!r}"
)

print(
    f"Hash type: "
    f"{type(hash_integer_type_result).__name__!r}"
)


# hash() returns an integer.


# =============================================================================
# 23. Equal Objects Must Have Equal Hashes
# =============================================================================

hash_equal_integer_a: int = 100
hash_equal_integer_b: int = 100

hash_equal_result: bool = (
    hash_equal_integer_a == hash_equal_integer_b
)

hash_equal_hash_result: bool = (
    hash(hash_equal_integer_a)
    == hash(hash_equal_integer_b)
)

print(
    f"Equal values: "
    f"{hash_equal_result}"
)

print(
    f"Equal hashes: "
    f"{hash_equal_hash_result}"
)


# Python's hashing contract requires:
#
# If:
#
#     a == b
#
# then:
#
#     hash(a) == hash(b)


# =============================================================================
# 24. Different Objects Can Have Equal Values
# =============================================================================

hash_equal_strings_left: str = "".join(
    ["Py", "thon"]
)

hash_equal_strings_right: str = "Python"

print(
    f"Equal values: "
    f"{hash_equal_strings_left == hash_equal_strings_right}"
)

print(
    f"Equal hashes: "
    f"{hash(hash_equal_strings_left) == hash(hash_equal_strings_right)}"
)


# Equal values should produce equal hashes.


# =============================================================================
# 25. Hash Does Not Guarantee Different Values
# =============================================================================

"""
A hash value is not the object itself.

Conceptually:

    object
       ↓
    hash()
       ↓
    integer

Different objects can theoretically produce the same hash.

This is called a hash collision.

Therefore:

    same hash
        does NOT necessarily mean
    same object

and does not necessarily mean:

    objects are equal
"""


# =============================================================================
# 26. Hash Stability
# =============================================================================

hash_stable_text: str = "Python"

hash_stable_first: int = hash(
    hash_stable_text
)

hash_stable_second: int = hash(
    hash_stable_text
)

print(
    f"First hash: "
    f"{hash_stable_first}"
)

print(
    f"Second hash: "
    f"{hash_stable_second}"
)

print(
    f"Same hash during execution: "
    f"{hash_stable_first == hash_stable_second}"
)


# A hashable object's hash must remain stable while the object
# is being used as a hash-based key.


# =============================================================================
# 27. Hashability and Mutability
# =============================================================================

"""
The relationship can be summarized as:

    mutable object
        ↓
    contents can change
        ↓
    hash could become invalid
        ↓
    generally unhashable

This is why common mutable containers are unhashable:

    list
    set
    dict
    bytearray


Immutable objects are commonly hashable:

    int
    float
    str
    bytes
    tuple
    frozenset

But remember:

    immutable does not automatically mean hashable.

A tuple containing an unhashable object is not hashable.
"""


# =============================================================================
# 28. Custom Class - Default Hash Behaviour
# =============================================================================

class HashDefaultExample:
    """Example custom class."""


hash_custom_instance_a: HashDefaultExample = (
    HashDefaultExample()
)

hash_custom_instance_b: HashDefaultExample = (
    HashDefaultExample()
)

print(
    f"Hash A: "
    f"{hash(hash_custom_instance_a)}"
)

print(
    f"Hash B: "
    f"{hash(hash_custom_instance_b)}"
)


# User-defined objects are normally hashable by identity unless
# equality/hash behaviour is customized.


# =============================================================================
# 29. Custom Class As Dictionary Key
# =============================================================================

class HashDictionaryKeyExample:
    """Example object used as a dictionary key."""


hash_custom_key_object: HashDictionaryKeyExample = (
    HashDictionaryKeyExample()
)

hash_custom_object_dictionary: dict[
    HashDictionaryKeyExample,
    str,
] = {
    hash_custom_key_object: "stored value",
}

print(
    f"Dictionary: "
    f"{hash_custom_object_dictionary!r}"
)


# A hashable custom object can be used as a dictionary key.


# =============================================================================
# 30. Custom Class As Set Element
# =============================================================================

class HashSetElementExample:
    """Example object used in a set."""


hash_custom_set_object: HashSetElementExample = (
    HashSetElementExample()
)

hash_custom_object_set: set[HashSetElementExample] = {
    hash_custom_set_object,
}

print(
    f"Set: "
    f"{hash_custom_object_set!r}"
)


# Hashable custom objects can be stored in sets.


# =============================================================================
# 31. Custom Equality Can Affect Hashability
# =============================================================================

class HashEqualityExample:
    """Class demonstrating custom equality."""

    def __eq__(
        self,
        other_value: Any,
    ) -> bool:
        return self is other_value


hash_equality_instance: HashEqualityExample = (
    HashEqualityExample()
)

print(
    f"Object created: "
    f"{hash_equality_instance!r}"
)


# Defining custom __eq__ can affect the availability of __hash__.
#
# Python may make the class unhashable unless __hash__ is also provided.


# =============================================================================
# 32. Explicit Hash Method
# =============================================================================

class HashExplicitExample:
    """Class with an explicit hash method."""

    def __hash__(self) -> int:
        return 100


hash_explicit_instance: HashExplicitExample = (
    HashExplicitExample()
)

hash_explicit_result: int = hash(
    hash_explicit_instance
)

print(
    f"Explicit hash: "
    f"{hash_explicit_result}"
)


# __hash__ controls the hash value returned for the object.


# =============================================================================
# 33. Equality and Hash Contract
# =============================================================================

class HashContractExample:
    """Class demonstrating equality/hash relationship."""

    def __init__(
        self,
        identifier_value: int,
    ) -> None:
        self.identifier_value = identifier_value

    def __eq__(
        self,
        other_value: Any,
    ) -> bool:
        if not isinstance(
            other_value,
            HashContractExample,
        ):
            return NotImplemented

        return (
            self.identifier_value
            == other_value.identifier_value
        )

    def __hash__(self) -> int:
        return hash(self.identifier_value)


hash_contract_left: HashContractExample = (
    HashContractExample(100)
)

hash_contract_right: HashContractExample = (
    HashContractExample(100)
)

print(
    f"Equal objects: "
    f"{hash_contract_left == hash_contract_right}"
)

print(
    f"Equal hashes: "
    f"{hash(hash_contract_left) == hash(hash_contract_right)}"
)


# If two objects compare equal,
# their hash values must also be equal.


# =============================================================================
# 34. Custom Hashable Objects as Dictionary Keys
# =============================================================================

hash_contract_dictionary: dict[
    HashContractExample,
    str,
] = {
    hash_contract_left: "first object",
}

print(
    f"Dictionary lookup: "
    f"{hash_contract_dictionary[hash_contract_right]!r}"
)


# Because the two objects:
#
#     compare equal
#
# and:
#
#     have equal hashes
#
# they can represent the same logical dictionary key.


# =============================================================================
# 35. Mutable State and Hashing Danger
# =============================================================================

from typing import Any

class HashMutableStateExample:
    """Example showing why mutable hash state is dangerous."""

    def __init__(
        self,
        key_value: int,
    ) -> None:
        self.key_value = key_value

    def __eq__(
        self,
        other_value: Any,
    ) -> bool:
        if not isinstance(
            other_value,
            HashMutableStateExample,
        ):
            return NotImplemented

        return (
            self.key_value
            == other_value.key_value
        )

    def __hash__(self) -> int:
        return hash(self.key_value)


hash_mutable_state_object: HashMutableStateExample = (
    HashMutableStateExample(100)
)

print(
    f"Initial hash: "
    f"{hash(hash_mutable_state_object)}"
)

hash_mutable_state_object.key_value = 200

print(
    f"New hash: "
    f"{hash(hash_mutable_state_object)}"
)


# This design is dangerous when the object is already being used
# as a dictionary key or set element.
#
# If the hash changes after insertion, the hash table may no longer
# be able to locate the object correctly.


# =============================================================================
# 36. Hashability Does Not Mean "Unique"
# =============================================================================

hash_unique_first: str = "Python"
hash_unique_second: str = "Python"

print(
    f"Equal: "
    f"{hash_unique_first == hash_unique_second}"
)

print(
    f"Same hash: "
    f"{hash(hash_unique_first) == hash(hash_unique_second)}"
)


# Hashability does not make an object unique.
#
# Equal objects can have the same hash.


# =============================================================================
# 37. Hashability and Dictionary Lookup
# =============================================================================

hash_lookup_data: dict[str, int] = {
    "Python": 100,
    "SQL": 90,
}

hash_lookup_key: str = "Python"

print(
    f"Lookup result: "
    f"{hash_lookup_data[hash_lookup_key]}"
)


# Dictionaries use hashing internally to efficiently locate keys.


# =============================================================================
# 38. Hashability and Set Membership
# =============================================================================

hash_membership_values: set[str] = {
    "Python",
    "SQL",
    "AWS",
}

hash_membership_target: str = "Python"

print(
    f"Present in set: "
    f"{hash_membership_target in hash_membership_values}"
)


# Sets use hashing internally for membership operations.


# =============================================================================
# 39. Hashability Does Not Mean Immutability
# =============================================================================

class HashIdentityExample:
    """Default user-defined objects are commonly hashable."""


hash_identity_object: HashIdentityExample = (
    HashIdentityExample()
)

hash_identity_result: int = hash(
    hash_identity_object
)

print(
    f"Hashable custom object: "
    f"{hash_identity_result}"
)


# A custom object can be mutable and still be hashable by identity.
#
# Therefore:
#
#     hashable != immutable
#
# Hashability depends on the equality/hash contract.


# =============================================================================
# 40. Practical Type Summary
# =============================================================================

"""
Typical behaviour:

    Type          Mutable?       Hashable?

    int           No             Yes
    float         No             Yes
    complex       No             Yes
    bool          No             Yes
    str           No             Yes
    bytes         No             Yes
    tuple         No             Sometimes
    frozenset     No             Sometimes
    list          Yes            No
    set           Yes            No
    dict          Yes            No
    bytearray     Yes            No

For tuple:

    tuple(hashable values)
        -> hashable

    tuple(containing list)
        -> unhashable


For frozenset:

    frozenset(hashable values)
        -> hashable

    frozenset cannot contain an unhashable element.


Important:

    immutable
        does not always mean
    hashable

and:

    hashable
        does not always strictly mean
    immutable
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `hash(object)` returns an integer hash value for a hashable object.

✓ Hashable objects can be used as:

      dictionary keys

      set elements

✓ Common hashable types:

      int
      float
      complex
      bool
      str
      bytes
      None
      tuple*
      frozenset*

    *when all contained elements are hashable.

✓ Common unhashable types:

      list
      set
      dict
      bytearray

✓ A tuple is immutable but may still be unhashable.

Example:

      (10, 20, 30)
          -> hashable

      ([10, 20], 30)
          -> unhashable

because the list is unhashable.

✓ Hashability is required by dictionaries and sets.

✓ Equal objects must have equal hashes:

      a == b
          implies
      hash(a) == hash(b)

✓ Equal hash values do not prove that two objects are equal.

✓ A hash value is not an object identity.

✓ Hashes need to remain stable while an object is used as a
  dictionary key or set element.

✓ Changing state that contributes to a custom object's hash is dangerous.

✓ Defining `__eq__` affects hashing behaviour.

✓ A custom class can explicitly define `__hash__`.

✓ Hashability and immutability are related but are not identical concepts.

Core relationship:

      object
        │
        ├── hashable
        │      │
        │      ├── hash(object)
        │      ├── dictionary key
        │      └── set element
        │
        └── unhashable
               │
               ├── cannot be dictionary key
               └── cannot be set element

Important condition:

      hashable
          requires
      stable hash/equality behaviour

The practical rule:

      If an object is going to be used as a dictionary key
      or set element, it must be hashable.
"""


# =============================================================================
# End of File
# =============================================================================