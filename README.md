# python-guess-elf-arch

This little Python tool uses [cppyy](https://cppyy.readthedocs.io/en/latest/)
(which by itself uses [Cling](https://github.com/vgvassilev/cling), the C++
interpreter) to dynamically interpret the system's
[`elf.h`](https://github.com/torvalds/linux/blob/master/include/linux/elf.h).
It reads an ELF binary's `e_machine` header field and converts it to an
AppImage-style architecture name.

AppImage does not use any "standardized" scheme (unlike, for instance, Debian,
the Linux kernel), but uses a mix of them.

Currently supported architectures:

- `i686`
- `x86_64`
- `armhf`
- `aarch64`
