bits 32 

global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    
    s db 1, 2, 4, 6, 10, 20, 25
    l equ $-s
    d times l db 0

segment code use32 class=code
    start:
        ; 9. Se da un sir de octeti S de lungime l. Sa se construiasca sirul D de lungime l-1 astfel incat elementele din D sa reprezinte diferenta dintre fiecare 2 elemente consecutive din S
        
        mov esi, 0
        mov edi, 0
        mov ecx, l ; ;punem lungimea in ecx si decrementam cu 1 pentru a putea realiza bucla loop de ecx - 1 ori
        dec ecx
        
        repeta:
            mov al, [s+esi] ; in al avem elementul din s la care ne aflam
            inc esi ; trecem la urmatorul element
            mov bl, [s+esi] ; in bl avem urmatorul element din s
            sub bl, al ; facem diferenta 
            mov [d+edi], bl ; adaugam diferenta in d
            inc edi
        loop repeta
    
        ; exit(0)
        push    dword 0      
        call    [exit]       
