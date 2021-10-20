"""Controller."""
from logzero import logger


class Controller:
    def __init__(self, model=None, view=None):
        ...

        logger.debug("view.mainloop")
        view.mainloop()
