bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data
    
    a db 4
    b db 3
    c db 15
    d dw 9

segment code use32 class=code
    start:
        ; 8. (100*a+d+5-75*b)/(c-5)
        ; a,b,c - BYTE , d - WORD
        mov edx, 0
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        ; 100*a+d+5-75*b = 100*4+9+5-75*b = 414 - 225 = 189
        ; 100*a+d+5
        mov ax, 100
        mov bl, [a]
        mul bl
        add ax, [d]
        add ax, 5
        mov bx, ax
        ; 75*b
        mov ax, 75
        mov cl, [b]
        mul cl
        ;100*a+d+5-75*b
        neg ax
        add ax, bx
        ; c - 5 = 15 - 5 = 10
        mov ebx, 0
        add bl, [c]
        sub bl, 5
        ; (100*a+d+5-75*b)/(c-5) = 18 rest 9
        div bx
        
        
        push    dword 0      
        call    [exit]    
