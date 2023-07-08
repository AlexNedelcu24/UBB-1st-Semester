bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data
    
    a dw 12
    b dw 25
    c dw 3
    d dw 13

segment code use32 class=code
    start:
        ; WORD -  23. (a+b+c)-(d+d)
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        ; a + b + c = 12 + 25 + 3 = 40
        add bx, [a] ;bx=12
        add bx, [b] ;bx=12+25=37
        add bx, [c] ;bx=37+3=40
        ; d + d = 13 + 13 = 26
        add cx, [d] ;cx=13
        add cx, [d] ;cx=13+13=26
        ; (a+b+c)-(d+d) = 40 - 26 = 14
        add ax, bx ;ax=40
        sub ax, cx ;ax=40-26=14
    
        push    dword 0      
        call    [exit]    