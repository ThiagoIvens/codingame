nNodes, nLinks, nGateways = [int(i) for i in input().split()]
gateway = []
ligacoes = {}
for i in range(nLinks):
    n1, n2 = [int(j) for j in input().split()]
    ligacoes.setdefault(n1, []).append(n2)
    ligacoes.setdefault(n2, []).append(n1)
for i in range(nGateways):
    gatewayIndex = int(input())
    gateway.append(gatewayIndex) 

def blockAgent(agentePosition, gateway, ligacoes):
    for g in gateway:
        if g in ligacoes[agentePosition]:
            return [agentePosition, g]
    for g in gateway:
        if len(ligacoes[g]) > 0:
            return [g, ligacoes[g][0]]
    return [0, 0]

def rmvLinks(c1, c2, ligacoes):
    ligacoes[c1].remove(c2)
    ligacoes[c2].remove(c1)

# game loop
while True:
    agentePosition = int(input())
    c1, c2 = blockAgent(agentePosition, gateway, ligacoes)
    print("{0} {1}".format(c1, c2))
    rmvLinks(c1, c2, ligacoes)