class Employee:
    """
    Represents an employee in the company.

    name: str
    birthday: int, a Unix timestamp
    salary: int, a yearly pre-tax dollar amount
    """

    def __init__(self: Employee, name: str, birthday: int, salary: int) -> None:
        """Initialize this Employee."""
        self.name, self.birthday, self.salary = name, birthday, salary

    def __repr__(self: Employee) -> str:
        """Return a string representation of this employee."""
        return self.name
