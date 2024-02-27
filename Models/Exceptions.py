class BinOptimizationError(Exception):
    """
    Base class for handling bin-ranging exceptions. Inherits from Exception class.
    """
    def __init__(self, *args):
        if args:
            self._message = args[0]
        else:
            self._message = None

    def __str__(self):
        if self._message:
            return f'{self.__class__.__name__}: {self._message}'
        else:
            return f'{self.__class__.__name__} called'


class LowerBoundGreaterThanUpperBoundError(BinOptimizationError):
    """
    Raised when the lower bound provided for the bin is greater than the upper bound provided for the bin.
    """
    def __init__(self, *args):
        super().__init__(*args)


class IncorrectBinDataType(BinOptimizationError):
    """
    Raised when an action is tried on an exhausted set of items.
    """
    def __init__(self, *args):
        super().__init__(*args)
        
class PanLengthError(BinOptimizationError):
    """
    Raised when an invalid pan length is passed.
    """
    def __init__(self, *args):
        super().__init__(*args)