bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data
    
    a db 17
    b dw 11
    d dq 5

segment code use32 class=code
    start:
        ; 8. (a+b-d)+(a-b-d)
        ; a - byte, b - word, c - double word, d - qword
        
        mov al, [a] ; al = 17 = 11h
        cbw ; conversie cu semn de la al la ax
            ; ax = a = 17 = 11h
        add ax, [b] ; ax = a+b = 17 + 11 = 28 = 1Ch
        cwde ; conversie cu semn de la ax la eax
             ; eax = 28 = 1Ch
        cdq ; conversie cu semn de la eax la edx:eax     
            ; edx:eax = 28 = 1Ch
        sub eax, dword [d]
        sbb edx, dword [d+4] ; edx:eax = a+b-d = 28 - 5 = 23 = 17h
        mov ecx, eax
        mov ebx, edx ; ebx:ecx = 23 = 17h
        mov eax, 0
        mov al, [a] ; al = 17 = 11h
        cbw ; conversie cu semn de la al la ax
            ; ax = 17 = 11h
        sub ax, [b] ; ax = a-b = 17 - 11 = 6
        cwde ; conversie cu semn de la ax la eax         
             ; eax = 6
        cdq ; conversie cu semn de la eax la edx:eax        
            ; edx:eax = 6
        sub eax, dword [d]
        sbb edx, dword [d+4] ; edx:eax = a-b-d = 6 - 5 = 1
        add eax, ecx 
        adc edx, ebx ; edx:eax = 23 + 1 = 24 = 18h
        
    
        ; exit(0)
        push    dword 0      
        call    [exit]       
