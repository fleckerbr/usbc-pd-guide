from __future__ import annotations

import math
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, Iterable, Self, SupportsBytes, SupportsIndex, overload

from typing_extensions import Buffer, Literal

if TYPE_CHECKING:
    from _typeshed import ConvertibleToInt


class Hex(int):
    # fmt: off
    @overload
    def __new__(cls, x: ConvertibleToInt, /, length: int = ...) -> Self: ...
    @overload
    def __new__(cls, x: str | bytes | bytearray, /, length: int = ..., base: SupportsIndex = 16) -> Self: ...
    # fmt: on
    def __new__(
        cls,
        x: ConvertibleToInt | str | bytes | bytearray,
        /,
        length: int | None = None,
        base: SupportsIndex = 16,
    ) -> Self:
        match x:
            case str() | bytes() | bytearray():
                obj = super().__new__(cls, x, base=base)
                match x[:2]:
                    case str("0x") | bytes(b"0x") | bytearray(b"0x"):
                        min_required_length = len(x[2:]) * 4
                    case _:
                        min_required_length = len(hex(obj).removeprefix("0x")) * 4
            case _:
                obj = super().__new__(cls, x)
                min_required_length = super().bit_length(obj)

        # Verify that the user provided hex length can fit the provided value
        if length is not None and (length * 4) < min_required_length:
            raise OverflowError(f"int cannot be represented in {length * 4} bits")

        obj.__length = length or math.ceil(min_required_length / 4)  # type: ignore
        return obj

    @classmethod
    def from_bytes(
        cls,
        bytes: Iterable[SupportsIndex] | SupportsBytes | Buffer,
        byteorder: Literal["little", "big"] = "big",
        *,
        signed: bool = False,
        length: int | None = None,
    ) -> Self:
        value = int.from_bytes(bytes, byteorder, signed=signed)
        return cls.__new__(cls, value) if length is None else cls.__new__(cls, value, length=length)

    def bit_length(self) -> int:
        return self.__len__() * 4

    def __add__(self, value: int | Hex) -> Hex:
        return Hex(super().__add__(value), length=len(self))

    def __sub__(self, value: int | Hex) -> Hex:
        return Hex(super().__sub__(value), length=len(self))

    def __len__(self) -> int:
        return self.__length  # type: ignore

    def __str__(self) -> str:
        return f"0x{super().__format__(f'0{self.__len__()}x').upper()}"

    def __repr__(self) -> str:
        return f"Hex('{self.__str__()}')"


if __name__ == "__main__":
    constructors: list[tuple[Callable[..., Hex], dict[str, Any]]] = [
        (Hex, {"args": [bytearray(b"0x0FAA")]}),
        (Hex, {"args": [256]}),
        (Hex.from_bytes, {"args": [b"\x0f\xaa"], "kwargs": {"byteorder": "big", "length": 4}}),
    ]
    for constructor in constructors:
        value = constructor[0](*constructor[1].get("args", []), **constructor[1].get("kwargs", {}))  # type: ignore

        construct_args = ", ".join(str(arg) for arg in constructor[1].get("args", []))
        construct_kwargs = ", ".join(
            f"{kw}={arg}"
            for kw, arg in constructor[1].get("kwargs", {}).items()  # type: ignore
        )
        if any(construct_kwargs):
            construct_kwargs = f", {construct_kwargs}"
        construct_repr = f"{constructor[0].__name__}({construct_args}{construct_kwargs})"
        print(construct_repr, f"  {repr(value)=}", f"  {value=}", "", sep="\n")
