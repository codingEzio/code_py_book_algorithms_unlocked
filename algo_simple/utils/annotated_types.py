from typing import List, Callable, Optional, DefaultDict

# https://stackoverflow.com/a/39624147/6273859
Function = Callable

# https://stackoverflow.com/a/39826915/6273859
CouldBeString = Optional[str]
CouldBeInteger = Optional[int]

CountIntegerAppearTimes = DefaultDict[int, int]

StringList = List[str]
BoolList = List[bool]
IntList = List[int]

NestedIntList = List[List[int]]
