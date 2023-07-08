bits 32

global _convert_unsigned
extern _printf

segment data use32 class=data
    saispe dd 0x10
    temporar db 0
    format db "mesaj %d", 0

segment code use32 class=code
    _convert_unsigned:  ;unsigned int convert(int n, char *s);
        push ebp
        mov ebp, esp
        ;[ebp] valoarea ebp pt apelant
        ;[ebp + 4] adresa de return
        mov ecx, [ebp + 8] ; [ECX] = n
        cld
        mov esi, [ebp + 12] ; esi pointeaza spre s[0]
        
        mov ebx, 0 ;in ebx retinem rezultatul
    repeta:
        LODSB ;al <- cifra curenta
      
        cmp al, '0'
        jb loop_repeta
        cmp al, '9'
        ja verifica_litera_hexa
        sub al, '0' ; al - cifra curenta
        jmp calcul
        
    verifica_litera_hexa:
        cmp al, 'a'
        jb loop_repeta
        cmp al, 'f'
        ja loop_repeta
        sub al, 'a'
        add al, 10 ; al - cifra curenta
        
    calcul:
        mov byte[temporar], al
        
        mov eax, ebx ; eax - rezultatul curent
        mul dword[saispe] ;edx:eax - rezultatul * 16
        mov ebx, eax
        add ebx, [temporar] ;ebx - rezultatul ce trb pe parcurgerea curenta        
    loop_repeta:
        loop repeta
    
    final:
        mov eax, ebx
        mov esp, ebp
        pop ebp
        ret