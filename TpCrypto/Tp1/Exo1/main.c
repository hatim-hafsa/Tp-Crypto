#include <stdio.h>
#include <stdlib.h>

void chiffrementCesar(const char *message, short key, char *cryptogramme) {
    unsigned int i = 0;
    short rang;

    while (message[i] != '\0') {
        if ((message[i] >= 'a') && (message[i] <= 'z')) {
            rang = message[i] - 'a';
            rang = (rang + key) % 26;
            if (rang < 0) rang += 26;
            cryptogramme[i] = 'a' + rang;
        } else if ((message[i] >= 'A') && (message[i] <= 'Z')) {
            rang = message[i] - 'A';
            rang = (rang + key) % 26;
            if (rang < 0) rang += 26;
            cryptogramme[i] = 'A' + rang;
        } else {
            cryptogramme[i] = message[i];
        }
        i++;
    }

    cryptogramme[i] = '\0';
}


void dechiffrementCesar(const char *cryptogramme, short key, char *messageDechiffre) {
    unsigned int i = 0;
    short rang;

    while (cryptogramme[i] != '\0') {
        if ((cryptogramme[i] >= 'a') && (cryptogramme[i] <= 'z')) {
            rang = cryptogramme[i] - 'a';
            rang = (rang - key) % 26;
            if (rang < 0) rang += 26;
            messageDechiffre[i] = 'a' + rang;
        } else if ((cryptogramme[i] >= 'A') && (cryptogramme[i] <= 'Z')) {
            rang = cryptogramme[i] - 'A';
            rang = (rang - key) % 26;
            if (rang < 0) rang += 26;
            messageDechiffre[i] = 'A' + rang;
        } else {
            messageDechiffre[i] = cryptogramme[i];
        }
        i++;
    }

    messageDechiffre[i] = '\0';
}

int main() {
    char msg[100] = "mastercsuemf ";
    char cryp[100];
    char dechiffre[100];

    chiffrementCesar(msg, 3, cryp);
    printf("cryp = %s \n", cryp);

    dechiffrementCesar(cryp, 3, dechiffre);
    printf("dechiffre = %s \n",dechiffre );
    return 0;
}
