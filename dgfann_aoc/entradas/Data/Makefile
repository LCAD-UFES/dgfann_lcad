

criarPadroesFANN: gerarTodosDados gerarEntrada
	./gerarEntrada todos_dados.txt 40 > todos_dados.fann

gerarTodosDados:
	bash -c 'grep STEERING results_pid/results_pid*txt > todos_dados.txt'
	if grep -q 'v,' todos_dados.txt;then touch velocity;else rm -f velocity;fi

gerarEntrada:
	if test -f velocity;then \
		gcc -o gerarEntrada gerarEntrada.c -D__VELOCITY; \
	else \
		gcc -o gerarEntrada gerarEntrada.c; \
	fi

clean:
	rm -f gerarEntrada todos_dados.fann todos_dados.txt velocity
