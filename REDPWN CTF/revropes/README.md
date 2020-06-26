# revropes

## Challenge

"It's not just a string, it's a rope!"

You can download the problem files here [ropes](ropes).

## Process

The title of the challenge hints that the flag is within the strings of the elf file. Turns out it was.

```
$ strings rope
__PAGEZERO
__TEXT
__text
__TEXT
__stubs
__TEXT
__stub_helper
__TEXT
__cstring
__TEXT
__unwind_info
__TEXT
__DATA
__nl_symbol_ptr
__DATA
__la_symbol_ptr
__DATA
__LINKEDIT
/usr/lib/dyld
/usr/lib/libSystem.B.dylib
Give me a magic number: 
First part is: flag{r0pes_ar3_
Second part is: just_l0ng_str1ngs}
@dyld_stub_binder
@_printf
@_puts
@_scanf
_mh_execute_header
!main
__mh_execute_header
_main
_printf
_puts
_scanf
dyld_stub_binder
```

Below are the important strings in the elf file.

```
First part is: flag{r0pes_ar3_
Second part is: just_l0ng_str1ngs}
```

The flag is flag{r0pes_ar3_just_l0ng_str1ngs}