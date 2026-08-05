"Strings are immutable, "
"so their contents cannot be changed in place after creation. "
"String methods return new strings or other new objects instead."


# Below is a demo of creating a string type data type.

random_string: str = "" # Default value [whose bool(var_name) is False always]
random_string_2: str = "non-default" # Non-Defualt value [whose bool(var_name) is True always]

print(bool(random_string), bool(random_string_2))

# Dir function lets you know the applicable functions for that dtype.

print(dir(str))
"""
[ 'capitalize', 'casefold', 'center',
    'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
      'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
        'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
          'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
            'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
              'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
                'splitlines', 'startswith', 'strip', 'swapcase', 'title',
                  'translate', 'upper', 'zfill']"""

random_string_3: str = random_string_2.strip('t')
print(random_string_3)

# 2886770282480 2886770287920 -> both strings have different id's, not same object.
print(id(random_string_2), id(random_string_3))