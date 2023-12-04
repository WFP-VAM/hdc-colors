"""Custom types for hdc-colors"""
from typing import Dict, List, Tuple, Union

ColorRampElement = Dict[str, Union[Union[int, float], str]]
SomeNumber = Union[int, float]
RampInput2 = List[Tuple[SomeNumber, str]]
RampInput3 = List[Tuple[SomeNumber, str, str]]
RampInput = Union[RampInput2, RampInput3]
RGBTuple = Tuple[SomeNumber, SomeNumber, SomeNumber]
RGBATuple = Tuple[SomeNumber, SomeNumber, SomeNumber, SomeNumber]
NodataType = Union[int, float]
