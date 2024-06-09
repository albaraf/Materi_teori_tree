def create_node(data):
    return {'data': data, 'left': None, 'right': None}

def insert_node(root, data):
    if root is None:
        return create_node(data)
    if data < root['data']:
        if root['left'] is None:
            root['left'] = create_node(data)
        else:
            insert_node(root['left'], data)
    else:
        if root['right'] is None:
            root['right'] = create_node(data)
        else:
            insert_node(root['right'], data)
    return root

def preorder_traversal(root):
    if root is not None:
        print(root['data'], end=" ")
        preorder_traversal(root['left'])
        preorder_traversal(root['right'])

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root['left'])
        print(root['data'], end=" ")
        inorder_traversal(root['right'])

def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root['left'])
        postorder_traversal(root['right'])
        print(root['data'], end=" ")

root = None
nodes = ['J', 'R', 'D', 'G', 'T', 'E', 'M', 'H', 'P', 'A', 'F', 'Q']
for node in nodes:
    root = insert_node(root, node)

print("Preorder traversal: ", end="")
preorder_traversal(root)
print()
print("Inorder traversal: ", end="")
inorder_traversal(root)
print()
print("Postorder traversal: ", end="")
postorder_traversal(root)
print()