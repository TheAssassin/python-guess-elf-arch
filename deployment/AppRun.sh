#! /bin/bash

this_dir="$(dirname "$0")"

exec "$this_dir"/usr/bin/python -m guess_elf_arch "$@"
