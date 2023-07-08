bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit , printf, scanf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific function
import printf msvcrt.dll
import scanf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 15
    b dw 0
    spatiu dw 0
    format db "%d", 0
    
; our code starts here
segment code use32 class=code
    start:
        ; 8) Se da un numar natural a (a: dword, definit in segmentul de date). Sa se citeasca un numar natural b si sa se calculeze: a + a/b. Sa se afiseze rezultatul operatiei. Valorile vor fi afisate in format decimal (baza 10) cu semn.
        
        
        push b ; punem parametrii pe stiva de la dreapta la stanga
        push dword format
        call [scanf] ; apelam functia scanf pentru citire
        add esp, 4*2 ; eliberam parametrii de pe stiva
        
        mov ax, word[a] ; punem in dx:ax pe a
        mov dx, word[a+2]
        idiv word[b] ; impartim dx:ax la b
        cwde ; conversie cu semn de la ax la eax
        add eax, [a] ; aduna la eax a astfel incat in eax sa avem a+a/b
        
        push eax ; punem in stiva parametrii de la dreapta la stanga
        push dword format 
        call [printf] ; apelam functia printf
        add esp, 4*2 ; eliberam parametrii de pe stiva
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
