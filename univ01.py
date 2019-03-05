# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

###
### Ce premier script extrait les informations des fichiers XML

import csv, os, glob
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

donnees = "contrats.csv"

for dossier in os.walk("."):
	# print(dossier[0],len(dossier[2]))
	for fichier in dossier[2]:
		if ".xml" in fichier:
			nom = "{}/{}".format(dossier[0],fichier)
			print(nom,fichier[:4])

			if fichier[:4] == "Avis":
				bs = BeautifulSoup(open(nom),"xml")
				# print(bs)
				tousAvis = bs.find_all("avis")
				print(len(tousAvis))

				for avis in tousAvis:
					# print(avis.organisme.text)
					fournisseurs = avis.find("fournisseurs").find_all("fournisseur")
					x = 0
					for fournisseur in fournisseurs:
						if fournisseur.adjudicataire.text == "1":
							x += 1
							orgNom = avis.organisme.text
							numSEAO = avis.numeroseao.text
							numero = avis.numero.text
							titre = avis.titre.text
							categorie = avis.categorieseao.text
							unspsc = avis.unspscprincipale.text
							dateAdj = avis.dateadjudication.text
							try:
								dateDebut = datetime.strptime(dateAdj,"%Y-%m-%d")
								annee = dateDebut.year
								mois = dateDebut.month
								jour = dateDebut.day
							except:
								dateDebut = "0000-00-00 00:00:00"
								annee = ""
								mois = ""
								jour = ""
							# dateFerm = avis.datefermeture.text

							# try:
							# 	dateFin = datetime.strptime(dateFerm,"%Y-%m-%d %H:%M")
							# 	diff = (dateDebut - dateFin)
							# except:
							# 	dateFin = ""
							# 	diff = ""

							categorie = avis.categorieseao.text
							fournisseurNom = fournisseur.nomorganisation.text
							fournisseurVille = fournisseur.ville.text
							fournisseurProv = fournisseur.province.text
							fournisseurPays = fournisseur.pays.text
							fournisseurNEQ = fournisseur.neq.text
							montantContrat = float(fournisseur.montantcontrat.text)
							out = [
								"Avis",
								fichier,
								numSEAO,
								numero,
								orgNom,
								titre,
								categorie,
								unspsc,
								dateDebut,
								# annee,
								# mois,
								# jour,
								# dateFin,
								# diff,
								fournisseurNom,
								fournisseurVille,
								fournisseurProv,
								fournisseurPays,
								fournisseurNEQ,
								montantContrat
								]

							print("+"*10)
							print(out)

							douglas = open(donnees, "a")
							coupland = csv.writer(douglas)
							coupland.writerow(out)

			elif fichier[:4] == "Cont":
				bs = BeautifulSoup(open(nom),"xml")
				# print(bs)
				tousContrats = bs.find_all("contrat")
				print(len(tousContrats))
	
				for contrat in tousContrats:
					numSEAO = contrat.numeroseao.text
					numero = contrat.numero.text
					dateFinale = contrat.datefinale.text

					if dateFinale != "":
						dateFin = datetime.strptime(dateFinale,"%Y-%m-%d")
					else:
						dateFin = "0000-00-00 00:00:00"

					montantFinal = float(contrat.montantfinal.text)
					fournisseurNom = contrat.nomcontractant.text
					fournisseurNEQ = contrat.neqcontractant.text

					out = [
						"Contrats",
						fichier,
						numSEAO,
						numero,
						"",
						"",
						"",
						"",
						dateFin,
						# "",
						# "",
						# "",
						# "",
						# "",
						fournisseurNom,
						"",
						"",
						"",
						fournisseurNEQ,
						montantFinal
					]

					print("+"*10)
					print(out)

					douglas = open(donnees, "a")
					coupland = csv.writer(douglas)
					coupland.writerow(out)

			elif fichier[:4] == "Depe":
				bs = BeautifulSoup(open(nom),"xml")
				# print(bs)
				toutesDepenses = bs.find_all("depense")
				print(len(toutesDepenses))

				tousAvis = bs.find_all("avis")
				for avis in tousAvis:
					depenses = avis.find_all("depense")

					for depense in depenses:
						numSEAO = avis.numeroseao.text
						numero = avis.numero.text
						dateDepense = depense.datedepense.text

						if dateDepense != "":
							date = datetime.strptime(dateDepense,"%Y-%m-%d")
						else:
							date = "0000-00-00 00:00:00"

						montantDepense = float(depense.montantdepense.text)
						fournisseurNom = depense.nomcontractant.text
						fournisseurNEQ = depense.neqcontractant.text
						description = depense.description.text

						out = [
							"Dépenses",
							fichier,
							numSEAO,
							numero,
							"",
							description,
							"",
							"",
							date,
							# "",
							# "",
							# "",
							# "",
							# "",
							fournisseurNom,
							"",
							"",
							"",
							fournisseurNEQ,
							montantDepense
						]

						print("+"*10)
						print(out)

						douglas = open(donnees, "a")
						coupland = csv.writer(douglas)
						coupland.writerow(out)