%ifndef _BAZA8_ASM_ ; continuăm dacă _FACTORIAL_ASM_ este nedefinit
%define _BAZA8_ASM_ ; și ne asigurăm că devine definit
                        ; astfel, %include permite doar o singură includere
                        
segment data use32 class=data
    opt db 8
    zece db 10
segment code use32 class=code

    imparte:
        mov eax, [esp+4] ; punem in eax numarul de pe stiva
        
        mov cl, 1
        mov ebx, 0
        
        sta:
           div byte [opt] ; impartim numarul la 8
           mov dl, al ; punem catul in dl
           mov dh, ah ; punem restul in ah
           
           mov al, dh ; in al punem restul
           mul cl ; inmultim cu cl care o sa fie 1 la inceput
           mov ch, 0
           add bx, ax ; in bx vom forma numarul in baza 8
           
           mov al, cl 
           mul byte [zece] 
           mov cl, al ; cl este inmultit cu 10 in urma celor 3 instructiuni
           
           mov al, dl ; punem catul inapoi in al
           
           cmp al, 0 
           jne sta ; daca catul este diferit de 0 sarim la eticheta sta
           
        ret 0
           
%endif       