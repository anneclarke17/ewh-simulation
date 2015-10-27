import enum

class State(enum.Enum):
    OFF = 0
    ON = 1

    def __str__(self):
        return self.name

class PowerUsage(enum.Enum):
    LOW = 0
    REGULAR = 1
