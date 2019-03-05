# ©2019 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv

fichierNb = "decompte-des-numeros-seao-nb2.csv"
fichierInput = "seao_2009-2018-nb2.csv"
fichierOutput = "contrats-nb2.csv"

f1 = open(fichierNb)
numeros = csv.reader(f1)
next(numeros)

for numero in numeros:
	if numero[1] == "2":
		montantAvis = 0
		montantAvisRevise = 0
		montantContrat = 0
		montantContratRevise = 0
		montantDepense = 0
		montantDepenseRevise = 0
		montantFinal = 0
		print("="*80)
		print(numero)
		deux = []

		f2 = open(fichierInput)
		contrats = csv.reader(f2)

		for contrat in contrats:
			if contrat[2] == numero[0]:
				deux.append(contrat)

		print(deux)
		print("."*10)
		# print(deux[0][13],deux[1][13])
		# print(deux[0][9],deux[1][9])
		# print("-"*80)

		if deux[0][0] == "Avis" and deux[1][0] == "Avis":
			if deux[0][9] == deux[1][9]:
				print("Problème")
			else:
				nb = 0
				for avis in deux:
					nb += 1
					if "Avis_" in avis[1]:
						montantAvis = float(avis[-1])
						montantFinal = montantAvis
					elif "AvisRevisions_" in avis[1]:
						montantAvisRevise = float(avis[-1])
						montantFinal = montantAvisRevise
					elif "Contrats_" in avis[1]:
						montantContrat = float(avis[-1])
						montantFinal = montantContrat
					out = [
						avis[2] + "-00" + str(nb),
						avis[3],
						avis[4],
						avis[5],
						avis[6],
						avis[7],
						avis[8],
						avis[9],
						avis[10],
						avis[11],
						avis[12],
						avis[13],
						montantAvis,
						montantAvisRevise,
						montantContrat,
						montantContratRevise,
						montantDepense,
						montantDepenseRevise,
						montantFinal
						]
					print(out)
					print("-"*60)

					douglas = open(fichierOutput, "a")
					coupland = csv.writer(douglas)
					coupland.writerow(out)

		elif deux[0][13] == deux[1][13] or deux[0][9] == deux[1][9]:
			# print(deux)
			# print("-"*80)

			if "Avis_" in deux[0][1]:
				montantAvis = float(deux[0][-1])
			elif "AvisRevisions_" in deux[0][1]:
				montantAvisRevise = float(deux[0][-1])

			if "Contrats_" in deux[1][1]:
				montantContrat = float(deux[1][-1])
				montantFinal = montantContrat
			elif "ContratsRevisions_" in deux[1][1]:
				montantContratRevise = float(deux[1][-1])
				montantFinal = montantContratRevise

			elif "Depenses_" in deux[1][1]:
				montantDepense = float(deux[1][-1])
				if "Avis_" in deux[0][1]:
					montantFinal = montantAvis + montantDepense
				elif "AvisRevisions_" in deux[0][1]:
					montantFinal = montantAvisRevise + montantDepense
			elif "DepensesRevisions_" in deux[1][1]:
				montantDepenseRevise = deux[1][-1]
				if "Avis_" in deux[0][1]:
					montantFinal = montantAvis + montantDepenseRevise
				elif "AvisRevisions_" in deux[0][1]:
					montantFinal = montantAvisRevise + montantDepenseRevise
			else:
				# print(deux)
				input("Problème")

			out = [
				deux[0][2],
				deux[0][3],
				deux[0][4],
				deux[0][5],
				deux[0][6],
				deux[0][7],
				deux[0][8],
				deux[0][9],
				deux[0][10],
				deux[0][11],
				deux[0][12],
				deux[0][13],
				montantAvis,
				montantAvisRevise,
				montantContrat,
				montantContratRevise,
				montantDepense,
				montantDepenseRevise,
				montantFinal
				]
			print(out)
			print("-"*60)

			douglas = open(fichierOutput, "a")
			coupland = csv.writer(douglas)
			coupland.writerow(out)