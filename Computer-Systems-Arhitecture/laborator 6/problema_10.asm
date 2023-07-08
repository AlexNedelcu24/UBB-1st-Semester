bits 32 

global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    
    b db 01001010b
    a dw 1000110100101101b

segment code use32 class=code
    start:
        ; 10. Sa se inlocuiasca bitii 0-3 ai octetului B cu bitii 8-11 ai cuvantului A.
        mov ebx, 0 ; in bl vom calcula rezultatul
        
        mov bl, [b] ; bl = b = 01001010b = 4Ah = 74
        
        mov ax, [a] ; ax = a = 1000110100101101b
        and ax, 0000111100000000b ; izolam bitii 8-11 ai lui a
                                  ; ax = 0000110100000000b
        
        mov cl, 8
        ror ax, cl ; rotim 8 pozitii spre dreapta
                   ; ax = 0000000000001101b = Dh = 13
        
        and bl, 11110000b ; facem bitii 0-3 sa aiba valoarea 0 
                          ;  bl = 01000000b
        
        or bl, al ; inlocuim bitii 0-3 cu bitii 8-11
                  ; bl = 01001101b = 4Dh = 77
        
        mov [b], bl ; punem valoarea din registru in variabila
    
        ; exit(0)
        push    dword 0      
        call    [exit]       
