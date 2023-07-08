bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data
    
    a db 6
    b db 22
    d db 8

segment code use32 class=code
    start:
        ; 23. [(a+b)*2]/(a+d)
        ; a,b,d - BYTE
        mov eax, 0
        mov ebx, 0
        ; [(a+b)*2]/(a+d) = 56 / 14 =  4
        ; (a+b)*2 = 56
        add al, [a]
        add al, [b]
        add bl, 2
        mul bl
        ; (a+d) 14
        mov ebx, 0
        add bl, [a]
        add bl, [d]
        ; [(a+b)*2]/(a+d) = 4
        div bl
    
        push    dword 0      
        call    [exit]    