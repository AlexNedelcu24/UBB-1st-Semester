bits 32 

global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    
    a dw 0001110110010110b
    b dw 0100111100101100b
    c dw 0111001000110010b
    d dw 0

segment code use32 class=code
    start:
        ; 31. Se dau cuvintele A, B si C. Sa se formeze cuvantul D ca suma a numerelor reprezentate de:
        ; biţii de pe poziţiile 1-5 ai lui A
        ; biţii de pe poziţiile 6-10 ai lui B
        ; biţii de pe poziţiile 11-15 ai lui C
    
        mov eax, 0 ; in ax vom calcula numerele
        mov ebx, 0 ; in dx vom calcula rezultatul
        
        mov ax, [a] ; ax = a = 0001110110010110b = 1D96h = 7574
        and ax, 0000000000111110b ; izolam bitii 1-5 ai lui a
                                  ; ax = 0000000000010110b = 16h = 22
        mov cl, 1
        ror ax, cl ; rotim o pozitie spre dreapta bitii
                   ; ax = 0000000000001011b = Bh = 11
        add bx, ax ; bx = 11 = Bh
        
        mov ax, [b] ; bx = b = 0100111100101100b = 4F2Ch = 20268
        and ax, 0000011111000000b ; izolam bitii 6-10 ai lui b
                                  ; ax = 0000011100000000b = 700h = 1792
        mov cl, 6 
        ror ax, cl ; rotim 6 pozitii spre dreapta bitii
                   ; ax = 0000000000011100b = 1Ch = 28 
        add bx, ax ; bx = 11 + 28 = 39 = 27h
        
        mov ax, [c] ; ax = c = 0111001000110010b = 7232h = 29234
        and ax, 1111100000000000b ; izolam bitii 11-15 ai lui c
                                  ; ax = 0111000000000000b
        mov cl, 5
        rol ax, cl ; rotim 5 pozitii spre stanga bitii
                   ; ax = 0000000000001110b = Eh = 14
        add bx, ax ; bx = 39 + 14 = 53 = 35h
    
        mov [d], bx ; punem valoarea din registru in variabila rezultat
                    ; d = 53 = 35h
    
        ; exit(0)
        push    dword 0      
        call    [exit]       
