Prédictions autour des données de recensement
=====

Le but est de prédire le niveau de revenu d'une personne *(si la personne gagne plus de $50k ou pas)* à partir d'autres données sur celle-ci.


La démarche suivie ainsi que les étapes seront explicitées ci dessous:

+ A première vue, après avoir regardé les données juste question d'avoir une intuition sur celles-ci, plusieurs facteurs paraissent pouvoir agir sur le revenu tel que l'age, l'éducation etc. 

+ Après avoir chargé les données, juste par curiosité j'ai essayé de visulasier l'influence de l'age sur le revenu, mais celle ci ne paraissait pas avoir une influence vu les distributions des ages chez les personnes gagnants plus de $50k et celles gagnant moins. Mais celà bien sûr ne suffit pas pour conclure et faire celà pour toutes les caractéristiques pourrait prendre du temps. Il faut choisir les caractéristiques les plus significatives *(feature selection)* .
 
+ Choisir les bonnes caractéristiques va permettre de réduire les dimension et d'enlever les caractéristiques non significatives. Petit problème, les données ne sont pas toutes numérique (des fonctions telles que matplotlib.pyplot ne fonctionnent pas sur les str par exemple), il va falloire transformer les données avant. J'ai essayé de faire un mapping (voir la fonction data_to_numbers) avec. 
- Remarque: la fonction deep_copy crée une copie de l'objet pandas.DataFrame (ce n'est pas une simple référence à l'objet, mais un objet différent avec les mêmes valeurs d'attributs)

+ Je n'ai pas réussi à calculer la variance pour les différentes caractéristique afin de me baser sur un seuil de variance.

+ J'ai ensuite opté pour l'utilisation de l'algorithme Random Forest (le choix des sous-ensembles parmis les caractéristique est effectué aussi). L'algorithme réussi bien à classifier les personnes ayant plus ou moins de $50k.

Exemples de résultats obtenus:
----
0: -50000$
1: +50000$

```
  >> RESULTS
   > Training data fitting:
Predicted       0      1
Real                    
0          187141      0
1               0  12382
   > Test data fitting:
Predicted      0     1
Real                  
0          93576     0
1              0  6186
```
```
  >> RESULTS
   > Training data fitting:
Predicted       0      1
Real                    
0          187141      0
1               0  12382
   > Test data fitting:
Predicted      0     1
Real                  
0          93576     0
1             92  6094
```




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Les données ont été extrates de la "census bureau database" trouvée à:
| http://www.census.gov/ftp/pub/DES/www/welcome.html
| Donor: Terran Lane and Ronny Kohavi
|        Data Mining and Visualization
|        Silicon Graphics.
|        e-mail: terran@ecn.purdue.edu, ronnyk@sgi.com for questions.
