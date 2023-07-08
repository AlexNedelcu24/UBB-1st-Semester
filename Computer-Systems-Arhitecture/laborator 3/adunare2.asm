bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data
    
    a db 25
    c db 13
    b db 10
    d db 12

segment code use32 class=code
    start:
        ; BYTE  23. (a-c)+(b+b+d)
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        ; a - c = 25 - 13 = 12
        add bl, [a] ;bl=25
        sub bl, [c] ;bl=25-13=12
        ; b + b + d = 10 + 10 + 12 = 32
        add cl, [b] ;cl=10
        add cl, [b] ;cl=10+10=20
        add cl, [d] ;cl=20+12=32
        ; (a-c)+(b+b+d) = 12 + 32 = 44
        add al, bl ;al=12
        add al, cl ;al=12+32=44
    
        push    dword 0      
        call    [exit]    