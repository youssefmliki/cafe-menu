# cafe-menu

Les QR des tables restent les mêmes :

- Menu Bas : https://youssefmliki.github.io/cafe-menu/MENU_BAS.pdf
- Menu Haut : https://youssefmliki.github.io/cafe-menu/MENU_HAUT.pdf

## Horaires (heure de Tunisie)

- **Menu Bas** : toujours le même
- **17:00 à 00:00** : le QR Haut affiche le Menu Bas
- **00:00 à 17:00** : le QR Haut revient au Menu Haut

Un robot GitHub vérifie à 17h, à minuit, et toutes les 15 minutes.

## Modifier les prix

- Menu Bas : éditer `MENU_BAS.pdf`
- Menu Haut (journée) : éditer `source/MENU_HAUT_ORIGINAL.pdf`

Ne pas éditer `MENU_HAUT.pdf` à la main : il est remplacé tout seul selon l’horaire.
