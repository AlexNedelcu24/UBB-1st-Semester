bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data
    
    a db 12
    b db 3
    e dw 17

segment code use32 class=code
    start:
        ; 8. 2*(a+b)-e
        ; a,b - BYTE , e - WORD
        mov eax, 0
        mov ebx, 0
        ; 2*(a+b)-e = 30 - 17 = 13
        add al, 2
        add bl, [a]
        add bl, [b]
        mul bl
        sub ax, [e]
    
        push    dword 0      
        call    [exit]    