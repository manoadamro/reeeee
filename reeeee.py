"""
>>> import reeeee

>>> reeeee.express(5) # mildly annoying
REEEEE

>>> reeeee.express(10) # quite irritating
REEEEEEEEEE

>>> reeeee.express(15) # absolutely fucking unacceptable
REEEEEEEEEEEEEEE

>>> reeeee.reeeeaise("I dun goofed.", 5)
I dun goofed. REEEEE
"""


class REEEEException(Exception):
    ...


def express(magnitude: int=5) -> str:
    magnitude = max(5, magnitude)
    return ("r" + ("e" * magnitude)).upper()


def reeeeaise(message: str, magnitude: int=5) -> str:
    raise REEEEException(f"{message} {express(magnitude)}")
