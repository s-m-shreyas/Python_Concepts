# Module Search and Resolution

This section explains **how Python finds, loads, and resolves modules during imports**.

The goal is to understand what happens behind an import statement such as:

```python
import math
import my_module
from package import module
```

Rather than treating imports as magic, this section focuses on the mechanism Python uses to locate and load modules.

## Topics Covered

### 01. Module Search Path

Understanding the locations Python searches when resolving an import.

Key concepts:

* `sys.path`
* Current execution context
* Standard library locations
* Installed packages
* Custom module locations
* `PYTHONPATH`

### 02. Module Resolution

Understanding how Python determines which module should satisfy an import.

Key concepts:

* Import names
* Search order
* Module discovery
* Package discovery
* Name conflicts
* Shadowing

### 03. `sys.path`

Understanding Python's module search path programmatically.

Key concepts:

* Inspecting `sys.path`
* Search-path order
* Adding custom paths
* Why modifying `sys.path` should generally be avoided in application code

### 04. Import Execution

Understanding what happens after Python finds a module.

Key concepts:

* Module loading
* Module execution
* Module objects
* `sys.modules`
* Import caching

### 05. Import Caching

Understanding why importing the same module multiple times does not normally execute the module repeatedly.

Key concepts:

* `sys.modules`
* Module caching
* Reusing loaded modules
* Reloading modules

### 06. Import Resolution Conflicts

Understanding common problems caused by conflicting module names.

Examples:

```text
project/
├── math.py
└── main.py
```

A local `math.py` can interfere with the expected standard-library `math` module.

This section explains:

* Module shadowing
* Naming conflicts
* Search-order effects
* How to diagnose unexpected imports

## Learning Objective

By the end of this section, you should be able to answer:

> **"When Python sees an import statement, where does it look, what does it find, and how does it decide what to load?"**

The important mental model is:

```text
import statement
       ↓
module name
       ↓
module search path
       ↓
module/package found
       ↓
module loaded
       ↓
module cached in sys.modules
```

This foundation is important before moving into more advanced package and import-system concepts.
