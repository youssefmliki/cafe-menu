# cafe-menu

Le QR des tables reste sur la même adresse :

https://youssefmliki.github.io/cafe-menu/MENU_BAS.pdf

## Horaires (heure de Tunisie)

- **17:00 à 23:58** : `MENU_BAS.pdf` affiche les prix du Menu Haut
- **23:58 à 17:00** : `MENU_BAS.pdf` revient aux prix du Menu Bas

Un robot GitHub vérifie l’heure toutes les 10 minutes et change le fichier automatiquement. Les QR des tables ne changent pas.

## Modifier les prix

- Prix **jour** (Menu Bas) : éditer `source/MENU_BAS_JOUR.pdf`
- Prix **soir / étage** (Menu Haut) : éditer `MENU_HAUT.pdf`

Ne pas éditer `MENU_BAS.pdf` à la main : il est remplacé tout seul selon l’horaire.
