![](https://www.seao.ca/images/logo_seao2.png)

Extraction des infos contenues dans les fichiers .xml du Système électronique d'appels d'offres (SÉAO) du gouvernement du Québec
-----

### Étape 1

Téléchargement de tous les [fichiers .xml du SÉAO](https://www.donneesquebec.ca/recherche/fr/dataset/systeme-electronique-dappel-doffres-seao).

### Étape 2

Extraction des informations contenues dans ces fichiers .xml en un seul fichier .csv grâce au script [**univ01.py**](univ01.py). Le fichier .csv obtenu est trop volumineux pour être téléversé dans Github.

### Étape 3

Après avoir chargé le fichier .csv obtenu à l'étape 2 dans MySQL, on peut faire un `group by` pour identifier le nombre d'occurrences de chaque avis public. On obtient alors un autre fichier .csv qu'on peut appeler [**decompte-des-numeros-seao.csv**](decompte-des-numeros-seao.csv).

### Étape 4 - Traitement

Si un avis public n'apparaît qu'une fois dans les fichiers .xml, son traitement est relativement simple et il est assuré par le script [**univ-nb1.py**](univ-nb1.py). C'est le cas de près de 63% des avis publics publiés dans le SÉAO.

Si un avis public apparaît deux fois, son traitement est assuré par le script [**univ-nb2.py**](univ-nb2.py). Ici, il s'agit de vérifier si la 2e fois qu'on trouve un même nom d'avis SÉAO, s'il s'agit d'une information relative à un contrat ou à une dépense (on reste alors avec le même contrat), ou s'il s'agit d'un 2e avis (il peut arriver qu'un même avis public donne lieu à deux contrats). Près de 33% des avis apparaissent deux fois dans le SÉAO.

Si un avis public apparaît trois fois, son traitement est assuré par le script [**univ-nb3.py**](univ-nb3.py). Ici, ça se complique. On peut être en présence d'un avis ayant donné lieu à un seul contrat, à deux ou à trois contrats. Il faut effectuer toutes ces vérifications. Près de 2,7% de l'ensemble des avis publics apparaissent trois fois dans le SÉAO.

Enfin pour le 1,95% des avis qui apparaissent quatre fois ou plus (certains apparissent [jusqu'à 284 fois](http://www.seao.ca/Recherche/adjudication.aspx?ItemId=e221b62a-8069-490c-af39-2590acea92f1&returnto=%2FOpportunityPublication%2FConsulterAvis%2FRecherche%3FItemId=e221b62a-8069-490c-af39-2590acea92f1%26callingPage=2%26searchId=18c1c6a2-6288-4bd3-a76d-aa06018599f0%26VPos=0&menu=&SubCategoryCode=&callingPage=2&searchId=18c1c6a2-6288-4bd3-a76d-aa06018599f0&Level2=AdjResults))

Enfin, si un avis public apparaît

On constate que près de 63% des avis publics n'apparaissent qu'une fois et que près de 33% apparaissent deux fois. Seulement 4,6% des avis publics apparaissent trois fois ou plus dans les fichiers .xml, mais ce sont tous ces cas qui sont les plus difficiles à traiter.
