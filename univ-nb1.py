# ©2019 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv

fichierNb = "decompte-des-numeros-seao.csv"
fichierInput = "seao_2009-2018.csv"
fichierOutput = "contrats-nb1.csv"

f1 = open(fichierNb)
numeros = csv.reader(f1)
next(numeros)

un = []

for numero in numeros:
	if numero[1] == "1":
		un.append(numero[0])

f2 = open(fichierInput)
contrats = csv.reader(f2)

for contrat in contrats:
	if contrat[2] in un:
		# print(contrat)
		montantAvis = 0
		montantAvisRevise = 0
		montantContrat = 0
		montantContratRevise = 0
		montantDepense = 0
		montantDepenseRevise = 0
		fournisseurNom = ""
		# if contrat[0] == "Avis":
		# 	print(contrat[0],contrat[2],contrat[8],n)
		if "Avis_" in contrat[1]:
			montantAvis = contrat[-1]
		elif "AvisRevisions_" in contrat[1]:
			montantAvisRevise = contrat[-1]
		elif "Contrats_" in contrat[1]:
			montantContrat = contrat[-1]
		elif "ContratsRevisions_" in contrat[1]:
			montantContratRevise = contrat[-1]
		elif "Depenses_" in contrat[1]:
			montantDepense = contrat[-1]
		elif "DepensesRevisions_" in contrat[1]:
			montantDepenseRevise = contrat[-1]

		out = [
			contrat[2],
			contrat[3],
			contrat[4],
			contrat[5],
			contrat[6],
			contrat[7],
			contrat[8],
			contrat[9],
			contrat[10],
			contrat[11],
			contrat[12],
			contrat[13],
			montantAvis,
			montantAvisRevise,
			montantContrat,
			montantContratRevise,
			montantDepense,
			montantDepenseRevise,
			contrat[-1]
			]
		print(out)

		douglas = open(fichierOutput, "a")
		coupland = csv.writer(douglas)
		coupland.writerow(out)

