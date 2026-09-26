# cafe-menu

Les QR des tables restent les mêmes :

- Menu Bas : https://youssefmliki.github.io/cafe-menu/MENU_BAS.pdf
- Menu Haut : https://youssefmliki.github.io/cafe-menu/MENU_HAUT.pdf

## Horaires (heure de Tunisie)

- **Menu Bas** : toujours le même
- **17:00 à 00:00** : `MENU_HAUT.pdf` affiche le Menu Bas
- **00:00 à 17:00** : `MENU_HAUT.pdf` revient au Menu Haut

Un robot GitHub vérifie l’heure toutes les 10 minutes. Les QR ne changent pas.

## Modifier les prix

- Menu Bas : éditer `MENU_BAS.pdf`
- Menu Haut (journée) : éditer `source/MENU_HAUT_ORIGINAL.pdf`

Ne pas éditer `MENU_HAUT.pdf` à la main : il est remplacé tout seul selon l’horaire.
