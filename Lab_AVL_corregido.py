import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  





def getHeight(node):
    if not node:
        return 0
    return node.height


def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)


def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))



def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x  


def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y  



def getMinNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current



class AVLTree:
    def __init__(self):
        self.root = None

    
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        
        if not node:
            return Node(value)

        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node  

        
        updateHeight(node)

        
        balance = getBalance(node)

        
        if balance > 1 and getBalance(node.left) >= 0:
            node = rotate_right(node) 

        
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            node = rotate_right(node)  

        
        elif balance < -1 and getBalance(node.right) <= 0:
            node = rotate_left(node)  

        
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            node = rotate_left(node)  

        return node

    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        
        if not node:
            print(f"El valor {value} no se encontró en el árbol.")
            return node

        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            
            if node.left is None:
                return node.right

           
            elif node.right is None:
                return node.left

            
            sucesor = getMinNode(node.right)
            node.value = sucesor.value
            node.right = self._delete_recursive(node.right, sucesor.value)

        
        updateHeight(node)

        
        balance = getBalance(node)

        
        if balance > 1 and getBalance(node.left) >= 0:
            node = rotate_right(node)

        
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            node = rotate_right(node)

    
        elif balance < -1 and getBalance(node.right) <= 0:
            node = rotate_left(node)

        
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            node = rotate_left(node)

        return node

    
    def inorder(self):
        resultado = []
        self._inorder_recursive(self.root, resultado)
        return resultado

    def _inorder_recursive(self, node, resultado):
        if node:
            self._inorder_recursive(node.left, resultado)
            resultado.append(node.value)
            self._inorder_recursive(node.right, resultado)

    
    def visualizar(self):
        if not self.root:
            print("El árbol está vacío.")
            return
        print("\n--- Visualización del árbol AVL ---")
        self._visualizar_recursive(self.root, "", True)
        print()

    def _visualizar_recursive(self, node, prefijo, es_derecha):
        if node:
            
            self._visualizar_recursive(node.right, prefijo + ("│   " if not es_derecha else "    "), False)

            
            conector = "└── " if es_derecha else "┌── "
            print(prefijo + conector + f"[{node.value}] h={node.height} b={getBalance(node)}")

            
            self._visualizar_recursive(node.left, prefijo + ("    " if not es_derecha else "│   "), True)




avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")
avl.visualizar()
print("Recorrido in-order:", avl.inorder())

print("\nEliminando el valor 40...")
avl.delete(40)
print("\n--- Después de eliminar 40 ---")
avl.visualizar()
print("Recorrido in-order:", avl.inorder())

print("\nEliminando el valor 10...")
avl.delete(10)
print("\n--- Después de eliminar 10 ---")
avl.visualizar()
print("Recorrido in-order:", avl.inorder())

print("\nIntentando eliminar un valor que no existe (99)...")
avl.delete(99)
