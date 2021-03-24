
class No:
    def __init__(self, indice: int):
        self.indice = indice
        self.ligacoes = []
        self.porta = False
        self.ligacaoMarcada = False

    @property
    def nLigacoesPortas(self) -> int:
        return sum(link.porta for link in self.ligacoes)

    def pegarLigacaoPorta(self):
        return next((link for link in self.ligacoes if link.porta), None)


class Graph:
    def __init__(self):
        self.nos = []
        self.porta_alvo = []

    def atualizar_alvo(self, porta: No):
        if not porta.ligacoes:
            self.porta_alvo.remove(porta)

    def resetar(self):
        for node in self.nos:
            node.ligacaoMarcada = False

    def mostraResposta(self, no1, no2):
        print(no1.indice, no2.indice)

    def le(self):
        self.nNos, nLigacoes, self.nPortas = map(int, input().split())

        for indice in range(self.nNos):
            self.nos.append(No(indice))

        for n in range(nLigacoes):
            n1, n2 = map(int, input().split())
            no1 = self.nos[n1]
            no2 = self.nos[n2]
            no1.ligacoes.append(no2)
            no2.ligacoes.append(no1)

        for _ in range(self.nPortas):
            indice = int(input())
            porta = self.nos[indice]
            porta.porta = True
            self.porta_alvo.append(porta)

    def bloquear_agente(self, indiceAgente: int) -> bool:
        no_agente = self.nos[indiceAgente]
        for no in no_agente.ligacoes:
            if no.porta:
                self.mostraResposta(no_agente, no)
                no_agente.ligacoes.remove(no)
                no.ligacoes.remove(no_agente)
                self.atualizar_alvo(no)
                return True
        return False

    def bloquear_porta_vermelha(self):
        porta = self.porta_alvo[0]
        no = porta.ligacoes[0]
        self.mostraResposta(porta, no)
        porta.ligacoes.remove(no)
        no.ligacoes.remove(porta)
        self.atualizar_alvo(porta)

    def bloquear_duas_portas(self, indiceAgente: int) -> bool:
        no_agente = self.nos[indiceAgente]
        queue = []
        self.resetar()
        no_agente.ligacaoMarcada = True
        queue.append(no_agente)

        while queue:
            no_atual = queue.pop(0)
            for vizinho in no_atual.ligacoes:
                nLigacoesPortas = vizinho.nLigacoesPortas
                if not vizinho.porta and nLigacoesPortas >= 1 and not vizinho.ligacaoMarcada:
                    vizinho.ligacaoMarcada = True
                    if nLigacoesPortas == 2:
                        porta = vizinho.pegarLigacaoPorta()
                        self.mostraResposta(vizinho, porta)
                        vizinho.ligacoes.remove(porta)
                        porta.ligacoes.remove(vizinho)
                        self.atualizar_alvo(porta)
                        return True
                    else:
                        queue.append(vizinho)
        return False

def main(graph):
        while True:
            posicaoAgente = int(input())
            if not graph.bloquear_agente(posicaoAgente):
                if not graph.bloquear_duas_portas(posicaoAgente):
                    graph.bloquear_porta_vermelha()

if __name__ == "__main__":
    graph = Graph()
    graph.le()
    main(graph)