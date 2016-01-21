#-*- coding: utf-8 -*-

# quantidade de entradas e de saidas da RNA
qntNeuroniosEntrada  = 80
qntNeuroniosSaida    = 1

# nome dos arquivos de treino e de testes
nomeArqTeste     = 'entradas/testes.fann'
nomeArqTreino    = 'entradas/treino.fann'
nomeArqValidacao = 'entradas/validacao.fann'

logFile = 'Execucao_Alg_Gen.log'

# porcentagem de padroes utilizados no treino
# utilizado no separarEntradas.py
porcTreino = 2.0/3.0

# Tamanho da populacao inicial de indivíduos
populacaoInicial = 150

# Criterio de parada
criterioSatisfacao = 0.0001

# Maximo de Geracoes do Algoritmo Genetico
maximoGeracoes=50

dirSaveRNAs = 'Redes_Geradas'

nodes = ['192.168.36.78', '192.168.36.79', '192.168.36.80', '192.168.36.139', '192.168.36.43', '192.168.36.121', '192.168.36.39', '192.168.36.103', '192.168.36.201']
