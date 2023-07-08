bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data
    
    a db 7
    b db 3
    c db 12
    d dw 40

segment code use32 class=code
    start:
        ; 23. [(a+b)*3-c*2]+d
        ; a,b,c - BYTE , d - WORD
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        ;[(a+b)*3-c*2]+d
        ;(a+b)*3 = 30
        add al, [a]
        add al, [b]
        add bl, 3
        mul bl
        mov bx, ax
        ; c*2 = 24
        mov al, [c]
        mov cl, 2
        mul cl
        ; (a+b)*3-c*2 = 30 - 24 = 6
        sub bx, ax
        mov ax, bx
        ; [(a+b)*3-c*2]+d = 6 + 40 = 46
        add ax, [d]
        
    
        push    dword 0      
        call    [exit]    