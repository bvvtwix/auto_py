from enum import Enum

class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = "Recieved status code is not equal 200"
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected"