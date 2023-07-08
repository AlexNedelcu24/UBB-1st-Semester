bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    
    s dd 12345678h, 1A2C3C4Dh, 98FCDC76h
    l equ ($-s)/4 ; lungimea sirului
    d times l db 0 ; noul sir
    zece db 10 ; variabila folosita pentru impartiri la 10
    octet db 0

; our code starts here
segment code use32 class=code
    start:
        ; 8. Se da un sir de dublucuvinte. Sa se obtina sirul format din octetii inferiori ai
        ; cuvintelor superioare din elementele sirului de dublucuvinte care sunt palindrom in scrierea in baza 10.
        
        mov esi, s
        cld ; parcurgem sirul de la stanga la dreapta
        mov ecx, l ; vom avea l iteratii in bucla
        mov edi, d
        
        jecxz final
        repeta:
               lodsd  ; in eax avem dublucuvantul din sir de pe pozitia esi
               
               mov ebx, ecx
               mov cl, 16 ; ne deplasam 16 biti spre dreapta
               shr eax, cl
               mov ecx, ebx               
               
               mov ah, 0 ; folosim octetul inferior din cuvant
               
               mov [octet], al
       
               mov ebx, 0
               
               palindrom:   
                    div byte[zece]  ; facem inversul octetului inferior
                    mov dh, ah
                    mov dl, al 
                    mov al, bl ; calculam inversul in al dupa formula al = bl*10+dh
                               ; unde bl este inversul calculat pana in acest moment si dh este untima cifra adaugata                    
                    mov ah, 0
                    mul byte[zece]
                    add al, dh
                    mov bl, al ; punem inversul in bl
                    mov al, dl ; in al pastram catul impartirii
                    mov ah, 0
                    
                    cmp al, 0 ; daca avem catul = 0 ne oprim
                    jne palindrom
                    
               cmp bl, [octet] ; comparam numarul cu inversul sau
               je adauga
               jne urmatorul
               
               adauga:
                 mov al, [octet] 
                 stosb ; punem elementul in noul sir pentru ca este palindrom
                 
               urmatorul:
        loop repeta
        final:
               
                    
               
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
