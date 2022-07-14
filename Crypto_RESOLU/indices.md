quand je tente de faire un seedcracker:

>[!] Searching for the seed
>Good seed found = 213551287

Défaut d'implémentation, il n'y a pas d'appel à l'AES-256, la première ligne du fichier est la clef de déchiffrement.
une fois le fichier passé à la moulinette, il faut retirer les extras du début:
```bash
dd if=CONFIDENTIEL.xlsx of=clean_CONFIDENTIEL.xlsx bs=1 skip=32 status=progress
```

