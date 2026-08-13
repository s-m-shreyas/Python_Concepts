# type: ignore

"""
02_composition.py

Demonstrates composition.

Composition occurs when a class contains another class object and
uses it to provide functionality.
"""


# ============================================================
# 1. COMPOSITION EXAMPLE
# ============================================================

class Keyboard:
    """A keyboard component."""

    def type(self, text: str) -> None:
        print(f"Typing: {text}")


class Computer:
    """A computer is composed of a keyboard."""

    def __init__(self) -> None:
        self.keyboard = Keyboard()

    def write(self, text: str) -> None:
        self.keyboard.type(text)


computer = Computer()
computer.write("Hello, world!")

"""
Computer owns a Keyboard and delegates the actual task to it.
This is composition.
"""


# ============================================================
# 2. COMPOSITION WITH MULTIPLE COMPONENTS
# ============================================================

class CPU:
    """The computer's CPU."""

    def process(self) -> None:
        print("CPU is processing data.")


class Memory:
    """The computer's memory."""

    def store(self) -> None:
        print("Data stored in memory.")


class Laptop:
    """A laptop is composed of CPU and Memory."""

    def __init__(self) -> None:
        self.cpu = CPU()
        self.memory = Memory()

    def run(self) -> None:
        self.cpu.process()
        self.memory.store()


laptop = Laptop()
laptop.run()

"""
The outer object creates and uses child objects for its operations.
"""


# ============================================================
# 3. WHY COMPOSITION IS POWERFUL
# ============================================================

# - It promotes modularity.
# - Each object has a clear responsibility.
# - Components can be replaced without changing the outer design.
# - It avoids deep inheritance chains.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Composition means building a class from smaller objects.
# - The outer object owns and uses the inner objects.
# - It is a strong design choice when behavior is composed from reusable parts.
# - Composition is often easier to modify than inheritance-heavy designs.
