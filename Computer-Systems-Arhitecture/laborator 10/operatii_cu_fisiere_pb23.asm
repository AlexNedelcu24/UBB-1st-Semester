bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fprintf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    nume_fisier dd "a.txt", 0
    Write dd "w", 0
    t dd 0
    buffer db 0
    format db `%X \n`, 0
    a dw 937h
    zece db 10h
    

; our code starts here
segment code use32 class=code
    start:
        ; 23) Se da numele unui fisier si un numar pe cuvant scris in memorie. Sa se scrie cifrele hexazecimale ale acestui numar ca text in fisier, fiecare cifra pe o linie separata.
        
        ;deschidem fisierul pentru a scrie in el (se creeaza un fisier nou)
        push dword Write ; punem parametrii pe stiva de la dreapta la stanga
        push dword nume_fisier
        call [fopen] ; apelam functia fopen pentru deschiderea fisierului
        add esp, 4*2 ; eliberam parametrii de pe stiva
        cmp eax, 0 ; verificam daca in eax a fost returnat descriptorul de fisier
        je final
        mov [t], eax ; punem in t descriptorul de fisier
        
        mov eax, 0
        mov ax, [a] ; punem in ax numarul a
        
        repeta:
           div byte[zece] ; impartim la 10h
           mov [buffer], ah ; retinem restul in buffer pentru a il scrie in fisier
           mov bl, al ; catul il retinem in bl
           
           ;fprintf(t, format, buffer)
           mov eax, 0
           mov al, [buffer] ; punem valoarea din buffer in al
           
           push eax ; punem parametrii pe stiva de la dreapta la stanga
           push dword format
           push dword [t]
           call [fprintf] ; apelam functia fprintf pentru scrierea in fisier
           add esp, 4*3 ; eliberam parametrii de pe stiva
           
           mov al, bl
           mov ah, 0
           
           cmp al, 0 ; verificam daca numarul nostru este diferit de 0
           jne repeta ; in caz afirmativ repetam procesul
           
        push dword [t] ; punem descriptorul de fisier pe stiva
        call [fclose] ; apelam functia fclose pentru inchiderea fisierului
        add esp, 4 ; eliberam parametrii de pe stiva
        
        final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
