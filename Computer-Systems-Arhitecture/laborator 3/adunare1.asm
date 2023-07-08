bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data
    
    a db 31
    b db 11
    d db 14
    

segment code use32 class=code
    start:
        ; BYTE - 8. (a + b - d) + (a - b - d)
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        ; a + b - d = 31 + 10 - 14 = 27
        add bl, [a] ;bl=31
        add bl, [b] ;bl=31+10=41
        sub bl, [d] ;bl=41-14=27
        ; a - b - d = 31 - 10 - 14 = 7
        add cl, [a] ;cl=31
        sub cl, [b] ;cl=31-10=21
        sub cl, [d] ;cl=21-14=7
        ;(a + b - d) + (a - b - d) = 27 + 7 = 34
        add al, bl ;al=27
        add al, cl ;al=27+7=34
        
    
        push    dword 0      
        call    [exit]       
