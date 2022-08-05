# Excel Confidential

## 0x1 : tldr

Ce flag peut être récupéré via différents tricks, je vais vous en montrer trois (dont un qui n'était pas prévu par les admins je pense)

## 0x2 : Le souci de compréhension entre les logiciels

Cette méthode n'était surement pas attendue par les créateurs du challenge, mais elle m'a permis de flag instantanément.

En effet, le fichier étant en XLSX, il est lisible avec libreoffice, mais malheureusement pour l'admin, la sécurité qui rend le tableau invisible sans le mdp n'est pas pris en charge.

Il suffit donc simplement d'ouvrir le document, puis faire un clic droit sur sur **AVERTISSEMENT** puis **Show Sheets** et pour finir de faire afficher **CONFIDENTIEL**

Le flag est donc:
>HACK{3xcEl_R3al_Pr0TeCT10N?}

## 0x3 : Excel et la (pseudo) sécurisation

Le premier réflexe que j'ai sur un fichier excel, c'est de vérifier la présence de macro et de worksheets cachées. Dans ce cas, nous trouvons rapidement qu'une sécurité a été mise en place, et excel demande un mot de passe.

Excel ne se connectant pas à Internet pour chercher cette information, il est forcément stocké dans le fichier, et nous sommes chanceux, car un fichier **xlsx** n'est ni plus ni moins un gros fichier zippé.

Sur Windows, avec 7zip, vous pouvez faire un clic droit sur le fichier, puis extraire les données. Ensuite vous allez dans le dossier créé, puis **xl**, et dans le fichier **workbook.xml**, supprimez la ligne suivante:

```xml
<workbookProtection workbookAlgorithmName="SHA-512" workbookHashValue="a6oCJWjPnijL69gmt2YwUFFJRdipxjVdShBQV6sQxfo32KRpXvSiNF7s05kP3izVnrpSvZcCGcVubPhuMMqTFg==" workbookSaltValue="yhMlpLTVjq3RdhG6XOLTlw==" workbookSpinCount="100000" lockStructure="1"/>
```

Ce qui aura pour effet de supprimer la protection sur la feuille de calcul, et elle sera donc lisible de nouveau sans le mot de passe.

## 0x4 : En utilisant le script flagfinder.py

Ben oui, un peu d'auto-promotion n'a jamais tué personne, clonez mon [repo github](https://github.com/tiphergane/FlagFinder) et suivez les informations pour l'installation, puis il vous suffira juste d'aller chercher dans le fichier **sharedStrings.xml** avec la commande suivante:


```bash
[*] Opening file: xl/sharedStrings.xml
[*] Searching for pattern: HACK{.*?}
[+] Yeah !!!! flag found: HACK{3xcEl_R3al_Pr0TeCT10N?}
[!] flag is now copied in flag.txt
[+] Yeah !!!! flag found: HACK{ImplementationErrorBreaksCiphers}
[!] flag is now copied in flag.txt
```


