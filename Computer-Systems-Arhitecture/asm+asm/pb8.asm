bits 32

global start

import printf msvcrt.dll
import exit msvcrt.dll
extern printf, exit


%include "baza8.asm"

segment data use32 class=data
    ; ...
    a db 32
    format db `%d \n`, 0
    format2 db "%c", 10, 0

; our code starts here
segment code use32 class=code
start:
   ; Sa se afiseze, pentru fiecare numar de la 32 la 126, valoarea numarului (in baza 8) si caracterul cu acel cod ASCII.
   op:
        mov EAX, 0
        mov al, [a] ; punem numarul din a in al, iar a ia valori pe rand de la 32 la 126
        push eax ; punem numarul pe stiva
        call imparte ; apelam modulul asm imparte pentru a trece numarul in baza 8
        add esp, 1*4 ; eliberam parametrii de pe stiva
        

        pusha ; punem registrii pe stiva
        push ebx ; punem parametrii pe stiva
        push format
        call [printf] ; apelam functia printf pentru afisare
        add esp, 2*4 ; eliberam parametrii de pe stiva
        popa ; punem inapoi valorile in registrii
        
        pusha 
        push ebx ; punem parametrii pe stiva
        push format2
        call [printf]
        add esp, 2*4 ; eliberam parametrii de pe stiva
        popa
        
        add byte [a], 1 ; trecem la urmatorul numar
        
        
        
        cmp byte [a], 126 ; comparam numarul cu 126
        jna op ; daca numarul este mai mic sau egal decat 126 repetam procesul
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
