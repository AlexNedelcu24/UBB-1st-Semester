bits 32 

global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    
    a db 10
    b dw 52
    c dd 148
    d dq 100

segment code use32 class=code
    start:
        ; 8. (b+c+d)-(a+a)
        ; a - byte, b - word, c - double word, d - qword
        
        mov ax, [b] ; ax = b = 52 = 34h
        mov dx, 0 ; conversie fara semn de la ax la dx:ax 
                  ; dx:ax = 52 = 34h
        push dx
        push ax
        pop eax ; eax = b = 52 = 34h
        add eax, [c] ; eax = b+c = 52 + 148 = 200 = C8h
        mov edx, 0 ; conversie fara semn de la eax la edx:eax
        add eax, dword [d]
        add edx, dword [d+4] ; edx:eax = b+c+d = 200 + 100 = 300 = 12Ch
        mov ecx, eax
        mov ebx, edx ; ebx:ecx = 300 = 12Ch
        mov eax, 0
        mov edx, 0
        mov al, [a] ; al = 10 = Ah
        add al, al  ; al = 10 + 10 = 20 = 14h
        mov ah, 0 ; conversie fara semn de la al la ax 
                  ; ax = 20 = 14h
        mov dx, 0 ; conversie fara semn de la ax la dx:ax
                  ; dx:ax = 20 = 14h
        push dx
        push ax
        pop eax ; eax = 20 = 14h
        mov edx, 0 ; conversie fara semn de la eax la edx:eax
                   ; edx:eax = 20 = 14h
        sub ecx, eax
        sbb ebx, edx ; ebx:ecx = 300 - 20 = 280 = 118h
    
        ; exit(0)
        push    dword 0      
        call    [exit]       
