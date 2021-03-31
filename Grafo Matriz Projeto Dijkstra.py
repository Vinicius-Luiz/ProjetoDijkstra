'''
%%MatrixMarket matrix coordinate real symmetric
%-------------------------------------------------------------------------------
% UF Sparse Matrix Collection, Tim Davis
% http://www.cise.ufl.edu/research/sparse/matrices/Pajek/USAir97
% name: Pajek/USAir97
% [Pajek network: US Air flights, 1997]
% id: 1529
% date: 1997
% author: US Air
% ed: V. Batagelj
% fields: name title A id kind notes aux date author ed
% aux: nodename coord
% kind: undirected weighted graph
%-------------------------------------------------------------------------------
'''
#Algoritmo de Prim NÃO faz parte do projeto

def arqVA():
    '''Ler Arquivo de Vértices e Arestas'''
    caminhos = []
    arquivo = open("USAir97.txt","r") 
    for linha in arquivo:
        if linha[0] != '%':
            valores = linha.split()
            v1, v2, p = int(valores[0])-1, int(valores[1])-1,   round(float(valores[2])*10**4, 2)
            valores = [v1, v2, p]
            caminhos.append(valores)
            
    numVertices, numArestas = caminhos[0][0]+1, int((caminhos[0][2])/10**4)+1
    caminhos.pop(0)
    arquivo.close()
    return caminhos, numVertices, numArestas

def aeroportos():
    '''Ler arquivo com os nomes dos aeroportos'''
    nomesAero = {}
    arquivo = open("USAir97_nodename.txt","r")
    i = 0
    for nome in arquivo:
        nomesAero[i] = nome.replace('\n', '')
        i += 1
    arquivo.close()
    return nomesAero

def inserirCaminhos(caminhos):
    '''Insere os caminhos carregado dos arquivos no grafo'''
    i = 0
    for caminho in caminhos:
        v1, v2, p = g.legenda[caminho[0]][0], g.legenda[caminho[1]][0], caminho[2]
        g.inserir_aresta(v1, v2, p)
        i += 1
    print(f'{i} ROTAS FORAM INSERIDAS COM SUCESSO\n')

def getNomes(legenda):
    '''Imprime nome de todos os aeroportos'''
    for num, nome in legenda.items():
        print(f'{num+1} - {nome[0]}')

def compararRotas(v1, v2):
    '''Compara caminho com e sem escala entre dois aeroportos'''
    iTemp, jTemp = g.aux_iTemp(v1), g.aux_iTemp(v2)
    if type(iTemp) is bool or type(iTemp) is bool:
        print('ERRO: AEROPORTO INVÁLIDO\n')
        return
    sEscala = g.verificar_aresta(v1, v2, 'comparar')
    print(sEscala)
    if 'INEXISTENTE' in sEscala:
        g.dijkstra(v1, v2, 'comparar')

def verificarRotasInexistentes():
    '''verifica quantas rotas sem escala existem'''
    qtdSemRotas = 0
    rotasEncontradas = 0
    for v1 in range(g.vertices):
        for v2 in range(g.vertices):
            if v1 < v2:
                n1, n2 = g.legenda[v1][0], g.legenda[v2][0]
                rota = g.verificar_aresta(n1, n2, 'vRotas')
                if not rota:
                    qtdSemRotas += 1
                    rotasEncontradas += g.dijkstra(n1, n2, 'vRotas')
    print(f'FORAM ENCONTRADAS {int(qtdSemRotas)} ROTAS SEM ESCALAS INEXISTENTES ENTRE DOIS AEROPORTOS\nFORAM ENCONTRADAS {rotasEncontradas} ROTAS COM ESCALA PARA SUPRIR AS FALTANTES\nNÃO SERÁ POSSÍVEL REALIZAR {(qtdSemRotas)-rotasEncontradas} VOOS')
        
    
class Grafo_Matriz():
    def __init__(self, numVert, ponderado = False, direcionado = False):
        self.vertices     = numVert
        self.arestas      = 0
        self.matriz       = []
        self.legenda      = {}
        self.ponderado    = ponderado
        self.direcionado  = direcionado
        nomes = aeroportos()
        if self.direcionado:
            for i in range(numVert):
                m = [None]*numVert
                self.matriz.append(m)
                self.legenda[i] = [nomes[i],[]]
        else:
            cont = numVert
            for i in range(numVert):
                m    = [None]*cont
                self.matriz.append(m)
                self.legenda[i] = [nomes[i],[]]
                cont -= 1
            del cont
            
    def imprimir_grafo(self):
        cont = 0
        numVert = self.vertices
        while cont < numVert:
            print(self.legenda[cont][0], self.matriz[cont])
            cont += 1

    def qtd_vertices_arestas(self):
        print(f'QUANTIDADE DE AEROPORTOS: {self.vertices}\nQUANTIDADE DE ROTAS: {self.arestas}\n(A>B & B>A É CONSIDERADO 1 ROTA)\n')

    def aux_iTemp(self, vert):
        for t in self.legenda:
            if self.legenda[t][0] == vert:
                iTemp = t
                return iTemp
        return False

    def verificar_peso(self, v1, v2):
        if self.direcionado:
            peso = self.matriz[v1][v2]
        else:
            min_i, max_i = min([v1,v2]), max([v1,v2])
            peso = self.matriz[min_i][max_i - min_i]
        return peso
        
    def verificar_aresta(self, v1, v2, ref = None):
        vertices = [v1, v2]
        iTemp, jTemp = self.aux_iTemp(vertices[0]), self.aux_iTemp(vertices[1])
        if type(iTemp) is bool:
            if ref is None:
                print('ROTA NÃO PERTENCE AO GRAFO\n')
                return
            else:
                return None, iTemp, None, vertices
            
        if vertices[1] in self.legenda[iTemp][1]:
            peso = self.verificar_peso(iTemp, jTemp)
            if ref == 'vRotas':
                return True
            elif ref is 'comparar':
                return f'DISTÂNCIA DA ROTA SEM ESCALAS\n>> MILHAS PERCORRIDAS: {peso}\n\n'
            else:
                jTemp = self.aux_iTemp(vertices[1])
                return 'Exist', iTemp, jTemp, vertices
        else:
            if ref == 'vRotas':
                return False
            elif ref is 'comparar':
                return f'DISTÂNCIA DA ROTA SEM ESCALAS\n>> INEXISTENTE\n\n'
            else:
                return None, iTemp, None, vertices

    def vertices_adjacentes(self, vert):
        iTemp = self.aux_iTemp(vert)
        if type(iTemp) is bool and not iTemp:
            print('ERRO: AEROPORTO NAO ENCONTRADO\n')
        else:
            print(f'ADJACENTES DO AEROPORTO [{vert.upper()}]:',self.legenda[iTemp][0]+'\n'+'_'*80)
            for v in self.legenda[iTemp][1]:
                print(v)
            print('\n')

    def inserir_aresta(self, v1, v2, peso = None):
        ref = 0
        vertTemp = [v1, v2]
        for t in self.legenda:
            if vertTemp[0] == self.legenda[t][0]:
                vertTemp[0] = t
                ref += 1
            if vertTemp[1] == self.legenda[t][0]:
                vertTemp[1] = t
                ref += 1
            if ref == 2:
                break
            
        if type(vertTemp[0]) is str or type(vertTemp[1]) is str:
            print('ERRO: AEROPORTO NAO ENCONTRADO\n')
            return
        else:
            if not self.direcionado:
                min_i, max_i = min(vertTemp), max(vertTemp)
            else:
                origem, destino = vertTemp[0], vertTemp[1]
            if peso is None:
                if self.ponderado:
                    print('ERRO: GRAFO É PONDERADO\n')
                    return
                else:
                    if not self.direcionado:
                        if self.matriz[min_i][max_i-min_i] is None:
                            self.arestas += 1
                            self.legenda[min_i][1].append(self.legenda[max_i][0])
                            if self.legenda[min_i][0] != self.legenda[max_i][0]:
                                self.legenda[max_i][1].append(self.legenda[min_i][0])
                        self.matriz[min_i][max_i - min_i] = 1
                    else:
                        if self.matriz[origem][destino] is None:
                            self.arestas += 1
                            self.legenda[origem][1].append(self.legenda[destino][0])
                        self.matriz[origem][destino] = 1
                    #print('Aresta inserida')
            else:
                if not self.ponderado:
                    print('ERRO: GRAFO NÃO É PONDERADO\n')
                    return
                else:
                    if not self.direcionado:
                        if self.matriz[min_i][max_i-min_i] is None:
                            self.arestas += 1
                            self.legenda[min_i][1].append(self.legenda[max_i][0])
                            self.legenda[max_i][1].append(self.legenda[min_i][0])
                        self.matriz[min_i][max_i - min_i] = peso
                    else:
                        if self.matriz[origem][destino] is None:
                            self.arestas += 1
                            self.legenda[origem][1].append(self.legenda[destino][0])
                        self.matriz[origem][destino] = peso
                    #print('Aresta inserida')

    def dijkstra(self, inicio, fim, ref = None):
        iInicio, iFim = self.aux_iTemp(inicio), self.aux_iTemp(fim)
        if type(iInicio) is bool or type(iFim) is bool:
            print(f'NÃO HÁ CAMINHO ENTRE [{inicio.upper()}] E [{fim.upper()}]\n')
        caminho, menorDist, antecessor, naoVisitados, inf    = [], {}, {}, list(self.legenda.keys()), 10**8
        for vertice in naoVisitados:
            menorDist[vertice] = inf
        menorDist[iInicio] = 0

        while naoVisitados:
            minvertice = None
            for vertice in naoVisitados:
                if minvertice is None:
                    minvertice = vertice

                elif menorDist[vertice] < menorDist[minvertice]:
                    minvertice = vertice
            for adj in self.legenda[minvertice][1]:
                adj = self.aux_iTemp(adj)
                peso = self.verificar_peso(minvertice, adj)
                if peso + menorDist[minvertice] < menorDist[adj]:
                    menorDist[adj] = peso + menorDist[minvertice]
                    antecessor[adj] = minvertice
            naoVisitados.remove(minvertice) 
        vTemp = iFim
        while vTemp != iInicio:
            try:
                caminho.insert(0, self.legenda[vTemp][0])
                vTemp = antecessor[vTemp]
            except KeyError:
                if ref is 'vRotas':
                    return 0
                print(f'NÃO HÁ CAMINHO ENTRE {inicio.upper()} E {fim.upper()}\n')
                break
            
        caminho.insert(0,self.legenda[iInicio][0])
        if menorDist[iFim] != inf:
            output = 'MENOR PERCURSO: '
            for rota in caminho:
                output += rota+' > '
            output+='\tMILHAS PERCORRIDAS: '+str(menorDist[iFim])
            if ref is 'comparar':
                print(f'DISTÂNCIA DA ROTA MAIS CURTA COM ESCALAS\n>> {output[16:]}\n\n')
            elif ref is 'vRotas':
                return 1
            else:
                print(output)

    def prim(self):
        global inf
        inf     = 10**5
        global rotulos
        rotulos = {}
        iVert = 0
        listAdjacentes = []
        S = []
        for i in range(self.vertices):
            rotulos[i] = inf
        rotulos[0] = 0

        while len(S) < self.vertices-1:
            adjs = self.legenda[iVert][1]
            (v1, v2, p) = self.selecionarAresta(iVert, adjs, listAdjacentes)
            S.append((v1, v2, p))
            rotulos[v2] = p
            iVert = v2

        menorCaminho = 0
        for caminho in S:
            menorCaminho += caminho[2]
        print(menorCaminho)
        del rotulos
        del listAdjacentes

    def selecionarAresta(self, iVert, adjs, listAdjacentes):
        for adj in adjs:
            adj = self.aux_iTemp(adj)
            if rotulos[adj] == inf:
                peso = self.verificar_peso(iVert, adj)
                listAdjacentes.append((iVert, adj, peso))

        arestaSegura = (None, None, inf)
        c = 1
        for aresta in listAdjacentes:
            if aresta[2] < arestaSegura[2]:
                if rotulos[aresta[0]] == inf or rotulos[aresta[1]] == inf:
                    arestaSegura = aresta
        listAdjacentes.remove(arestaSegura)
        return arestaSegura
            

        
print('_'*80,f'\n\nUSAir97 - ROTAS DE AERORPORTOS NO TERRITÓRIO AMERICANO EM 1997\n{"_"*80}')  
caminhos, numV, numA = arqVA()        
g = Grafo_Matriz(numV, ponderado = True)
inserirCaminhos (caminhos)
programa = True
while programa:
    op = input(f'\n[1] COMPARAR ROTAS COM E SEM ESCALA ENTRE 2 AEROPORTOS\n[2] VER NOMES DOS AEROPORTOS\n[3] VER QUANTIDADE DE ROTAS INEXISTENTES\n[4] VER QUANTIDADE DE AEROPORTOS E ROTAS\n[5] SAIR\n> ')
    if op == '1':
        v1 = input(f'NOME DO AEROPORTO 1\n> ')
        v2 = input(f'NOME DO AEROPORTO 2\n> ')
        print('\n')
        compararRotas(v1, v2)
    elif op == '2':
        getNomes(g.legenda)
    elif op == '3':
        confirmacao = input('ESTE PROCESSO DEMORA LONGOS MINUTOS, DESEJA CONTINUAR? (sim/nao)\n> ').upper()
        if confirmacao == 'SIM':
            verificarRotasInexistentes()
    elif op == '4':
        g.qtd_vertices_arestas()
    elif op == '5':
        programa = False
