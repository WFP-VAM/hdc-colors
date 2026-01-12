"""Custom types for hdc-colors."""

ColorRampElement = dict[str, int | float | str]
SomeNumber = int | float
RampInput2 = list[tuple[SomeNumber, str]]
RampInput3 = list[tuple[SomeNumber, str, str]]
RampInput = RampInput2 | RampInput3
RGBTuple = tuple[SomeNumber, SomeNumber, SomeNumber]
RGBATuple = tuple[SomeNumber, SomeNumber, SomeNumber, SomeNumber]
NodataType = int | float
