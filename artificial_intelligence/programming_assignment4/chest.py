import time

from baysnet import *

node = BayesNode

T, F = True, False

chestClinic = BayesNet([
	node('VisitToAsia', '', .99),
	node('Smoking', '', .50)
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
	node('Dyspnea', 'TuberculosisOrLungCancer Bronchitis' {
		(T, T):.9,
		(T, F):.7,
		(F, T):.8,
		(F, F):.1
		})
	])