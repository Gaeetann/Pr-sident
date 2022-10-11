# Python Exercice : Le jeu du président

Le président (aussi appelé le troufion) est un jeu de cartes rapide et amusant, au cours duquel la hiérarchie des joueurs changera à chaque manche. Le vainqueur d'une manche devient le président, alors que le perdant est proclamé troufion. Une fois que vous maitriserez les règles de base, vous pourrez essayer différentes variantes de ce jeu très populaire.

## Exercice 1
Générer un deck de 52 cartes.
Rédiger les méthodes magiques permettant de comparer deux cartes.

.Afin de vous assurer que le code généré fonctionne. Executez
 les tests suivants. 
 
 `python test_exercice1.py`

## Exercice 2
Afin de pouvoir jouer au président, il va être nécessaire d'implémenter la
 classe d'un joueur. Et de distribuer les cartes aux joueurs. 
 
Afin de faciliter les tests, nous allons considérer qu'il y a trois joueurs
 présents autour de la table. 
 
Ainsi, dans cette étape, implémentez les classes `PresidentGame` et `Player`.

.Afin de vous assurer que le code généré fonctionne. Executez
 les tests suivants. Adaptez les si vos classes ont des méthodes différentes. 
 
 `python test_exercice2.py`

 
## Exercice 3
Nous avons maintenant une partie qui peut se lancer. N'ayant pas d'interface
 graphique pour le moment, nous allons réaliser les échanges avec le joueur
  par le biais de la console. 

A partir du fichier `main.py`, implémentez une petite interface pour repr
ésenter les cartes au sein de la console, et permettre au joueur de choisir les cartes à joueur. 
 
 Il est possible de sélectionner plusieurs cartes dès lors qu'elles ont la m
 ême valeur. 
 
 Une vérification doit être mise en place pour voir si le choix de l
 'utilisateur est correct.
 
 ## Encore à implémenter
 - [ ] Le déroulé d'une manche. 
    - Chaque utilisateur doit fournir s'il peut (ou veut) la quantité de cartes demandées.
    - Les cartes doivent être du même type
    - Le vainqueur d'une manche ouvre la manche suivante
    - Il existe un gagnant
 - [ ] Gestion d'une fin et lancé de nouvelle partie
 - [ ] Le mécanisme de troufion et de président
    - En fonction du nombre de joueurs, il peut exister : 
        - Un président et un troufion si 3 ou 4 joueurs (1 carte)
        - Ajout d'un vice président et d'un vice troufion si 5+ (2 cartes (président <-> trouffion), 1 carte (vice <-> vice))
    - Le troufion doit donner sa meilleure carte, le président choisit quelle carte donner
 - [ ] Interface graphique
 - [ ] Intelligence artificielle 
