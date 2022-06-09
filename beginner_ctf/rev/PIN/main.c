#include <stdio.h>
#include <stdbool.h>

int main() {
    int userNumber;

    printf("What is the PIN for my safe? \n"); 
    while (true) {
        scanf("%d", &userNumber);
        if(userNumber == 204372844) { 
            char *alphabet = "abcdefghijklmnopqrstuvwxyz";
            printf("%c%c%c%c{%c_%c%c%c%c_%c%c%c_%c%c%c_%c%c%c_%c%c%c%c%c%c%c%c%c%c_%c%c}", alphabet[3], alphabet[7], alphabet[1], alphabet[22], alphabet[8], alphabet[7], alphabet[14], alphabet[15], alphabet[4], alphabet[24], alphabet[14], alphabet[20], alphabet[3], alphabet[8], alphabet[3], alphabet[13], alphabet[14], alphabet[19], alphabet[1], alphabet[17], alphabet[20], alphabet[19], alphabet[4], alphabet[5], alphabet[14], alphabet[17], alphabet[2], alphabet[4], alphabet[8], alphabet[19]);
            return 0;
        } else {
            printf("That is not my PIN! Want to try another one? \n");
        }
    }
    
    return 0;
}
