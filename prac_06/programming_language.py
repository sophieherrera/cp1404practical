"""
CP1404 Practical
ProgrammingLanguage class
Estimated time: 30 min
actual time: 21 min
"""

class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, name, typing, reflection, year):
        """
        Create a new programming language.

        :param name: str, name of the language
        :param typing: str, typing style ( "Dynamic" or "Static")
        :param reflection: bool, supports reflection
        :param year:int, year language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ Returns True if the language is dynamic, False otherwise. """
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """ Return a string representation of the language."""
        return f" {self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
