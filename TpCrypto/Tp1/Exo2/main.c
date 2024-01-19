#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void chiffrementVigenere(const char *message, const char *key, char *cryptogramme) {
    unsigned int i, size = strlen(key);

    for (i = 0; message[i] != '\0'; i++) {
        if ((message[i] >= 'a') && (message[i] <= 'z')) {
            int rang = (message[i] + key[i % size] - 2 * 'a') % 26;
            cryptogramme[i] = 'a' + rang;
        } else if ((message[i] >= 'A') && (message[i] <= 'Z')) {
            int rang = (message[i] + key[i % size] - 'a' - 'A') % 26;
            cryptogramme[i] = 'A' + rang;
        } else {
            cryptogramme[i] = message[i];
        }
    }
    cryptogramme[i] = '\0';
}

void dechiffrementVigenere(const char *cryptogramme, const char *key, char *message) {
    unsigned int i, size = strlen(key);
    char keytemp[size + 1];

    for (i = 0; key[i] != '\0'; i++) {
        int rang = (26 - (key[i] - 'a')) % 26;
        keytemp[i] = rang + 'a';
    }
    keytemp[i] = '\0';

    chiffrementVigenere(cryptogramme, keytemp, message);
}

int main() {
    char msg[100] = "mastercsuemf  ";
    char cryp[100];

    chiffrementVigenere(msg, "clefvigenere ", cryp);


    printf("cryp = %s \n", cryp);


    char decrypted[100];
    dechiffrementVigenere(cryp, "clefvigenere ", decrypted);
    printf("decrypted = %s \n", decrypted);

    return 0;
}
