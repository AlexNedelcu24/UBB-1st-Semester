bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data
    
    a dw 7
    b dw 8
    c dw 2
    d dw 5

segment code use32 class=code
    start:
        ; WORD - 8. (b+c+d)-(a+a)
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        ; b + c + d = 8 + 2 + 5 = 15
        add bx, [b] ;bx=8
        add bx, [c] ;bx=8+2=10
        add bx, [d] ;bx=10+5=0015
        ; a + a = 7 + 7 = 14
        add cx, [a] ;cx=7
        add cx, [a] ;cx=7+7=14
        ; (b+c+d)-(a+a) = 15 - 14 = 1
        add ax, bx ;ax=15
        sub ax, cx ;ax=15-14=1
    
        push    dword 0      
        call    [exit]    
