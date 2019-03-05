# ©2019 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv

fichierNb = "decompte-des-numeros-seao-nb4plus.csv"
fichierInput = "seao_2009-2018-nb4plus.csv"
fichierOutput = "contrats-nb4plus.csv"

f1 = open(fichierNb)
numeros = csv.reader(f1)
next(numeros)

for numero in numeros:
	if int(numero[1]) >= 3:
		montantAvis = 0
		montantAvisRevise = 0
		montantContrat = 0
		montantContratRevise = 0
		montantDepense = 0
		montantDepenseRevise = 0
		montantFinal = 0
		nbAvis = 0
		nbAvisRevise = 0
		nbContrat = 0
		nbContratRevise = 0
		nbDepense = 0
		nbDepenseRevise = 0
		print("="*80)
		print(numero)
		quatrePlus = []

		f2 = open(fichierInput)
		contrats = csv.reader(f2)

		for contrat in contrats:
			if contrat[2] == numero[0]:
				quatrePlus.append(contrat)

		# print(quatrePlus)
		# print(len(quatrePlus))
		fournisseurs = []
		for i in range(0,len(quatrePlus)):
			fournisseurs.append(quatrePlus[i][9])
			if "Avis_" in quatrePlus[i][1]:
				nbAvis += 1
			elif "AvisRevisions_" in quatrePlus[i][1]:
				nbAvisRevise += 1
			elif "Contrats_" in quatrePlus[i][1]:
				nbContrat += 1
			elif "ContratsRevisions_" in quatrePlus[i][1]:
				nbContratRevise += 1
			elif "Depenses_" in quatrePlus[i][1]:
				nbDepense += 1
			elif "DepensesRevisions_" in quatrePlus[i][1]:
				nbDepenseRevise += 1
		fournisseurs = set(fournisseurs)

		print(str(nbAvis) + " avis")
		print(str(nbAvisRevise) + " avis révisés")
		print(str(nbContrat) + " contrats")
		print(str(nbContratRevise) + " contrats révisés")
		print(str(nbDepense) + " dépenses")
		print(str(nbDepenseRevise) + " dépenses révisées")
		print("Pour " + str(len(fournisseurs)) + " fournisseurs différents dans " + str(len(quatrePlus)))
		print("~"*20)

		if nbAvis != 0 or nbAvisRevise != 0:
			if len(fournisseurs) == 1 and nbAvis != 1: # Pour les cas à 4 avis (nb4)
				print(quatrePlus)
				nbCont = input("Combien de contrats? ")
				if int(nbCont) == 2:
					for k in [0,1]:
						out = [
							quatrePlus[k][2] + "-00{}".format(str(k)),
							quatrePlus[k][3],
							quatrePlus[k][4],
							quatrePlus[k][5],
							quatrePlus[k][6],
							quatrePlus[k][7],
							quatrePlus[k][8],
							quatrePlus[k][9],
							quatrePlus[k][10],
							quatrePlus[k][11],
							quatrePlus[k][12],
							quatrePlus[k][13],
							quatrePlus[k][-1],
							0,
							quatrePlus[k+2][-1],
							0,
							0,
							0,
							quatrePlus[k][-1]
							]
						print(out)
						print("-"*60)

						douglas = open(fichierOutput, "a")
						coupland = csv.writer(douglas)
						coupland.writerow(out)

			elif len(fournisseurs) == 1:
				for avis in quatrePlus:
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
					if montantDepenseRevise > 0:
						montantFinal = montantContratRevise + montantDepenseRevise
					else:
						montantFinal = montantContratRevise + montantDepense
				elif montantContrat > 0:
					if montantDepenseRevise > 0:
						montantFinal = montantContrat + montantDepenseRevise
					else:
						montantFinal = montantContrat + montantDepense
				elif montantAvisRevise > 0:
					if montantDepenseRevise > 0:
						montantFinal = montantAvisRevise + montantDepenseRevise
					else:
						montantFinal = montantAvisRevise + montantDepense
				else:
					if montantDepenseRevise > 0:
						montantFinal = montantAvis + montantDepenseRevise
					else:
						montantFinal = montantAvis + montantDepense

				out = [
					quatrePlus[0][2],
					quatrePlus[0][3],
					quatrePlus[0][4],
					quatrePlus[0][5],
					quatrePlus[0][6],
					quatrePlus[0][7],
					quatrePlus[0][8],
					quatrePlus[0][9],
					quatrePlus[0][10],
					quatrePlus[0][11],
					quatrePlus[0][12],
					quatrePlus[0][13],
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

			elif len(fournisseurs) == len(quatrePlus):
				for i in range(0,len(quatrePlus)):
					if i < 9:
						nb = "0{}".format(str(i+1))
					else:
						nb = str(i+1)
					if "Avis_" in quatrePlus[i][1]:
						montantAvis = float(quatrePlus[i][-1])
						montantFinal = montantAvis
					elif "AvisRevisions_" in quatrePlus[i][1]:
						montantAvisRevise = float(quatrePlus[i][-1])
						montantFinal = montantAvisRevise
					out = [
						quatrePlus[i][2] + "-" + nb,
						quatrePlus[i][3],
						quatrePlus[i][4],
						quatrePlus[i][5],
						quatrePlus[i][6],
						quatrePlus[i][7],
						quatrePlus[i][8],
						quatrePlus[i][9],
						quatrePlus[i][10],
						quatrePlus[i][11],
						quatrePlus[i][12],
						quatrePlus[i][13],
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
				if len(fournisseurs) >= nbAvis:
					neqs = []
					neqZero = 0
					for j in range(0,len(quatrePlus)):
						if quatrePlus[j][13] == "":
							neqZero += 1
						else:
							neqs.append(quatrePlus[j][13])
					neqs = set(neqs)
					nb = 0

					if neqZero == 0:
						print("   >>> NEQ <<<")
						for neq in neqs:
							print(neq)
							montantAvis = 0
							montantAvisRevise = 0
							montantContrat = 0
							montantContratRevise = 0
							montantDepense = 0
							montantDepenseRevise = 0
							montantFinal = 0
							# print("."*20)
							nb += 1
							for avis in quatrePlus:
								# print(avis)
								if neq == avis[13]:
									if nb < 10:
										nbnb = "-0{}".format(str(nb))
									else:
										nbnb = "-{}".format(str(nb))
									# print(avis)
									# print("."*20)
									
									if "Avis_" in avis[1]:
										numSeao = avis[2] + nbnb
										numContrat = avis[3]
										org = avis[4]
										desc = avis[5]
										cat = avis[6]
										unspsc = avis[7]
										date = avis[8]
										fournisseurNom = avis[9]
										fournisseurVille = avis[10]
										fournisseurProv = avis[11]
										fournisseurPays = avis[12]
										montantAvis = float(avis[-1])
									elif "AvisRevisions_" in avis[1]:
										numSeao = avis[2] + nbnb
										numContrat = avis[3]
										org = avis[4]
										desc = avis[5]
										cat = avis[6]
										unspsc = avis[7]
										date = avis[8]
										fournisseurNom = avis[9]
										fournisseurVille = avis[10]
										fournisseurProv = avis[11]
										fournisseurPays = avis[12]
										montantAvisRevise = float(avis[-1])
									elif "Contrats_" in avis[1]:
										montantContrat = float(avis[-1])
									elif "ContratsRevisions_" in avis[1]:
										montantContratRevise = float(avis[-1])
									elif "Depenses_" in avis[1]:
										montantDepense += float(avis[-1])
									elif "DepensesRevisions_" in avis[1]:
										montantDepenseRevise = float(avis[-1])
	
								if montantContratRevise > 0:
									if montantDepenseRevise > 0:
										montantFinal = montantContratRevise + montantDepenseRevise
									else:
										montantFinal = montantContratRevise + montantDepense
								elif montantContrat > 0:
									if montantDepenseRevise > 0:
										montantFinal = montantContrat + montantDepenseRevise
									else:
										montantFinal = montantContrat + montantDepense
								elif montantAvisRevise > 0:
									if montantDepenseRevise > 0:
										montantFinal = montantAvisRevise + montantDepenseRevise
									else:
										montantFinal = montantAvisRevise + montantDepense
								else:
									if montantDepenseRevise > 0:
										montantFinal = montantAvis + montantDepenseRevise
									else:
										montantFinal = montantAvis + montantDepense
							out = [
								numSeao,
								numContrat,
								org,
								desc,
								cat,
								unspsc,
								date,
								fournisseurNom,
								fournisseurVille,
								fournisseurProv,
								fournisseurPays,
								neq,
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
						print("   >>> FOURNISSEUR <<<")
						for fournisseur in fournisseurs:
							montantAvis = 0
							montantAvisRevise = 0
							montantContrat = 0
							montantContratRevise = 0
							montantDepense = 0
							montantDepenseRevise = 0
							montantFinal = 0
							nb += 1
							for avis in quatrePlus:
								# print(avis)
								if fournisseur == avis[9]:
									if nb < 10:
										nbnb = "-0{}".format(str(nb))
									else:
										nbnb = "-{}".format(str(nb))

									# print(avis)
									# print("."*20)
									
									if "Avis_" in avis[1]:
										numSeao = avis[2] + nbnb
										numContrat = avis[3]
										org = avis[4]
										desc = avis[5]
										cat = avis[6]
										unspsc = avis[7]
										date = avis[8]
										fournisseurVille = avis[10]
										fournisseurProv = avis[11]
										fournisseurPays = avis[12]
										fournisseurNEQ = avis[13]
										montantAvis = float(avis[-1])
									elif "AvisRevisions_" in avis[1]:
										numSeao = avis[2] + nbnb
										numContrat = avis[3]
										org = avis[4]
										desc = avis[5]
										cat = avis[6]
										unspsc = avis[7]
										date = avis[8]
										fournisseurVille = avis[10]
										fournisseurProv = avis[11]
										fournisseurPays = avis[12]
										fournisseurNEQ = avis[13]
										montantAvisRevise = float(avis[-1])
									elif "Contrats_" in avis[1]:
										montantContrat = float(avis[-1])
									elif "ContratsRevisions_" in avis[1]:
										montantContratRevise = float(avis[-1])
									elif "Depenses_" in avis[1]:
										montantDepense += float(avis[-1])
									elif "DepensesRevisions_" in avis[1]:
										montantDepenseRevise = float(avis[-1])
									
								if montantContratRevise > 0:
									if montantDepenseRevise > 0:
										montantFinal = montantContratRevise + montantDepenseRevise
									else:
										montantFinal = montantContratRevise + montantDepense
								elif montantContrat > 0:
									if montantDepenseRevise > 0:
										montantFinal = montantContrat + montantDepenseRevise
									else:
										montantFinal = montantContrat + montantDepense
								elif montantAvisRevise > 0:
									if montantDepenseRevise > 0:
										montantFinal = montantAvisRevise + montantDepenseRevise
									else:
										montantFinal = montantAvisRevise + montantDepense
								else:
									if montantDepenseRevise > 0:
										montantFinal = montantAvis + montantDepenseRevise
									else:
										montantFinal = montantAvis + montantDepense
							out = [
								numSeao,
								numContrat,
								org,
								desc,
								cat,
								unspsc,
								date,
								fournisseur,
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

				elif nbAvis == len(quatrePlus):
					for i in range(0,len(quatrePlus)):
						if i < 9:
							nb = "0{}".format(str(i+1))
						else:
							nb = str(i+1)
						if "Avis_" in quatrePlus[i][1]:
							montantAvis = float(quatrePlus[i][-1])
							montantFinal = montantAvis
						elif "AvisRevisions_" in quatrePlus[i][1]:
							montantAvisRevise = float(quatrePlus[i][-1])
							montantFinal = montantAvisRevise
						out = [
							quatrePlus[i][2] + "-" + nb,
							quatrePlus[i][3],
							quatrePlus[i][4],
							quatrePlus[i][5],
							quatrePlus[i][6],
							quatrePlus[i][7],
							quatrePlus[i][8],
							quatrePlus[i][9],
							quatrePlus[i][10],
							quatrePlus[i][11],
							quatrePlus[i][12],
							quatrePlus[i][13],
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
					input("Cas particulier -> à remplir manuellement")

