#!/usr/bin/env python

from config import dirSaveRNAs, nomeArqTreino, nomeArqValidacao, \
                   qntNeuroniosEntrada, qntNeuroniosSaida,       \
                   criterioSatisfacao as desiredError

filename = 'Avaliador_Fann.h'

header = '''
#define dirSaveRNAs      "%s"
#define nomeArqTreino    "%s"
#define nomeArqValidacao "%s"
#define qntNeuroniosEntrada %d
#define qntNeuroniosSaida   %d
#define desiredError        %f
''' % (dirSaveRNAs, nomeArqTreino, nomeArqValidacao, qntNeuroniosEntrada, qntNeuroniosSaida, desiredError)

open(filename, 'w').writelines(header)
print "`%s' created." % filename
