#include <stdio.h>
#include <string.h>

unsigned int convert_unsigned(int n, char s[]);

int main()
{
    int n, signed_list[500], signed_value = 0;
    unsigned int unsigned_list[500], unsigned_value = 0;
    char s[500];
    printf("Introdu nr de elemente: ");
    scanf("%d", &n);
    printf("Introdu elementele: ");
    for (int i = 0; i < n; ++i)
    {
        scanf("%s", s);
        unsigned_value = convert_unsigned(strlen(s), s);
        printf("%u ", unsigned_value);
        unsigned_list[i] = unsigned_value;
        signed_list[i] = 0;
    }
    printf("\nLista de numere fara semn: ");
    for (int i = 0; i < n; ++i)
        printf("%u ", unsigned_list[i]);
    printf("\nLista de numere cu semn: ");
    for (int i = 0; i < n; ++i)
        printf("%d ", signed_list[i]);
}