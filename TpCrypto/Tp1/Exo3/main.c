#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void chiffrementTransposition(const char *message, const int *key, char *cryptogramme) {
    int taille = strlen(message);
    int nbColonnes = taille / key[0] + (taille % key[0] ? 1 : 0);
    char matrice[key[0]][nbColonnes];

    for (int i = 0; i < key[0]; i++) {
        for (int j = 0; j < nbColonnes; j++) {
            matrice[i][j] = ' ';
        }
    }

    int index = 0;
    for (int col = 0; col < nbColonnes; col++) {
        for (int row = 0; row < key[0]; row++) {
            if (index < taille) {
                matrice[row][col] = message[index++];
            }
        }
    }

    index = 0;
    for (int col = 0; col < nbColonnes; col++) {
        for (int row = 1; row <= key[0]; row++) {
            if (key[row] <= nbColonnes) {
                cryptogramme[index++] = matrice[row - 1][col];
            }
        }
    }

    cryptogramme[index] = '\0';
}

void dechiffrementTransposition(const char *cryptogramme, const int *key, char *message) {
    int taille = strlen(cryptogramme);
    int nbColonnes = taille / key[0] + (taille % key[0] ? 1 : 0);
    char matrice[key[0]][nbColonnes];

    for (int i = 0; i < key[0]; i++) {
        for (int j = 0; j < nbColonnes; j++) {
            matrice[i][j] = ' ';
        }
    }

    int index = 0;
    for (int col = 0; col < nbColonnes; col++) {
        for (int row = 1; row <= key[0]; row++) {
            if (key[row] <= nbColonnes) {
                matrice[row - 1][col] = cryptogramme[index++];
            }
        }
    }

    index = 0;
    for (int row = 0; row < key[0]; row++) {
        for (int col = 0; col < nbColonnes; col++) {
            if (matrice[row][col] != ' ') {
                message[index++] = matrice[row][col];
            }
        }
    }

    message[index] = '\0';
}

int main() {
    char msg[100] = "mastercsuemf";
    char cryp[100];

    int key[] = {4, 3, 2, 5, 1, 4};

    chiffrementTransposition(msg, key, cryp);
    printf("cryp : %s\n", cryp);

    char dechiffre[100];
    dechiffrementTransposition(cryp, key, dechiffre);
    printf("dechiffrett : %s\n", dechiffre);

    return 0;
}
