
<br />
<div align="center">
  

  <h3 align="center">Loggin API</h3>

  <p align="center">
    API de production journal d'erreur </p>
    
    

</div>


<!-- À propos -->
## À propos

Cette API reçoit des requêtes dont le contenu est sous le format application x-www-form-urlencoded.

Les logs d'erreur sont ajoutés en texte brut au fichier de sortie.



<!-- Instructions -->
## Instructions

Valeurs par défaut :
* Port : 5000
* Fichier de sortie : log.txt

Une configuration peut-être spécifiée par les arguments. 

Exemple :
   ```sh
   python logging_api.py 5100 nouveau_log.txt
   ```




