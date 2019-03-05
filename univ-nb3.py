# ©2019 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv

fichierNb = "decompte-des-numeros-seao.csv"
fichierInput = "seao_2009-2018-nb3.csv"
fichierOutput = "contrats-nb3.csv"

f1 = open(fichierNb)
numeros = csv.reader(f1)
next(numeros)

for numero in numeros:
	if numero[1] == "3":
		montantAvis = 0
		montantAvisRevise = 0
		montantContrat = 0
		montantContratRevise = 0
		montantDepense = 0
		montantDepenseRevise = 0
		montantFinal = 0
		print("="*80)
		print(numero)
		trois = []

		f2 = open(fichierInput)
		contrats = csv.reader(f2)

		for contrat in contrats:
			if contrat[2] == numero[0]:
				trois.append(contrat)

		print(trois)
		print(len(trois))
		print("."*10)
		# print(trois[0][0],trois[1][0],trois[2][0])

		if "Avis_" in trois[0][1] and "Avis_" in trois[1][1] and "Avis_" in trois[2][1]:
			nb = 0
			for avis in trois:
				nb += 1
				montantAvis = float(avis[-1])
				montantFinal = montantAvis
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

		elif trois[0][9] == trois[1][9] == trois[2][9]:
			for avis in trois:
				if "Avis_" in avis[1]:
					montantAvis = float(avis[-1])
				elif "AvisRevisions_" in avis[1]:
					montantAvisRevise = float(avis[-1])
				elif "Contrats_" in avis[1]:
					montantContrat = float(avis[-1])
				elif "ContratsRevisions_" in avis[1]:
					montantContratRevise = float(avis[-1])
				elif "Depenses_" in avis[1]:
					montantDepense += float(avis[-1])
				elif "DepensesRevisions_" in avis[1]:
					montantDepenseRevise += float(avis[-1])

			if montantContratRevise > 0:
				if montantDepense > 0:
					montantFinal = montantContratRevise + montantDepense
				else:
					montantFinal = montantContratRevise + montantDepenseRevise
			elif montantContrat > 0:
				if montantDepense > 0:
					montantFinal = montantContrat + montantDepense
				else:
					montantFinal = montantContrat + montantDepenseRevise
			elif montantAvisRevise > 0:
				if montantDepense > 0:
					montantFinal = montantAvisRevise + montantDepense
				else:
					montantFinal = montantAvisRevise + montantDepenseRevise
			else:
				if montantDepense > 0:
					montantFinal = montantAvis + montantDepense
				else:
					montantFinal = montantAvis + montantDepenseRevise

			out = [
				trois[0][2],
				trois[0][3],
				trois[0][4],
				trois[0][5],
				trois[0][6],
				trois[0][7],
				trois[0][8],
				trois[0][9],
				trois[0][10],
				trois[0][11],
				trois[0][12],
				trois[0][13],
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

		else:
			print("Problème...")
			print(0,trois[0][9],trois[0])
			print(1,trois[1][9],trois[1])
			print(2,trois[2][9],trois[2])
			nbEntreprises = input("Combien d'entreprises (1 ou 2)? ")
			if int(nbEntreprises) == 1:
				for avis in trois:
					if "Avis_" in avis[1]:
						montantAvis = float(avis[-1])
						fournisseurNom = avis[9]
						fournisseurVille = avis[10]
						fournisseurProv = avis[11]
						fournisseurPays = avis[12]
						fournisseurNEQ = avis[13]
					elif "AvisRevisions_" in avis[1]:
						montantAvisRevise = float(avis[-1])
						fournisseurNom = avis[9]
						fournisseurVille = avis[10]
						fournisseurProv = avis[11]
						fournisseurPays = avis[12]
						fournisseurNEQ = avis[13]
					elif "Contrats_" in avis[1]:
						montantContrat = float(avis[-1])
					elif "ContratsRevisions_" in avis[1]:
						montantContratRevise = float(avis[-1])
					elif "Depenses_" in avis[1]:
						montantDepense += float(avis[-1])
					elif "DepensesRevisions_" in avis[1]:
						montantDepenseRevise += float(avis[-1])

				if montantContratRevise > 0:
					if montantDepense > 0:
						montantFinal = montantContratRevise + montantDepense
					else:
						montantFinal = montantContratRevise + montantDepenseRevise
				elif montantContrat > 0:
					if montantDepense > 0:
						montantFinal = montantContrat + montantDepense
					else:
						montantFinal = montantContrat + montantDepenseRevise
				elif montantAvisRevise > 0:
					if montantDepense > 0:
						montantFinal = montantAvisRevise + montantDepense
					else:
						montantFinal = montantAvisRevise + montantDepenseRevise
				else:
					if montantDepense > 0:
						montantFinal = montantAvis + montantDepense
					else:
						montantFinal = montantAvis + montantDepenseRevise

				out = [
					trois[0][2],
					trois[0][3],
					trois[0][4],
					trois[0][5],
					trois[0][6],
					trois[0][7],
					trois[0][8],
					fournisseurNom,
					fournisseurVille,
					fournisseurProv,
					fournisseurPays,
					fournisseurNEQ,
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

			else:
				ent1 = int(input("L'entreprise qui a 2 infos est dans item 0, 1 ou 2? "))
				ent2 = int(input("L'autre est dans item 0, 1 ou 2? "))
				q1 = int(input("Les infos supp. sont dans quel item (0, 1 ou 2)? "))

				if "Avis_" in trois[ent1][1]:
					montantAvis = float(trois[ent1][-1])
				elif "AvisRevisions_" in trois[ent1][1]:
					montantAvisRevise = float(trois[ent1][-1])

				if "Contrats_" in trois[q1][1]:
					montantContrat = float(trois[q1][-1])
					montantFinal = montantContrat
				elif "ContratsRevisions_" in trois[q1][1]:
					montantContratRevise = float(trois[q1][-1])
					montantFinal = montantContratRevise

				elif "Depenses_" in trois[q1][1]:
					montantDepense = float(trois[q1][-1])
					if "Avis_" in trois[ent1][1]:
						montantFinal = montantAvis + montantDepense
					elif "AvisRevisions_" in trois[ent1][1]:
						montantFinal = montantAvisRevise + montantDepense
				elif "DepensesRevisions_" in trois[q1][1]:
					montantDepenseRevise = trois[q1][-1]
					if "Avis_" in trois[ent1][1]:
						montantFinal = montantAvis + montantDepenseRevise
					elif "AvisRevisions_" in trois[ent1][1]:
						montantFinal = montantAvisRevise + montantDepenseRevise
				else:
					# print(deux)
					input("Problème")

				out = [
					trois[ent1][2] + "-001",
					trois[ent1][3],
					trois[ent1][4],
					trois[ent1][5],
					trois[ent1][6],
					trois[ent1][7],
					trois[ent1][8],
					trois[ent1][9],
					trois[ent1][10],
					trois[ent1][11],
					trois[ent1][12],
					trois[ent1][13],
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

				montantAvis = 0
				montantAvisRevise = 0
				montantContrat = 0
				montantContratRevise = 0
				montantDepense = 0
				montantDepenseRevise = 0
				montantFinal = 0
				if "Avis_" in trois[ent2][1]:
					montantAvis = trois[ent2][-1]
				elif "AvisRevisions_" in trois[ent2][1]:
					montantAvisRevise = trois[ent2][-1]
				elif "Contrats_" in trois[ent2][1]:
					montantContrat = trois[ent2][-1]
				elif "ContratsRevisions_" in trois[ent2][1]:
					montantContratRevise = trois[ent2][-1]
				elif "Depenses_" in trois[ent2][1]:
					montantDepense = trois[ent2][-1]
				elif "DepensesRevisions_" in trois[ent2][1]:
					montantDepenseRevise = trois[ent2][-1]

				out = [
					trois[ent2][2] + "-002",
					trois[ent2][3],
					trois[ent2][4],
					trois[ent2][5],
					trois[ent2][6],
					trois[ent2][7],
					trois[ent2][8],
					trois[ent2][9],
					trois[ent2][10],
					trois[ent2][11],
					trois[ent2][12],
					trois[ent2][13],
					montantAvis,
					montantAvisRevise,
					montantContrat,
					montantContratRevise,
					montantDepense,
					montantDepenseRevise,
					trois[ent2][-1]
					]
				print(out)
				print("-"*60)

				douglas = open(fichierOutput, "a")
				coupland = csv.writer(douglas)
				coupland.writerow(out)
