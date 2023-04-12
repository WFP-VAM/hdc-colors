"""Custom types for hdc-colors"""
from typing import Dict, List, Tuple, Union

ColorRampElement = Dict[str, Union[Union[int, float], str]]
RampInputTuple = Union[
    Tuple[Union[int, float], str], Tuple[Union[int, float], str, str]
]
RampInput = List[RampInputTuple]
