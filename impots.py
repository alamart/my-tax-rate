#!/usr/bin/env python 

import matplotlib.pyplot as plt
import sys, getopt
import argparse


def calcul_by_tranche(somme, tranches=[], taux=[]):
	tax = 0
	if somme < tranches[0]:
		return 0, 0
	else:
		tranche_somme = somme - tranches[0]
		if tranche_somme < (tranches[1]-tranches[0]):
			tax += tranche_somme * taux[0]
			return tax, tax/somme
		else:
			tax += (tranches[1]-tranches[0]) * taux[0]
			tranche_somme = somme - tranches[1]
			if tranche_somme < (tranches[2]-tranches[1]):
				tax += tranche_somme * taux[1]
				return tax, tax/somme
			else:
				tax += (tranches[2]-tranches[1]) * taux[1]
				tranche_somme = somme - tranches[2]
				if tranche_somme < (tranches[3]-tranches[2]):
					tax += tranche_somme * taux[2]
					return tax, tax/somme
				else:
					tax += (tranches[3]-tranches[2]) * taux[2]
					tranche_somme = somme - tranches[3]
					tax += tranche_somme * taux[3]
					return tax, tax/somme

def main(args):
	try:
		optlist, args = getopt.getopt(args, 'bprs')
		optlist = dict(optlist)
	except Exception as e:
		raise e
	print(optlist)

	salary_rate = 1
	denom = 1
	show_rate = '-r' in optlist
	salary = '-s' in optlist 
	if '-b' in optlist:
		salary_rate = 0.75
	
	if '-p' in optlist:
		denom = 12
	
	pays = range(0, 100000, 100)
	tranches = [9964, 27519, 73779, 156244]
	taux = [0.14, 0.30, 0.41, 0.45]

	fig, ax1 = plt.subplots()
	color = 'tab:red'

	if salary_rate==0.75:
		type_salary = "brut"
	else:
		type_salary = "net"
	if denom == 12:
		periodicity = "mensuel"
	else:
		periodicity = "annuel"
	ax1.set_xlabel('Revenu annuel {}'.format(type_salary))
	if salary == True:
		ax1.set_ylabel('Vrai Salaire {} net'.format(periodicity), color=color)
		ax1.plot(pays, list(map(lambda somme : (somme * salary_rate - calcul_by_tranche(somme * salary_rate, tranches, taux)[0])/denom, pays)), color=color)
	else:
		ax1.set_ylabel('Impots {}'.format(periodicity), color=color)
		ax1.plot(pays, list(map(lambda somme : calcul_by_tranche(somme * salary_rate, tranches, taux)[0]/denom, pays)), color=color)

	if show_rate==True:
		color = 'tab:blue'
		ax2 = ax1.twinx()
		ax2.set_ylabel("Taux d'imposition", color=color)
		ax2.plot(pays, list(map(lambda somme : calcul_by_tranche(somme * salary_rate, tranches, taux)[1], pays)), color=color)

	fig.tight_layout()
	plt.show()

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "-h":
		parser=argparse.ArgumentParser(
		description='''Calculate your tax rate in France''',
		epilog="""All's well that ends well.""")
		parser.add_argument('-b', help='Get the tax from the "BRUT" salary')
		parser.add_argument('-p', help='Get the "NET" salary you get after tax or tax rate monthly')
		parser.add_argument('-r', help='Show the tax rate according to your salary')
		parser.add_argument('-s', help='Get the true "NET" month salary you get after tax')
		args=parser.parse_args()
	else:
		main(sys.argv[1:])