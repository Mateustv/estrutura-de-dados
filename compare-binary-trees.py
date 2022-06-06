# Dadas duas árvores binárias, escreva uma função que indique se elas são iguais ou não.
#
# As duas árvores binárias são consideradas as mesmas se elas forem estruturalmente
# identicas e os nós estiverem com o mesmo valor.
#
# Exemplo 1:
# Entrada:
#
#       1          1
#      / \        / \
#     2   3      2   3
#    [1,2,3],   [1,2,3]
# Deverá retornar true pois as duas arvores são identicas.
#
# Exemplo 2:
# Entrada:
#
#       1          1
#      / \        / \
#     2   3      2   3
#    / \
#   4   5
#  [1,2,4,5,3],  [1,2,3]
# Deverá retornar false pois as duas arvores são diferentes.
# Definição da classe de árvore binária
class BinaryTree:
    value = 0
    left = None
    right = None


mateus = BinaryTree()
mateus.value = 15

joao = BinaryTree()
joao.value = 22

treeOne = BinaryTree()
treeOne.value = 20
treeOne.right = mateus
treeOne.right = mateus

treeTwo = treeOne




# def compareTree(tree1, tree2):
#     if tree1 is None or tree2 is None:
#         if tree1 == tree2:
#             return print('Ok')
#         else:
#             return print('Shit')
#     if tree1.value == tree2.value:
#         return compareTree(tree1.left, tree2.left) and compareTree(tree2.right, tree2.right)
#     else:
#         return print('Shit')
#
# compareTree(treeOne, treeTwo)

def compareTree(tree1, tree2):
    queue = [(tree1, tree2)]

    while queue:
        t1, t2 = queue.pop(0)

        if t1 is None or t2 is None:
            if t1 == t2:
                continue
            return print('Shit!')
        if t1.value != t2.value:
            return print('Shit')
        queue.append((t1.left, t2.left))
        queue.append((t1.right, t2.right))
    return print('ok')

compareTree(treeOne,joao)


