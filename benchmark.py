import os,time
tempoInicioBench = time.time()

# Configurações padrões
qtde = 50
printResult = False

# CARREGANDO CONFIGURAÇÕES
conf = open("benchmark.conf","r")
for linha in conf:
	linha = linha.strip()
	if "#" not in linha and linha != '':
		if 'PRINT_RESULT=' in linha:
			linha = linha.upper().replace('PRINT_RESULT=','')
			if linha == 'TRUE':
				printResult = True
			else:
				printResult = False
		if 'QNTD=' in linha:
			linha = linha.replace('QNTD=','')
			if linha.isnumeric():
				qtde = int(linha)
				
conf.close()

# Carregando ontologias
print("")
print("======================")
print("Ínicio do Benchmark")
print("Carregando informações do arquivo 'benchmark.conf'")
print("Quantidade total de execuções por linha e por motor: "+str(qtde))
print("")

conf = open("benchmark.conf","r")
for linha in conf:
	if "#" not in linha and 'BENCH_EXECUTE=' in linha:
		linha = linha.replace('BENCH_EXECUTE=','')
		command = linha.rstrip().split(",")
		command = " ".join(command)
		print("")
		print("=== Próxima Execução (Ontologia / Querys)")
		print(command)
		print("")
		print("==")
		print("WSML Engine")
		print("==")
		totalCarregarOntologia = 0
		totalConsulta = 0
		commandWsmlEngine = "python3 wsml-engine-bench.py " + str(command)
		for x in range(qtde):
			print("Loop "+str(x))
			result = os.popen(commandWsmlEngine).read()
			result = result.split('\n')
			for l in result:
				if 'Carregar Ontologia: ' in l:
					l = l.replace('Carregar Ontologia: ','')
					l = l[:-3]
					tempoCarregarOntologia = float(l)
					print("Ontologia: "+str(tempoCarregarOntologia))
					totalCarregarOntologia += tempoCarregarOntologia
				elif 'Tempo de Execução: ' in l:
					l = l.replace('Tempo de Execução: ','')
					l = l[:-3]
					tempoConsulta = float(l)
					print("Consulta: "+str(tempoConsulta))
					totalConsulta += tempoConsulta
				elif printResult and 'Resultado: ' in l:
					print(l)
			print("=")

		print("Tempo total do carregamento da ontologia: "+ str(totalCarregarOntologia))
		print("Média em "+str(qtde)+" execuções: "+str(totalCarregarOntologia/qtde))
		print("Tempo total de execução da consulta: "+ str(totalConsulta))
		print("Média em "+str(qtde)+" execuções: "+str(totalConsulta/qtde))

		print("==")
		print("Íris")
		print("==")
		totalCarregarOntologia = 0
		totalConsulta = 0
		commandIris = "java -jar iris-bench.jar " + str(command)
		for x in range(qtde):
			print("Loop "+str(x))
			result = os.popen(commandIris).read()
			result = result.split('\n')
			for l in result:
				if 'Carregar Ontologia: ' in l:
					l = l.replace('Carregar Ontologia: ','')
					l = l[:-3]
					tempoCarregarOntologia = float(l)
					print("Ontologia: "+str(tempoCarregarOntologia))
					totalCarregarOntologia += tempoCarregarOntologia
				elif 'Tempo de Execução: ' in l:
					l = l.replace('Tempo de Execução: ','')
					l = l[:-3]
					tempoConsulta = float(l)
					print("Consulta: "+str(tempoConsulta))
					totalConsulta += tempoConsulta
				elif printResult and 'Resultado: ' in l:
					print(l)

		print("Tempo total do carregamento da ontologia: "+ str(totalCarregarOntologia))
		print("Média em "+str(qtde)+" execuções: "+str(totalCarregarOntologia/qtde))
		print("Tempo total de execução da consulta: "+ str(totalConsulta))
		print("Média em "+str(qtde)+" execuções: "+str(totalConsulta/qtde))

conf.close()

tempoFimBench = time.time()

print("")
print("Fim do Benchmark")
print("Tempo Total: "+ str(round(tempoFimBench-tempoInicioBench,2)) + " segundos")
print("======================")