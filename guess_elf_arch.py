#! /usr/bin/env python3

import click
import cppyy
import pathlib
import sys


cppyy.include("elf.h")

cppyy.cppdef(
    """
Elf64_Ehdr* get_ehdr(char* data) {
    return static_cast<Elf64_Ehdr*>(static_cast<void*>(data));
}
"""
)


# these names are used by appimagetool by default (look at AppImageKit's release page)
ArchsToEmNames = {
    "i686": "386",
    "x86_64": "X86_64",
    "armhf": "ARM",
    "aarch64": "AARCH64",
}


for arch, em_name in ArchsToEmNames.items():
    code = f"static constexpr int ARCH_{arch} = EM_{em_name};"
    cppyy.cppdef(code)


def get_e_machine_id(em_name: str):
    return getattr(cppyy.gbl, f"ARCH_{em_name}")


EmIdsToArchs = {get_e_machine_id(em_name): em_name for em_name in ArchsToEmNames.keys()}


def get_elf64_ehdr(filename: str):
    with open(filename, "rb") as f:
        data = f.read(cppyy.sizeof("Elf64_Ehdr"))

    return cppyy.gbl.get_ehdr(data)


@click.command()
@click.argument("filename", type=click.Path())
def main(filename):
    ehdr = get_elf64_ehdr(filename)
    print(EmIdsToArchs[ehdr.e_machine])


if __name__ == "__main__":
    main()
