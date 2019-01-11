"""
>>> import reeeee

>>> reeeee.express(5) # mildly annoying
REEEEE

>>> reeeee.express(10) # quite irritating
REEEEEEEEEE

>>> reeeee.express(15) # absolutely fucking unacceptable
REEEEEEEEEEEEEEE

>>> reeeee.reeeeaise("something fucked up", 5)
something fucked up REEEEE
"""


class REEEEException(Exception):
    ...


def express(magnitude: int=5) -> str:
    magnitude = min(5, magnitude)
    return ("r" + ("e" * magnitude)).upper()


def reeeeaise(message: str, magnitude: int=5) -> str:
    raise REEEEException(f"{message} {express(magnitude)}")