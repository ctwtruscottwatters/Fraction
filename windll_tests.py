from ctypes import *
from time import sleep

def main():
    print(windll.kernel32)
    print(cdll.msvcrt)
    print(windll.kernel32.GetModuleHandleA())
    printf = cdll.msvcrt.printf
    printf.argtypes = [c_char_p]
    printf(b"Hello, World!\n")
    sscanf = cdll.msvcrt.sscanf
    sleep(30)
    i = c_int()
    j = c_float()
    k = c_float()
    s = create_string_buffer(b"\00" * 32)
    sscanf(b"1.33 13.1993 Charles", b"%llf %llf %s", byref(j), byref(k), s)
    print(i.value, j.value, repr(s.value), k.value)

if __name__ == "__main__": main()
