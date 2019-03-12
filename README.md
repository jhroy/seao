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

Si un avis public apparaît trois fois, son traitement est assuré par le script [**univ-nb3.py**](univ-nb3.py). Ici, ça se complique. On peut être en présence d'un avis ayant donné lieu à un seul contrat, à deux ou à trois contrats. Il faut effectuer toutes ces vérifications et vérifier aussi si les informations relatives à un même avis public ont fait l'objet de mises à jour dans le fichier «&nbsp;contrats&nbsp;» et/ou «&nbsp;dépenses&nbsp;» du SÉAO. Près de 2,7% de l'ensemble des avis publics apparaissent trois fois dans le SÉAO.

Il reste enfin 1,95% des avis qui apparaissent quatre fois ou plus (certains apparissent [jusqu'à 284 fois](http://www.seao.ca/Recherche/adjudication.aspx?ItemId=e221b62a-8069-490c-af39-2590acea92f1&returnto=%2FOpportunityPublication%2FConsulterAvis%2FRecherche%3FItemId=e221b62a-8069-490c-af39-2590acea92f1%26callingPage=2%26searchId=18c1c6a2-6288-4bd3-a76d-aa06018599f0%26VPos=0&menu=&SubCategoryCode=&callingPage=2&searchId=18c1c6a2-6288-4bd3-a76d-aa06018599f0&Level2=AdjResults)). Leur traitement est assuré par le script [**univ-nb4plus.py**](univ-nb4plus.py) qui vérifie tous les cas de figure pouvant survenir.

Au final, chacun de ces quatre scripts produit un fichier .csv structuré de la même manière (exemple avec [**contrats-nb3.csv**](contrats-nb3.csv)). Il s'agit de les réunir tous les quatre, puis d'importer le tout dans MySQL pour faire des recherches. Au final, vous devriez obtenir un fichier .csv contenant 315&nbsp;817 lignes, chacune représentant un contrat octroyé par un organisme public entre 2009 et 2018.

### Étape 5 - Recherches dans MySQL

Si vous avez donné à votre table où se trouvent tous les contrats le nom de `contrats_final`, voici la requête à effectuer pour rechercher les contrats octroyés par les cégeps et universités à la société [Elsevier](https://www.elsevier.com/), par exemple.

```SQL
select organisme, count(organisme) as nbContrats, sum(montantTotal) as total
from contrats_final
WHERE
(fournisseur like '%elsevier%' OR
description like '%elsevier%')
AND
(organisme = 'Université McGill' OR
organisme = 'Université Laval' OR
organisme = 'Université du Québec en Outaouais' OR
organisme = 'Université du Québec de l\'Abitibi-Témiscamingue (UQAT)' OR
organisme = 'Université du Québec à Trois-Rivières' OR
organisme = 'Université du Québec à Rimouski.' OR
organisme = 'Université du Québec à Montréal (SPI)' OR
organisme = 'Université du Québec à Montréal' OR
organisme = 'Université du Québec à Chicoutimi .' OR
organisme = 'Université du Québec (Siège social)' OR
organisme = 'Université de Sherbrooke -Service des ressources financières-  Section de l\'approvisionnement' OR
organisme = 'Université de Sherbrooke -Service des ressources financières-  Secteur approvisionnement' OR
organisme = 'Université de Montréal.' OR
organisme = 'Université de Montréal - Direction des immeubles' OR
organisme = 'Université Concordia' OR
organisme = 'Université Bishop\'s.' OR
organisme = 'Université Bishop\'s B&G' OR
organisme = 'Télé-université' OR
organisme = 'Institut national de la recherche scientifique (INRS)' OR
organisme = 'INRS-Service des ressources matérielles - Gestion de projets' OR
organisme = 'HEC Montréal' OR
organisme = 'École Polytechnique' OR
organisme = 'École nationale d\'administration publique.' OR
organisme = 'École de technologie supérieure' OR
organisme = 'Le Collège Montmorency' OR
organisme = 'Le Cégep Régional de Lanaudière' OR
organisme = 'Le Cégep Gérald-Godin' OR
organisme = 'Institut de tourisme et d\'hôtellerie du Québec' OR
organisme = 'Heritage College' OR
organisme = 'Collège Shawinigan.' OR
organisme = 'Collège Lionel-Groulx' OR
organisme = 'Collège John Abbott' OR
organisme = 'Collège De-Bois-De-Boulogne' OR
organisme = 'Collège de Valleyfield' OR
organisme = 'Collège de Rosemont.' OR
organisme = 'Collège de Maisonneuve' OR
organisme = 'Collège Dawson.' OR
organisme = 'Collège d\'Alma' OR
organisme = 'Collège Ahuntsic' OR
organisme = 'Champlain Regional College' OR
organisme = 'Cégep Vanier College.' OR
organisme = 'CÉGEP Sherbrooke' OR
organisme = 'CEGEP Saint-Jean-Sur-Richelieu' OR
organisme = 'Cégep Marie-Victorin' OR
organisme = 'Cégep Limoilou' OR
organisme = 'Cégep Garneau' OR
organisme = 'Cégep Édouard-Montpetit' OR
organisme = 'Cegep du Vieux-Montréal' OR
organisme = 'Cégep de Victoriaville.' OR
organisme = 'Cégep de Trois-Rivières.' OR
organisme = 'Cégep de Thetford.' OR
organisme = 'CEGEP de Ste-Foy' OR
organisme = 'Cégep de Sorel-Tracy.' OR
organisme = 'Cegep de Sept-Iles' OR
organisme = 'Cégep de Saint-Laurent.' OR
organisme = 'Cégep de Saint-Jérome.' OR
organisme = 'CEGEP de Saint-Hyacinthe' OR
organisme = 'Cégep de Saint-Félicien.' OR
organisme = 'Cégep de Rivière-du-Loup.' OR
organisme = 'Cégep de Rimouski' OR
organisme = 'Cégep de Matane.' OR
organisme = 'CEGEP de La Pocatière' OR
organisme = 'CEGEP de La Gaspésie et des Iles' OR
organisme = 'Cégep de l\'Outaouais...' OR
organisme = 'CÉGEP de Jonquière.' OR
organisme = 'Cégep de Granby' OR
organisme = 'Cégep de Drummondville.' OR
organisme = 'Cégep de Chicoutimi.' OR
organisme = 'Cégep de Baie-Comeau.' OR
organisme = 'Cégep Beauce-Appalaches.' OR
organisme = 'CÉGEP André Laurendeau' OR
organisme = 'Cégep Abitibi-Témiscamingue' OR
organisme = 'Cégep  Lévis-Lauzon')
group by organisme
order by total desc;
```

Je donne un exemple avec les cégeps et universités parce que ce travail d'analyse a été réalisé pour [*Découvrir*](https://www.acfas.ca/publications/decouvrir), la revue en ligne de l'Acfas, dans le cadre d'un dossier sur le coûts des licences logicielles et des abonnements à des revues académiques pour le système d'éducation supérieure québécois. À paraître bientôt.

Si vous souhaitez plonger dans les données de votre côté, le fichier [**contrats_univ_cegeps_2009-2018.csv**](contrats_univ_cegeps_2009-2018.csv) contient les quelque 38nbsp;771 contrats octroyés par les cégeps et universités du Québec entre 2009 et 2018.
