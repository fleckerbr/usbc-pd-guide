from __future__ import annotations

import re
import textwrap
from collections.abc import Generator, Iterable, Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, Self, Union, overload

import yaml

from usb.subtypes import Hex

if TYPE_CHECKING:
    from _typeshed import SupportsRead

    StructuredText = Union[str, None, "StructuredTextList", "StructuredTextDict"]
    StructuredTextList = Sequence[StructuredText]
    StructuredTextDict = Mapping[str, StructuredText]


class Bits(tuple[int]):
    @overload
    def __new__(cls, bit: int, /) -> Self: ...
    @overload
    def __new__(cls, max_bit: int, min_bit: int, /) -> Self: ...
    def __new__(cls, *bits: int) -> Self:
        if (_bitlen := len(bits)) not in (1, 2):
            raise ValueError(f"Expected 1 or 2 bit values, received {_bitlen}")
        elif _bitlen == 2 and bits[0] <= bits[1]:
            raise ValueError("The maximum bit value must be greater than the minimum")
        return super().__new__(cls, bits)

    def __str__(self) -> str:
        if len(self) == 1:
            return f"B{self[0]}"
        return f"B{self[0]}..{self[1]}"


def register_fields() -> list[Register.Field]:
    """Helper function for type-checking."""
    return []


@dataclass(slots=True)
class Register:
    name: str
    address: Hex
    bytes: int
    details: str
    permissions: Register.Permissions | None = None
    reset_value: Hex | Literal["Vendor Defined", "..."] | None = None
    registers: Registers | None = None
    fields: list[Register.Field] = field(default_factory=register_fields)

    @dataclass(slots=True)
    class Permissions:
        read: bool
        write: bool

    @dataclass(slots=True)
    class Field:
        bits: Bits
        name: str = "Reserved"
        reserved: bool = True
        required: bool = True
        identifier: str = "Reserved"
        details: StructuredText = None

        def __post_init__(self) -> None:
            if isinstance(self.bits, str):
                bits = (int(bit) for bit in self.bits.removeprefix("B").split(".."))
                self.bits = Bits(*bits)
            if self.identifier == "<auto>":
                self.identifier = re.sub(r"[ _-]+", "", self.name)

        @property
        def link(self) -> str:
            return re.sub(r"[^\w-]", "", re.sub(r"[ \\/_-]+", "-", self.name.lower()))

    def _format_text(self, text: StructuredText) -> str:
        SEPARATOR = ":material-arrow-right-thin:"

        match text:
            case str():
                return text
            case None:
                return ""
            case Sequence():
                if all(isinstance(part, list) for part in text):
                    return "\n\n***\n\n".join(self._format_text(_st) for _st in text)
                else:
                    return "\n\n".join(self._format_text(_st) for _st in text)
            case Mapping():
                definition_lists: list[str] = []
                for key, value in text.items():
                    details = self._format_text(value).split("\n\n", 1)
                    if len(details) < 2:
                        details.append("")
                    header, body = details
                    header = f"`{key}` {SEPARATOR} {header}" if any(header) else f"`{key}`"
                    if any(body):
                        body = f"\n\n:{textwrap.indent(body, '    ')[1:]}"
                    definition_lists.append(f"{header}{body}")
                return "\n\n".join(definition_lists)

    def summary_table(self) -> str:
        columns: tuple[list[str], list[str], list[str], list[str]] = (["Address"], ["Register Name"], ["IO Access"], ["Reset Value"])  # fmt: skip
        widths: tuple[int, int, int, int] = (17, 17, 13, 13)

        address = f"`{self.address}`"
        if self.bytes == 2:
            address = f"{address}..`{self.address + 1}`"
        columns[0].append(address)
        if (width_0 := len(address)) > widths[0]:
            widths = width_0, widths[1], widths[2], widths[3]

        columns[1].append(name := f"[{self.name}]")
        if (width_1 := len(name)) > widths[1]:
            widths = widths[0], width_1, widths[2], widths[3]

        if self.permissions is not None:
            columns[2].append(access := f"{'`Read`'*self.permissions.read}/{'`Write`'*self.permissions.write}".strip("/"))  # fmt: skip
            if (width_2 := len(access)) > widths[2]:
                widths = widths[0], widths[1], width_2, widths[3]
        else:
            columns[2].append("-")

        reset_value = "" if self.reset_value is None else f"`{self.reset_value}`"
        columns[3].append(reset_value)
        if (width_3 := len(reset_value)) > widths[3]:
            widths = widths[0], widths[1], widths[2], width_3

        width_0, width_1, width_2, width_3 = ((width // 4 + 1) * 4 + 1 for width in widths)
        table: list[str] = [
            f"| {c0:<{width_0}} | {c1:<{width_1}} | {c2:<{width_2}} | {c3:<{width_3}} |"
            for c0, c1, c2, c3 in zip(columns[0], columns[1], columns[2], columns[3])
        ]
        table.insert(1, f"| :{'-'*(width_0-2)}: | :{'-'*(width_1-2)}: | :{'-'*(width_2-2)}: | :{'-'*(width_3-2)}: |")  # fmt: skip
        return "\n".join(table)

    def fields_table(self) -> str:
        columns: tuple[list[str], list[str], list[str]] = (["Bit(s)"], ["Name"], ["Identifier"])
        widths: tuple[int, int, int] = (9, 37, 37)
        for _field in self.fields:
            columns[0].append(bits := f"`{_field.bits}`")
            if (width_0 := len(bits)) > widths[0]:
                widths = width_0, widths[1], widths[2]

            columns[1].append(name := _field.name)
            if (width_1 := len(name)) > widths[1]:
                widths = widths[0], width_1, widths[2]

            identifier = "" if _field.reserved else f"[{self.name}.{_field.identifier}]"
            columns[2].append(identifier)
            if (width_2 := len(identifier)) > widths[2]:
                widths = widths[0], widths[1], width_2

        width_0, width_1, width_2 = ((width // 4 + 1) * 4 + 1 for width in widths)
        table: list[str] = [
            f"| {c0:<{width_0}} | {c1:<{width_1}} | {c2:<{width_2}} |"
            for c0, c1, c2 in zip(columns[0], columns[1], columns[2])
        ]
        table.insert(1, f"| {'-' * width_0} | {'-' * width_1} | {'-' * width_2} |")
        return "\n".join(table)

    def markdown_page(self) -> str:
        def format_page(register: Register, header_prefix: str = "") -> str:
            output: list[str] = []
            output.append(f"{header_prefix}# {register.name}")
            output.append("")
            output.append(register.summary_table())
            output.append("")
            output.append(f"{header_prefix}## Description")
            output.append("")
            output.append(register.details)

            if register.registers is not None:
                output.append("***")
                output.append("")

                for _register in register.registers:
                    output.append(format_page(_register, header_prefix + "#"))
                    output.append("***")
                    output.append("")

            else:
                output.append(f"{header_prefix}## Register Fields")
                output.append("")
                output.append(register.fields_table())
                output.append("")

                for _field in register.fields:
                    if _field.reserved:
                        continue

                    admonition = "success" if _field.required else "warning"
                    requirement = "(Required)" if _field.required else "(Optional)"
                    field_name = _field.name.replace("*", "\\*")
                    field_name_toc = _field.name.replace('"', '\\"')

                    output.append(f"{header_prefix}### `{_field.bits}` {field_name} {{ #{_field.link} data-toc-label=\"{field_name_toc}\" }}")  # fmt: skip
                    output.append("")
                    output.append(f'!!! {admonition} "{register.name}.{_field.identifier} {requirement}"')  # fmt: skip
                    output.append(textwrap.indent(register._format_text(_field.details), "    ").rstrip())  # fmt: skip
                    output.append("")

            return "\n".join(output).rstrip() + "\n"

        return format_page(self)


class Registers:
    def __init__(self, __iter: Iterable[Register]) -> None:
        self.__items = {register.name: register for register in __iter}

    @classmethod
    def load(cls, fp: SupportsRead[str]) -> Self:
        def get_registers(data: dict[str, Any]) -> list[Register]:
            registers: list[Register] = []
            for name, data in data.items():
                if data.get("registers", None) is None:
                    _fields: list[dict[str, Any]] = data.get("fields", [])
                    register = Register(
                        name=name,
                        address=Hex(data["address"], 2),
                        bytes=data["bytes"],
                        details=data["details"],
                        permissions=Register.Permissions(
                            read=data["permissions"]["read"],
                            write=data["permissions"]["write"],
                        ),
                        reset_value=_reset
                        if (_reset := data["reset-value"]) in ("Vendor Defined", "...", None)
                        else Hex(_reset, length=data["bytes"] * 2),
                        fields=[
                            Register.Field(bits=field["bit(s)"])
                            if field.get("reserved", False)
                            else Register.Field(
                                bits=field["bit(s)"],
                                name=field["name"],
                                reserved=False,
                                required=field.get("required", True),
                                identifier=field.get("identifier", "<auto>"),
                                details=field["details"],
                            )
                            for field in _fields
                        ],
                    )
                else:
                    register = Register(
                        name=name,
                        address=Hex(data["address"], 2),
                        bytes=data["bytes"],
                        details=data["details"],
                        registers=cls(get_registers(data["registers"])),
                    )
                registers.append(register)
            return registers

        return cls(get_registers(yaml.safe_load(fp)))

    def __getitem__(self, __key: str) -> Register:
        return self.__items[__key]

    def __iter__(self) -> Generator[Register, None, None]:
        yield from self.__items.values()

    def hyperlinks(self, prefix: Path | None = None) -> str:
        def get_hyperlinks(register: Register, prefix: Path, override_file: str | None) -> str:
            output: list[str] = []

            if override_file is None:
                override_file = register.name.lower().replace("_", "-")
            path = f"/{(prefix / override_file).as_posix()}/"

            output.append(f"<!-- {register.address} -- {register.name} Register -->")
            output.append(f"[{register.name}]: {path}#{register.name.lower()}")
            for _field in register.fields:
                if _field.reserved:
                    continue
                output.append(f"[{register.name}.{_field.identifier}]: {path}#{_field.link}")
            output.append("")

            if register.registers is not None:
                for register in register.registers:
                    output.append(get_hyperlinks(register, prefix, override_file))

            return "\n".join(output)

        return "\n".join(get_hyperlinks(register, prefix or Path(), None) for register in self)


if __name__ == "__main__":
    with open("src/usbc/data/registers.yaml") as file:
        registers = Registers.load(file)

    FIELD_TEMPLATE = textwrap.dedent(
        """
        {name} = Field(
            bits=B({bits}),
            alias="{alias}",
            identifier="{identifier}",
            reset={reset},
            required={required},
        )
        """
    )[1:-1]
    REGISTER_TEMPLATE = textwrap.dedent(
        """
        from __future__ import annotations

        from usbc.port_controller import B, Field, Register


        class {classname}(Register):
            __address__ = {address}
            __alias__ = "{alias}"
            __identifier__ = "{identifier}"
            __readable__ = {readable}
            __writable__ = {writable}

        {fields}
        """
    )[1:-1]

    def camel_to_snake(name: str) -> str:
        name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).upper()

    def fields_string(fields: list[Register.Field]) -> str:
        return "\n".join(
            FIELD_TEMPLATE.format(
                name=camel_to_snake(field.identifier),
                bits=f"{_bits[0]}, {_bits[1]}"
                if (len(_bits := tuple(field.bits)) == 2)
                else f"{_bits[0]}",
                alias=field.name,
                identifier=field.identifier,
                reset="0b0"
                if len(_bits := tuple(field.bits)) == 1
                else f"0b{'0' * (_bits[0] - _bits[1] + 1)}",
                required=field.required,
            )
            for field in fields
        )

        # return "\n".join(
        #     textwrap.dedent(
        #         f"""
        #         ["{field.identifier}{f'.{field.bits}' if field.reserved else ''}"] {{
        #           bits = "{field.bits}"
        #           name = "{field.name}"
        #           required = {str(field.required).lower()}
        #         }}
        #         """
        #     )[1:-1]
        #     for field in fields
        # )

    REGISTERS_PATH = Path.cwd() / "src" / "usbc" / "port_controller" / "registers"
    for register_name in (_r.name for _r in registers):
        register = registers[register_name]
        register_file = register_name.lower().replace("_", "-")
        with REGISTERS_PATH.joinpath(f"{register_file}.py").open("w") as file:
            file.write(
                REGISTER_TEMPLATE.format(
                    classname="".join(word.title() for word in register.name.split("_")),
                    address=str(register.address),
                    alias=" ".join(word.title() for word in register.name.split("_")),
                    identifier=register.name,
                    readable=str((register.permissions or Register.Permissions(True, True)).read),
                    writable=str((register.permissions or Register.Permissions(True, True)).write),
                    fields=textwrap.indent(fields_string(register.fields), "    "),
                )
            )

            # file.write(
            #     textwrap.dedent(
            #         f"""
            #         amends "../Register.pkl"

            #         address = {register.address}
            #         size = {register.bytes}.b
            #         readable = {str((register.permissions or Register.Permissions(True, True)).read).lower()}
            #         writable = {str((register.permissions or Register.Permissions(True, True)).write).lower()}
            #         resetValue = {str(register.reset_value).replace("None", "null").replace("Vendor Defined", '"Vendor Defined"').replace("...", '"Vendor Defined"')}
            #         fields {{
            #         {"  "+textwrap.indent(fields_string(register.fields), "                      ").strip()}
            #         }}
            #         """[1:-1]
            #     )
            # )
