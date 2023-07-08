bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data
    
    a db 2
    b dw 5
    c dd 10
    d dq 20

segment code use32 class=code
    start:
        ; 8. (b+c+d)-(a+a)
        ; a - byte, b - word, c - double word, d - qword
        
        mov ax, [b] ; ax = b = 5 = 5h
        cwde ; converteste cu semn de la ax la eax         
        ; eax = 5 = 5h
        add eax, [c] ; eax = b+c = 5+10 = 15 = Fh
        cdq ; conversie cu semn de la eax la edx:eax
            ; edx:eax = 15 = Fh
        add eax, dword [d]
        adc edx, dword [d+4] ; edx:eax = b+c+d = 15 + 20 = 35 = 23h
        mov ecx, eax
        mov ebx, edx ; ebx:ecx = 35 = 23h
        mov eax, 0
        mov al, [a] ; al = 2
        add al, al  ; al = 2 + 2 = 4
        cbw ; converteste cu semn de la al la ax  
            ; ax = 4
        cwde ; converteste cu semn de la ax la eax
             ; eax = 4
        cdq ;converteste cu semn de la eax la edx:eax 
            ; edx:eax = 4
        sub ecx, eax
        sbb ebx, edx ; ebx:ecx = (b+c+d)-(a+a) = 35 - 4 = 31 = 1Fh
                 
    
        ; exit(0)
        push    dword 0      
        call    [exit]       
