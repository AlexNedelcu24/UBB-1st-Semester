bits 32 

global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    
    a dw 1
    b dw 2
    c db 8
    d db 3
    x dq 6
    e dd 4

segment code use32 class=code
    start:
        ; 8. 1/a+200*b-c/(d+1)+x/a-e
        ; a,b-word, c,d-byte, e-doubleword, x-qword
        
        mov ax, 1 ; ax = 1
        cwd ; conversie cu semn de la ax la dx:ax
             ; dx:ax = 1
        idiv word [a] ; ax = 1/a = 1/1 = 1 , dx = 1%a = 0
        
        cwde ; conversie cu semn de la ax la eax
             ; eax = 1/a = 1
        mov ebx, eax ; ebx = 1/a = 1
        mov eax, 0
        
        mov ax, 200 ; ax = 200 = C8h
        imul word [b] ; dx:ax = ax * b = 200 * 2 = 400 = 190h
        push dx
        push ax
        pop eax ; eax = 200*b = 400 = 190h
        
        add ebx, eax ; ebx = 1/a+200*b = 1 + 400 = 401 = 191h
        mov eax, 0
        
        mov al, [c] ; al = c = 8
        cbw ; conversie cu semn de la al la ax
            ; ax = c = 8
        mov dl, [d] ; dl = d = 3
        add dl,  1 ; dl = d+1 = 3 + 1 = 4
        idiv dl ; al = ax/dl = c/(d+1) = 8 / 4 = 2 , ah = ax%dl = 8 % 4 = 0
        
        cbw ; conversie cu semn de la al la ax
            ; ax = c/(d+1) = 2
        cwd ; conversie cu semn de la ax la eax 
            ; eax = c/(d+1) = 2
        sub ebx, eax ; ebx = 1/a+200*b-c/(d+1) = 401 - 2 = 399 = 18Fh
        sub ebx, [e] ; ebx = 1/a+200*b-c/(d+1)-e = 399 - 4 = 395 = 18Bh
        mov eax, 0
        
        mov ax, [a] ; ax = a = 1
        cwde ; conversie cu semn de la ax la eax
             ; eax = a = 1
        mov ecx, eax ; ecx = a = 1
        
        mov eax, dword [x]
        mov edx, dword [x+4] ; edx:eax = x = 6
        
        idiv ecx ; eax = edx:eax/ecx = x/a = 6/1 = 6 , edx = x%a = 0
        
        add ebx, eax ; ebx = 1/a+200*b-c/(d+1)+x/a-e = 395 + 6 = 401 = 191h
        
    
        ; exit(0)
        push    dword 0      
        call    [exit]       
