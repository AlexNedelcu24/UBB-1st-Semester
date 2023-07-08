bits 32 

global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    
    s db 'a', 'A', 'b', 'B', '2', '%', 'x', 'M'
    l equ $-s
    d times l db 0

segment code use32 class=code
    start:
        ; 8. Se da un sir de caractere S. Sa se construiasca sirul D care sa contina toate literele mari din sirul S.
        mov esi, 0
        mov edi, 0
        mov ecx, l ;punem lungimea in ecx pentru a putea realiza bucla loop de ecx ori
        
        repeta:
            mov bl, [s+esi]  ; in bl vom avea elementul la care ne aflam din sirul s
            cmp bl, 'A'  ; comparam caracterul din s cu 'A'
            jb lessA
            jae bigA
        
            bigA:   ; daca este mai mare sau egal cu 'A'
                cmp bl, 'Z' ; comparam caracterul din s cu 'Z' 
                jbe lessZ
                ja bigZ
                  lessZ:  ; daca este mai mic sau egal cu 'Z'
                    mov [d+edi], bl  ; adaugam caracterul in noul sir
                    inc edi
                    inc esi  ; trecem la urmatorul caracter
                    jmp end_repeta
                  bigZ:
                    inc esi  ; trecem la urmatorul caracter
                    jmp end_repeta
            lessA:
              inc esi  ; trecem la urmatorul caracter
          
        end_repeta:
        loop repeta
        
        
    
        ; exit(0)
        push    dword 0      
        call    [exit]       
