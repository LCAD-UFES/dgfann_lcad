#!/bin/bash

[ ! -d ../RNAs ] && {
    echo "ERRO: Não foi possível encontrar a pasta '../RNAs'"
    echo 'Execute o script 01-copiar_redes.sh ou verifique se está executando este script pasta principal.'
    exit 1
}


[ ! -f ./utils/teste_RNA_with_effort ] && make teste_RNA_with_effort

#PATTERNS_FILENAME='nomeArqTreino'
#PATTERNS_FILENAME='nomeArqValidacao'
PATTERNS_FILENAME='nomeArqTeste'
PATTERNS_FILE=$(python -c "from config import $PATTERNS_FILENAME;print $PATTERNS_FILENAME") 

DIR_OUTPUTS="results_${PATTERNS_FILENAME#nomeArq}-ann"
DIR_PLOTS="results_${PATTERNS_FILENAME#nomeArq}-plots"

echo "Using '$PATTERNS_FILE'. The results will be saved in folder '$DIR_OUTPUTS' and '$DIR_PLOTS'..."

mkdir -p $DIR_OUTPUTS $DIR_PLOTS

for i in ../RNAs/*;do
    N=`basename ${i}`
    N=${N%%-*}
    ./utils/teste_RNA_with_effort $i $PATTERNS_FILE > $DIR_OUTPUTS/teste_RNA-$N.txt
    for JUMP in 1 4 8;do
        ./utils/03-org_graph.py $JUMP $DIR_OUTPUTS/teste_RNA-${N}.txt $DIR_OUTPUTS/teste_RNA-${N}_${JUMP}.txt
        MSE=$(awk '{if ($5 == "Mean") print $NF}' $DIR_OUTPUTS/teste_RNA-${N}.txt)
        ARQ="$DIR_OUTPUTS/teste_RNA-${N}_${JUMP}.txt"
        echo "set term pngcairo font 'Times New Roman,18' size 1920,1280;
              set output '${DIR_PLOTS}/ANN_${N}_${JUMP}.png';
              set multiplot layout 2,1
              set title 'ANN (MSE: $MSE) $N 1/${JUMP}'
              set xlabel 'Samples'
              set ylabel 'Velocity and Error (m/s)'
              plot '$ARQ' using  2 title 'Estimated' with lines lc rgb '#ff0000', \
                   '$ARQ' using  4 title 'Desired' with lines lc rgb '#0000ff', \
                   '$ARQ' using  6 title 'Error' with lines lc rgb '#00ff00'
              unset title
              set xlabel 'Samples'
              set ylabel 'Trhottle and Brake Efforts'
              plot '$ARQ' using  8 title 'Throttle' with lines lc rgb '#e46c0a', \
                   '$ARQ' using 10 title 'Brake' with lines lc rgb '#555555'
             " | gnuplot
    done

done
