from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from enum import Enum, EnumMeta, StrEnum
from functools import reduce
from operator import ior
from typing import Any, Literal, LiteralString, Never, NoReturn, Self, cast, overload

type Bit = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


class B[H: Bit, L: Bit]:
    @overload
    def __init__(self, bit: H | L, /) -> None: ...
    @overload
    def __init__(self, bit_high: H, bit_low: L, /) -> None: ...
    def __init__(self, *args: H | L) -> None:
        if (nargs := len(args)) > 2:
            raise ValueError(f"B.__init__() takes 2 positional arguments but {nargs} were given")
        elif any(0 > n > 15 for n in args):
            raise ValueError("Expected bits to be in range 0-15")

        self.__high = cast(H, args[0])
        self.__low = cast(L, self.__high if len(args) == 1 else args[1])

        if self.__high < self.__low:
            raise ValueError("Expected high bit to be provided first")
        elif self.__high == self.__low and len(args) == 2:
            raise ValueError("When two bits are provided, they must not be the same")

    @property
    def high(self) -> H:
        return self.__high

    @property
    def low(self) -> L:
        return self.__low

    def __str__(self) -> str:
        return f"B{self.high}" if self.high == self.low else f"B{self.high}..{self.low}"

    def __repr__(self) -> str:
        return f"B({self.high})" if self.high == self.low else f"B({self.high}, {self.low})"


class EnumAttribute[T, M]:
    def __init__(self, member_attribute: M = True) -> None:
        self.member_attribute = member_attribute

    def __set_name__(self, owner: Any, name: str) -> None:
        del owner  # Dereference unused variables
        self.value_attribute = name
        self.enum_attribute = f"__{name}__"

    def __set__(self, obj: Any, value: Never) -> NoReturn:
        del obj, value  # Dereference unused variables
        attribute = self.value_attribute
        raise AttributeError(f"can't set attribute '{attribute}'")

    @overload
    def __get__(self: EnumAttribute[T, Literal[True]], obj: Any, objtype: Any) -> T: ...
    @overload
    def __get__(self: EnumAttribute[T, Literal[False]], obj: None, objtype: Any) -> T: ...
    @overload
    def __get__(self: EnumAttribute[T, Literal[False]], obj: Any, objtype: Any) -> None: ...
    def __get__(self, obj: Any, objtype: Any) -> T | None:
        if obj is None:
            return getattr(objtype, self.enum_attribute)
        elif self.member_attribute:
            return getattr(obj.value, self.value_attribute)
        else:
            return None


class RegisterMeta(EnumMeta):
    def __str__(self) -> str:
        return cast(Register, self).identifier

    # TODO: Implement way to filter out Reserved fields
    def __iter__(self) -> Iterator[Field]:
        return cast(Iterator[Field], super().__iter__())

        # NOTE: Dropping reserved fields this way results in missing data when computing __bits__
        # return itertools.dropwhile(
        #     lambda field: "Reserved" in field.alias,
        #     cast(Iterator[Field], super().__iter__()),
        # )


class Register(Enum, metaclass=RegisterMeta):
    address = EnumAttribute[int, Literal[False]](member_attribute=False)
    bits = EnumAttribute[B[Bit, Bit], Literal[True]]()
    alias = EnumAttribute[LiteralString, Literal[True]]()
    identifier = EnumAttribute[LiteralString, Literal[True]]()
    parent = EnumAttribute[int, Literal[False]](member_attribute=False)
    readable = EnumAttribute[bool, Literal[False]](member_attribute=False)
    writable = EnumAttribute[bool, Literal[False]](member_attribute=False)
    reset = EnumAttribute[int, Literal[True]]()

    __address__: int
    __alias__: LiteralString
    __identifier__: LiteralString
    __parent__: Register | None
    __readable__: bool
    __writable__: bool

    def __new__(cls, value: Field) -> Self:
        value.identifier = f"{cls.identifier}.{value.identifier}"

        obj = object.__new__(cls)
        obj._value_ = value

        return obj

    def __init_subclass__(cls) -> None:
        attributes = ("__address__", "__alias__", "__identifier__", "__readable__", "__writable__")
        for attribute in attributes:
            if not hasattr(cls, attribute):
                raise AttributeError(f"'{cls.__name__}' class is missing attribute '{attribute}'")
        if not hasattr(cls, "__parent__"):
            cls.__parent__ = None

        def get_reset() -> int | Reset:
            fields = [field for field in cls]
            if all(isinstance(field.reset, int) for field in fields):
                return reduce(ior, (cast(int, field.reset) << field.bits.low for field in fields))

            reset: Reset | None = None
            illegal_field_reset: Field | None = None
            for field in fields:
                match field.reset, reset:
                    case int(), _:
                        # Track whether a non-reserved field has defined an integer reset value.
                        # This would be an illegal definition since special reset types should
                        # apply to all non-reserved fields.
                        if field.alias != "Reserved":
                            illegal_field_reset = field
                    case field_reset, None:
                        reset = field_reset
                    case field_reset, reset:
                        if reset != field_reset:
                            raise ValueError(
                                "Incompatible register field reset types: "
                                f"'{reset}' and '{field_reset}'"
                            )
            assert reset is not None

            if illegal_field_reset is not None:
                identifier = illegal_field_reset.identifier
                raise ValueError(
                    f"Non-Reserved field '{identifier}' cannot define an integer reset value "
                    f"when a register includes a special reset type: '{reset}'"
                )
            return reset

        cls.__bits__ = B(max(field.bits.high for field in cls), 0)  # type: ignore
        cls.__reset__ = get_reset()  # type: ignore

        return super().__init_subclass__()

    def __str__(self) -> str:
        return self._value_.__str__()

    @classmethod
    def subclasses(cls) -> list[type[Self]]:
        return cls.__subclasses__()


@dataclass
class Field:
    bits: B[Bit, Bit]
    alias: LiteralString | Literal["Reserved"]
    identifier: LiteralString
    reset: int | Reset
    required: bool

    def __str__(self) -> LiteralString:
        return self.identifier


class Reset(StrEnum):
    UNDEFINED = "Undefined"
    CAPABILITY_DEFINED = "Capability Defined"
    VENDOR_DEFINED = "Vendor Defined"
