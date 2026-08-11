"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Multi-Valued Data Types

Data Type
---------
Memory View (`memoryview`)

Overview
--------
`memoryview` is a view object that provides access to the memory of another
object that supports Python's buffer protocol.

Unlike `bytes` and `bytearray`, a memoryview does not contain an independent
copy of the underlying binary data.

Conceptually:

    bytes
        owns immutable data

    bytearray
        owns mutable data

    memoryview
        views existing buffer data

Common objects that can provide a buffer include:

    - bytes
    - bytearray
    - array.array
    - other buffer-compatible objects

Memoryview is particularly useful when binary data is large and copying it
would be unnecessary or expensive.

This module covers:

    - Creation
    - Default and non-default values
    - Empty memoryview
    - Type identification
    - Runtime type checking
    - Length
    - Positive indexing
    - Negative indexing
    - Slicing
    - Iteration
    - Membership
    - Underlying object
    - Object identity
    - Read-only views
    - Writable views
    - format
    - itemsize
    - ndim
    - shape
    - strides
    - nbytes
    - tolist()
    - bytes()
    - bytearray()
    - hex()
    - release()
    - Hashability
    - Equality
    - Identity

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - Conversion

is covered separately under:

    17_type_behaviour/
"""


# =============================================================================
# 01. Creation
# =============================================================================

memoryview_creation_empty: memoryview = memoryview(b"")
memoryview_creation_bytes: memoryview = memoryview(b"Python")
memoryview_creation_bytearray: memoryview = memoryview(
    bytearray(b"Python")
)

print(f"Empty:     {memoryview_creation_empty!r}")
print(f"From bytes:{memoryview_creation_bytes!r}")
print(f"From bytearray: {memoryview_creation_bytearray!r}")


# =============================================================================
# 02. Default and Non-Default Values
# =============================================================================

memoryview_default_value: memoryview = memoryview(b"")

memoryview_non_default_alpha: memoryview = memoryview(
    b"Python"
)

memoryview_non_default_beta: memoryview = memoryview(
    bytearray(b"Data")
)

print(f"Default-like value: {memoryview_default_value!r}")
print(f"Non-default value:  {memoryview_non_default_alpha!r}")
print(f"Another value:      {memoryview_non_default_beta!r}")


# Type annotation alone does not create a memoryview:
#
#     value: memoryview
#
# Explicit initialization is required.


# =============================================================================
# 03. Empty Memoryview
# =============================================================================

memoryview_empty_example: memoryview = memoryview(b"")

print(f"Value:  {memoryview_empty_example!r}")
print(f"Length: {len(memoryview_empty_example)}")
print(f"Type:   {type(memoryview_empty_example)}")


# =============================================================================
# 04. Type Identification
# =============================================================================

memoryview_type_example: memoryview = memoryview(b"Python")

print(f"Value: {memoryview_type_example!r}")
print(f"Type:  {type(memoryview_type_example)}")


# =============================================================================
# 05. Runtime Type Checking
# =============================================================================

memoryview_type_candidate: object = memoryview(b"Python")

bytearray_type_candidate: object = bytearray(b"Python")

memoryview_is_memoryview: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    memoryview_type_candidate,
    memoryview,
)

bytearray_is_memoryview: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    bytearray_type_candidate,
    memoryview,
)

print(
    f"memoryview object is memoryview: "
    f"{memoryview_is_memoryview}"
)

print(
    f"bytearray object is memoryview: "
    f"{bytearray_is_memoryview}"
)


# =============================================================================
# 06. Length
# =============================================================================

memoryview_length_example: memoryview = memoryview(
    b"Python"
)

print(
    f"Length: {len(memoryview_length_example)}"
)


# =============================================================================
# 07. Positive Indexing
# =============================================================================

memoryview_positive_index_example: memoryview = memoryview(
    b"Python"
)

print(
    f"Index 0: {memoryview_positive_index_example[0]}"
)

print(
    f"Index 2: {memoryview_positive_index_example[2]}"
)


# A byte-oriented memoryview returns integer values when indexed.


# =============================================================================
# 08. Negative Indexing
# =============================================================================

memoryview_negative_index_example: memoryview = memoryview(
    b"Python"
)

print(
    f"Index -1: {memoryview_negative_index_example[-1]}"
)

print(
    f"Index -2: {memoryview_negative_index_example[-2]}"
)


# =============================================================================
# 09. Slicing
# =============================================================================

memoryview_slice_source: memoryview = memoryview(
    b"Python"
)

memoryview_slice_first: memoryview = (
    memoryview_slice_source[0:3]
)

memoryview_slice_second: memoryview = (
    memoryview_slice_source[2:6]
)

print(f"Source: {memoryview_slice_source!r}")
print(f"First:  {memoryview_slice_first!r}")
print(f"Second: {memoryview_slice_second!r}")


# A memoryview slice produces another memoryview.


# =============================================================================
# 10. Iteration
# =============================================================================

memoryview_iteration_source: memoryview = memoryview(
    b"ABC"
)

for memoryview_iteration_item in memoryview_iteration_source:
    print(memoryview_iteration_item)


# Iteration over a byte-oriented memoryview produces integers.


# =============================================================================
# 11. Membership Testing
# =============================================================================

memoryview_membership_source: memoryview = memoryview(
    b"Python"
)

print(
    80 in memoryview_membership_source
)

print(
    b"Python" in memoryview_membership_source
)


# =============================================================================
# 12. Underlying Object
# =============================================================================

memoryview_underlying_source: bytearray = bytearray(
    b"Python"
)

memoryview_underlying_view: memoryview = memoryview(
    memoryview_underlying_source
)

print(
    f"Underlying object: "
    f"{memoryview_underlying_view.obj!r}"
)


# `.obj` identifies the object exporting the underlying buffer.


# =============================================================================
# 13. View Object vs Underlying Object
# =============================================================================

memoryview_identity_source: bytearray = bytearray(
    b"Python"
)

memoryview_identity_view: memoryview = memoryview(
    memoryview_identity_source
)

print(
    f"View id:   {id(memoryview_identity_view)}"
)

print(
    f"Source id: {id(memoryview_identity_source)}"
)

print(
    f"Underlying id: {id(memoryview_identity_view.obj)}"
)

print(
    memoryview_identity_view.obj
    is memoryview_identity_source
)


# The memoryview and bytearray are different objects.
#
# The memoryview's `.obj` refers to the original bytearray.


# =============================================================================
# 14. Writable Memoryview
# =============================================================================

memoryview_writable_source: bytearray = bytearray(
    b"Python"
)

memoryview_writable_view: memoryview = memoryview(
    memoryview_writable_source
)

print(
    f"Before: {memoryview_writable_source!r}"
)

memoryview_writable_view[0] = 74

print(
    f"After:  {memoryview_writable_source!r}"
)


# 74 is ASCII "J".
#
# The memoryview modified the underlying bytearray.


# =============================================================================
# 15. Modification Through Underlying Object
# =============================================================================

memoryview_shared_buffer: bytearray = bytearray(
    b"ABC"
)

memoryview_shared_reference: memoryview = memoryview(
    memoryview_shared_buffer
)

memoryview_shared_buffer[0] = 90

print(
    f"Buffer: {memoryview_shared_buffer!r}"
)

print(
    f"View:   {memoryview_shared_reference!r}"
)


# Changes made to the underlying buffer are visible through the view.


# =============================================================================
# 16. Read-Only Memoryview
# =============================================================================

memoryview_readonly_source: bytes = b"Python"

memoryview_readonly_view: memoryview = memoryview(
    memoryview_readonly_source
)

print(
    f"Read-only: "
    f"{memoryview_readonly_view.readonly}"
)


# bytes is immutable, therefore the resulting memoryview is read-only.


# =============================================================================
# 17. Writable Status
# =============================================================================

memoryview_writable_status_source: bytearray = (
    bytearray(b"Python")
)

memoryview_writable_status_view: memoryview = (
    memoryview(memoryview_writable_status_source)
)

print(
    f"Read-only: "
    f"{memoryview_writable_status_view.readonly}"
)


# bytearray is mutable, therefore its memoryview is writable.


# =============================================================================
# 18. format
# =============================================================================

memoryview_format_example: memoryview = memoryview(
    bytearray(b"ABC")
)

print(
    f"Format: "
    f"{memoryview_format_example.format!r}"
)


# For a normal byte-oriented memoryview, the format is usually "B".


# =============================================================================
# 19. itemsize
# =============================================================================

memoryview_itemsize_example: memoryview = memoryview(
    bytearray(b"ABC")
)

print(
    f"Item size: "
    f"{memoryview_itemsize_example.itemsize}"
)


# itemsize represents the size of each element in bytes.


# =============================================================================
# 20. ndim
# =============================================================================

memoryview_ndim_example: memoryview = memoryview(
    bytearray(b"ABC")
)

print(
    f"Dimensions: "
    f"{memoryview_ndim_example.ndim}"
)


# A normal bytearray view is one-dimensional.


# =============================================================================
# 21. shape
# =============================================================================

memoryview_shape_example: memoryview = memoryview(
    bytearray(b"ABC")
)

print(
    f"Shape: "
    f"{memoryview_shape_example.shape}"
)


# =============================================================================
# 22. strides
# =============================================================================

memoryview_strides_example: memoryview = memoryview(
    bytearray(b"ABC")
)

print(
    f"Strides: "
    f"{memoryview_strides_example.strides}"
)


# strides describe how memory is traversed between elements.


# =============================================================================
# 23. nbytes
# =============================================================================

memoryview_nbytes_example: memoryview = memoryview(
    bytearray(b"Python")
)

print(
    f"Number of bytes: "
    f"{memoryview_nbytes_example.nbytes}"
)


# =============================================================================
# 24. tolist()
# =============================================================================

memoryview_tolist_example: memoryview = memoryview(
    b"ABC"
)

memoryview_tolist_output: list[int] = (
    memoryview_tolist_example.tolist()
)

print(
    f"View: {memoryview_tolist_example!r}"
)

print(
    f"List: {memoryview_tolist_output}"
)


# =============================================================================
# 25. Convert to bytes
# =============================================================================

memoryview_bytes_conversion_source: memoryview = (
    memoryview(bytearray(b"Python"))
)

memoryview_bytes_conversion_result: bytes = bytes(
    memoryview_bytes_conversion_source
)

print(
    f"View:  "
    f"{memoryview_bytes_conversion_source!r}"
)

print(
    f"Bytes: "
    f"{memoryview_bytes_conversion_result!r}"
)


# bytes() creates an independent immutable bytes object.


# =============================================================================
# 26. Convert to bytearray
# =============================================================================

memoryview_bytearray_conversion_source: memoryview = (
    memoryview(b"Python")
)

memoryview_bytearray_conversion_result: bytearray = (
    bytearray(memoryview_bytearray_conversion_source)
)

print(
    f"View:       "
    f"{memoryview_bytearray_conversion_source!r}"
)

print(
    f"Bytearray:  "
    f"{memoryview_bytearray_conversion_result!r}"
)


# bytearray() creates an independent mutable bytearray.


# =============================================================================
# 27. hex()
# =============================================================================

memoryview_hex_example: memoryview = memoryview(
    b"ABC"
)

print(
    f"Memoryview: "
    f"{memoryview_hex_example!r}"
)

print(
    f"Hex: "
    f"{memoryview_hex_example.hex()!r}"
)


# =============================================================================
# 28. Memoryview Slice and Shared Buffer
# =============================================================================

memoryview_slice_buffer: bytearray = bytearray(
    b"Python"
)

memoryview_slice_parent: memoryview = memoryview(
    memoryview_slice_buffer
)

memoryview_slice_child: memoryview = (
    memoryview_slice_parent[0:3]
)

print(
    f"Buffer: "
    f"{memoryview_slice_buffer!r}"
)

print(
    f"Parent view: "
    f"{memoryview_slice_parent!r}"
)

print(
    f"Child view: "
    f"{memoryview_slice_child!r}"
)

memoryview_slice_child[0] = 74

print(
    f"Modified buffer: "
    f"{memoryview_slice_buffer!r}"
)


# The child view accesses the same underlying buffer.


# =============================================================================
# 29. Multiple Views of One Buffer
# =============================================================================

memoryview_multiple_view_buffer: bytearray = (
    bytearray(b"ABC")
)

memoryview_multiple_view_left: memoryview = (
    memoryview(memoryview_multiple_view_buffer)
)

memoryview_multiple_view_right: memoryview = (
    memoryview(memoryview_multiple_view_buffer)
)

memoryview_multiple_view_left[0] = 90

print(
    f"Buffer: "
    f"{memoryview_multiple_view_buffer!r}"
)

print(
    f"Left view:  "
    f"{memoryview_multiple_view_left!r}"
)

print(
    f"Right view: "
    f"{memoryview_multiple_view_right!r}"
)


# Both views observe the same underlying memory.


# =============================================================================
# 30. release()
# =============================================================================

memoryview_release_buffer: bytearray = bytearray(
    b"Python"
)

memoryview_release_example: memoryview = memoryview(
    memoryview_release_buffer
)

print(
    f"Before release: "
    f"{memoryview_release_example!r}"
)

memoryview_release_example.release()

# After release(), the view can no longer access the underlying buffer.
#
# Operations such as:
#
#     memoryview_release_example[0]
#
# are invalid.


# =============================================================================
# 31. Equality
# =============================================================================

memoryview_equality_first: memoryview = memoryview(
    b"Python"
)

memoryview_equality_second: memoryview = memoryview(
    b"Python"
)

print(
    f"Equal values: "
    f"{memoryview_equality_first == memoryview_equality_second}"
)


# `==` checks represented values.


# =============================================================================
# 32. Identity
# =============================================================================

memoryview_identity_buffer: bytearray = bytearray(
    b"Python"
)

memoryview_identity_left: memoryview = memoryview(
    memoryview_identity_buffer
)

memoryview_identity_right: memoryview = memoryview(
    memoryview_identity_buffer
)

print(
    f"Same view object: "
    f"{memoryview_identity_left is memoryview_identity_right}"
)


# They are two different memoryview objects.


# =============================================================================
# 33. Same Underlying Object
# =============================================================================

memoryview_shared_identity_buffer: bytearray = (
    bytearray(b"Python")
)

memoryview_shared_identity_view: memoryview = (
    memoryview(memoryview_shared_identity_buffer)
)

print(
    f"Same underlying object: "
    f"{memoryview_shared_identity_view.obj is memoryview_shared_identity_buffer}"
)


# This is different from:
#
#     memoryview_shared_identity_view
#     is
#     memoryview_shared_identity_buffer
#
# The first checks the underlying object.
# The second checks the memoryview object itself.


# =============================================================================
# 34. Read-Only Memoryview Hashability
# =============================================================================

memoryview_hash_source: bytes = b"Python"

memoryview_hash_example: memoryview = memoryview(
    memoryview_hash_source
)

print(
    f"Read-only: "
    f"{memoryview_hash_example.readonly}"
)

print(
    f"Hash: "
    f"{hash(memoryview_hash_example)}"
)


# A read-only byte-format memoryview can be hashable.


# =============================================================================
# 35. Writable Memoryview Hashability
# =============================================================================

memoryview_unhashable_source: bytearray = (
    bytearray(b"Python")
)

memoryview_unhashable_example: memoryview = (
    memoryview(memoryview_unhashable_source)
)

print(
    f"Read-only: "
    f"{memoryview_unhashable_example.readonly}"
)

# The following is invalid:
#
#     hash(memoryview_unhashable_example)
#
# A writable memoryview is unhashable.


# =============================================================================
# 36. bytes vs bytearray vs memoryview
# =============================================================================

memoryview_comparison_immutable: bytes = b"Python"

memoryview_comparison_mutable: bytearray = (
    bytearray(b"Python")
)

memoryview_comparison_view: memoryview = (
    memoryview(memoryview_comparison_mutable)
)

print(
    f"bytes:      "
    f"{memoryview_comparison_immutable!r}"
)

print(
    f"bytearray:  "
    f"{memoryview_comparison_mutable!r}"
)

print(
    f"memoryview: "
    f"{memoryview_comparison_view!r}"
)


"""
Conceptual difference:

    bytes
        Owns immutable binary data.

    bytearray
        Owns mutable binary data.

    memoryview
        Views existing buffer data.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `memoryview` is a view over an existing buffer.

✓ It does not behave like an independent copy of the underlying data.

✓ Common buffer providers include:
      bytes
      bytearray
      array.array
      other buffer-compatible objects

✓ `memoryview()` creates the view.

✓ `memoryview(b"")` creates an empty view.

✓ A type annotation alone does not initialize a memoryview.

✓ `type()` identifies the concrete type.

✓ `isinstance()` performs runtime type checking.

✓ `len()` gives the number of visible elements.

✓ Memoryviews support:
      indexing
      negative indexing
      slicing
      iteration
      membership testing

✓ Byte-oriented indexing returns integers.

✓ A memoryview slice creates another memoryview.

✓ `.obj` identifies the underlying buffer object.

✓ `id(view)` and `id(view.obj)` refer to different objects.

✓ A memoryview over bytes is read-only.

✓ A memoryview over bytearray is writable.

✓ A writable memoryview can modify its underlying bytearray.

✓ Changes made directly to the underlying bytearray are visible through
  the memoryview.

✓ Multiple memoryviews can reference the same underlying buffer.

✓ `.readonly` reports whether the view is read-only.

✓ `.format` describes the element format.

✓ `.itemsize` gives the size of one element in bytes.

✓ `.ndim` gives the number of dimensions.

✓ `.shape` describes the dimensions.

✓ `.strides` describes memory movement between elements.

✓ `.nbytes` gives the total number of bytes exposed by the view.

✓ `.tolist()` converts the visible data to a normal list.

✓ `bytes(view)` creates a separate immutable bytes object.

✓ `bytearray(view)` creates a separate mutable bytearray.

✓ `.hex()` returns hexadecimal text.

✓ `.release()` releases the memoryview's access to its buffer.

✓ Read-only byte-format memoryviews can be hashable.

✓ Writable memoryviews are unhashable.

✓ `==` checks represented values.

✓ `is` checks object identity.

✓ Two memoryviews can be different objects while referring to the same
  underlying buffer.

✓ `view.obj is source` checks whether the view refers to that source object.

✓ `view is source` checks whether the view itself is the source object.

✓ `!r` is useful for clearly displaying the Python representation of
  binary objects.

Main distinction:

    bytes
        immutable owner of data

    bytearray
        mutable owner of data

    memoryview
        view over existing data
"""


# =============================================================================
# End of File
# =============================================================================