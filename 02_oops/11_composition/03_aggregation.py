# type: ignore

"""
03_aggregation.py

Demonstrates aggregation.

Aggregation is a looser form of composition where one object uses
another object, but the contained object still exists independently.
"""


# ============================================================
# 1. AGGREGATION EXAMPLE
# ============================================================

class Manager:
    """A manager can exist separately."""

    def __init__(self, name: str) -> None:
        self.name = name

    def supervise(self) -> None:
        print(f"{self.name} is supervising.")


class Department:
    """A department uses a manager."""

    def __init__(self, manager: Manager) -> None:
        self.manager = manager

    def run(self) -> None:
        print("Department is running.")
        self.manager.supervise()


manager = Manager("Asha")
department = Department(manager)
department.run()

"""
The manager object is passed in from outside.
The department depends on the manager, but the manager is not
created or owned by the department itself.
This is aggregation.
"""


# ============================================================
# 2. AGGREGATION IS MORE LOOSELY COUPLED
# ============================================================

class Team:
    """A team can have different members."""

    def __init__(self, members: list[str]) -> None:
        self.members = members


class Project:
    """A project aggregates a team."""

    def __init__(self, team: Team) -> None:
        self.team = team

    def show_team(self) -> None:
        print("Team members:")
        for member in self.team.members:
            print(member)


team = Team(["Riya", "Sam", "Nina"])
project = Project(team)
project.show_team()

"""
The project uses a team object, but the team has a life outside the
project as well.
"""


# ============================================================
# 3. AGGREGATION VS COMPOSITION
# ============================================================

# - Composition: outer object owns and controls the inner object.
# - Aggregation: outer object uses an object that has independent existence.
# - Aggregation is usually looser and more flexible.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Aggregation is a weaker form of object association.
# - The contained object can still exist independently.
# - It is useful when dependencies are shared rather than owned.
# - It helps model real-world relationships cleanly.
