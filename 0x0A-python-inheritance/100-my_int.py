#!/usr/bin/python3

"""Define a class MyInt that inherits from int."""


class MyInt(int):
    """Inverted attributes int operators == and !=."""

    def __eq__(self, value):
        """Overrides == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value 
