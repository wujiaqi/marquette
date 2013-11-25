import time

from bayesnet import *

wetGrass = BayesNet([
	node('Cloudy', '', .5),
	node('Sprinkler', 'Cloudy', {(T,):.10, (F,):.50}),
	node('Rain', 'Cloudy', {(T,):.99, (F,):.90}),
	node('WetGrass', 'Sprinkler Rain', {
		(T, T):.99,
		(T, F):.90,
		(F, T):.90,
		(F, F):.00})
	])

e = {'Sprinkler': F}

f = open('rain_test.csv', 'w')

for i in xrange(10, 1010, 10):
	f.write(str(i))
	f.write(',')
	startTime = time.time()
	sample = rejection_sampling('Rain', e, wetGrass, i)
	stopTime = time.time()
	f.write(str(sample[True]))
	f.write(',')
	f.write(str((stopTime - startTime)*1000))
	f.write('\n')

f.close()
