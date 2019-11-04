section .data
     a dd 4,5
     p db "this is a string",10,0
     c db "this is a boy",10,0
section .bss
     q resb 1
     q resd 2
section .text
     global main
     extern printf,abc
main:
     mov ebx,ecx
     mov a,a
     add ecx,20
     mov ebx,eax
