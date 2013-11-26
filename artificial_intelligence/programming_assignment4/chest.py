##########################################
#
# Jiaqi Wu
# MSCS 5600 Programming Assignment 4
#
# Chest Clinic Test Cases
#
# chest.py
#
##########################################

import time

from bayesnet import *

chestClinic = BayesNet([
	node('VisitToAsia', '', .99),
	node('Smoking', '', .50),
	node('Tuberculosis', 'VisitToAsia', {(T,):.05, (F,):.01}),
	node('LungCancer', 'Smoking', {(T,):.9, (F,):.01}),
	node('Bronchitis', 'Smoking', {(T,):.6, (F,):.3}),
	node('TuberculosisOrLungCancer', 'Tuberculosis LungCancer', {
		(T, T):1.0,
		(T, F):1.0,
		(F, T):1.0,
		(F, F):0.0
		}),
	node('XRayResult', 'TuberculosisOrLungCancer', {(T,):.95, (F,):.02}),
	node('Dyspnea', 'TuberculosisOrLungCancer Bronchitis', {
		(T, T):.9,
		(T, F):.7,
		(F, T):.8,
		(F, F):.1
		})
	])

class Test:
	def __init__(self, name, conditions, bn, samples):
		self.name = name
		self.e = conditions
		self.bn = bn
		self.samples = samples

s = [100, 2500, 100000]
tests = []
tests.append(Test('XRayResult', {'Smoking': T}, chestClinic, s))
tests.append(Test('XRayResult', {'Smoking': F, 'VisitToAsia': T}, chestClinic, s))
tests.append(Test('XRayResult', {'Smoking': F}, chestClinic, s))
tests.append(Test('XRayResult', {'LungCancer': T, 'Tuberculosis': T}, chestClinic, s))
tests.append(Test('Dyspnea', {'Smoking': T, 'LungCancer':T}, chestClinic, s))
tests.append(Test('Dyspnea', {'Smoking': F}, chestClinic, s))
tests.append(Test('Dyspnea', {'Bronchitis': T}, chestClinic, s))
tests.append(Test('Dyspnea', {'LungCancer': T, 'VisitToAsia': T}, chestClinic, s))
tests.append(Test('TuberculosisOrLungCancer', {'Smoking': T, 'LungCancer': T}, chestClinic, s))
tests.append(Test('Bronchitis', {'Smoking': T, 'Tuberculosis': T}, chestClinic, s))

f = open('ChestClinicResults.csv', 'w')

for test in tests:
	testTitle = 'P(' + test.name + ' | '
	for cond in test.e.keys():
		testTitle += cond + ' = ' + str(test.e[cond]) + ' '
	testTitle += ')'
	f.write(testTitle)
	f.write(',')
	for n in test.samples:
		sample = rejection_sampling(test.name, test.e, test.bn, n)
		f.write(str(sample[T]))
		f.write(',')
	f.write('\n')
	

f.close()