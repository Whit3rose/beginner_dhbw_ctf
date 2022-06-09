#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string.h>

char* options[3] = {"first", "second", "third"};
char* lose1[3] = {"second", "third", "first"};
char* lose2[3] = {"third", "first", "second"};
int wins = 0;

bool game() {
    int real = rand() % 3;
    char guess[30];

    printf("Below which cup is the ball? \nTake a guess: first, second or third? ");
    scanf("%s", guess);
    printf("You guessed: %s\n", guess);
    printf("Correct cup: %s\n", options[real]);

    if (strstr(guess, options[real])) {
        puts("You win! Play again?");
        return true;
    } else {
        puts("Seems like you didn't win this time. Play again?");
        return false;
    }
}

int main()
{
    printf("Let's play a couple rounds of shell game. If you win 10 times in a row you will get the flag!");
    while (true) {
        if (game() == true) {
            wins++;
            if (wins == 10) {
                char *alphabet = "abcdefghijklmnopqrstuvwxyz";
                printf("%c%c%c%c{%c%c%c%c%c_%c%c%c%c_%c%c%c%c_%c%c%c%c%c%c%c%c_%c%c_%c%c%c_%c%c%c%c}", alphabet[3], alphabet[7], alphabet[1], alphabet[22], alphabet[11], alphabet[14], alphabet[14], alphabet[10], alphabet[18], alphabet[11], alphabet[8], alphabet[10], alphabet[4], alphabet[19], alphabet[7], alphabet[0], alphabet[19], alphabet[5], alphabet[20], alphabet[13], alphabet[2], alphabet[19], alphabet[8], alphabet[14], alphabet[13], alphabet[8], alphabet[18], alphabet[13], alphabet[14], alphabet[19], alphabet[18], alphabet[0], alphabet[5], alphabet[4]);
            }
        } else {
            wins = 0;
        }
    }
}