import Tree

t1 = Tree.Tree()

t1.insere(6)
t1.insere(9)
t1.insere(7)


print("Buscando o elemento 4 na árvore: ")
t1.busca(4)

print("Imprimindo árvore pré-ordem: ")
t1.imprimirPre()

print("Imprimindo árvore in-ordem: ")
t1.imprimirIn()

print("Imprimindo árvore pós-ordem: ")
t1.imprimirPos()


print("Nível do elemento 1 na árvore: ")
t1.nivel(1)

print("Imprimindo todos os nós galhos da árvore: ")
t1.imprimeNaoFolha()

print("Imprimindo todos os nós folhas da árvore: ")
t1.imprimeNoFolha()


t1.somaNos()