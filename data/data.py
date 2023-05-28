from dataclasses import dataclass

@dataclass
class Person:
    FULL_NAME: str = None
    EMAIL: str = None
    CURRENT_ADDRESS: str = None
    PERMANENT_ADDRESS: str = None
