"""__main__."""
import os
from smatrix.data_model import DataModel
from smatrix.view import View
from smatrix.controller import Controller

import logzero
from logzero import logger

# env variable (if set) has precedence
_ = 10
logzero.loglevel(level=10 if os.getenv("DEBUG") else 0 or _)


def main():
    """Run main."""
    logger.debug(" debug ")
    logger.info(" info ")
    m = DataModel()
    v = View()
    c = Controller(m, v)


if __name__ == "__main__":
    main()
