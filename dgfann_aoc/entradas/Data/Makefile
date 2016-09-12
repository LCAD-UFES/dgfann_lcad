

criarPadroesFANN: gerarTodosDados gerarEntrada
	./gerarEntrada todos_dados.txt 40 > todos_dados.fann

gerarTodosDados:
	bash -c 'cat results_pid/results_pid-steering-* > todos_dados.txt'

gerarEntrada: gerarEntrada.c

clean:
	rm -f gerarEntrada todos_dados.fann todos_dados.txt
