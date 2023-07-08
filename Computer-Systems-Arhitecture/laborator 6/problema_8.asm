bits 32 

global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    
    a dw 0110110011101010b
    b dw 0100011100101100b
    c db 0
    d dd 0

segment code use32 class=code
    start:
        ; 8. Se dau doua cuvinte A si B. Sa se obtina un octet C care are:
        ; pe bitii 0-5, bitii 5-10 ai cuvantului A
        ; pe bitii 6-7 bitii 1-2 ai cuvantului B.
        ; Sa se obtina dublucuvantul D care are :
        ; pe bitii 8-15, bitii lui C
        ; pe bitii 0-7, bitii 8-15 din B
        ; pe bitii 24-31, bitii 0-7 din A
        ; iar pe bitii 16-23, bitii 8-15 din A.
        
        mov ebx, 0 ; in bl vom calcula rezultatul
        
        mov ax, [a] ; ax = a = 0110110011101010b
        and ax, 0000011111100000b ; izolam bitii 5-10 ai lui a
                                  ; ax = 0000010011100000b
        mov cl, 5
        ror ax, cl ; rotim 5 pozitii spre dreapta
                   ; ax = 0000000000100111b = 27h = 39
        or bl, al ; punem bitii in rezultat
                  ; bl = 00100111b = 27h = 39
        
        mov ax, [b] ; ax = b = 0100011100101100b
        and ax, 0000000000000110b ; izolam bitii 1-2 ai lui b
                                  ; ax = 0000000000000100b
        mov cl, 5
        rol ax, cl ; rotim 5 pozitii spre stanga 
                   ; ax = 0000000010000000b
        or bl, al ; punem bitii in rezultat
                  ; bl = 10100111b = A7h = 167
                  
        mov [c], bl ; punem valoarea din registru in variabila rezultat
        
        mov ebx, 0
        mov ecx, 0 ; in bx:cx vom calcula rezultatul
        
        or ch, [c] ; punem bitii in rezultat
                   ; bx:cx = 00000000000000001010011100000000b = A700h = 42752
                   
        mov ax, [b] ; ax = b = 0100011100101100b
        or cl, ah ; punem bitii in rezultat
                  ; bx:cx = 00000000000000001010011101000111b = A747h = 42823
                  
        mov ax, [a] ; ax = a = 0110110011101010b
        or bh, al ; punem bitii in rezultat
                  ; bx:cx = 11101010000000001010011101000111b = EA00A747h = 3925911367
                  
        mov ax, [a] ; ax = a = 0110110011101010b
        or bl, ah ; punem bitii in rezultat
                  ; bx:cx = 11101010011011001010011101000111b = EA6CA747h = 3932989255
             
        mov eax, 0
             
        push bx
        push cx
        pop eax
        
        mov [d], eax
    
        ; exit(0)
        push    dword 0      
        call    [exit]      
