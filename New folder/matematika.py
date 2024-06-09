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
    elif data > root['data']:
        if root['right'] is None:
            root['right'] = create_node(data)
        else:
            insert_node(root['right'], data)
    return root

def print_inorder(root):
    if root is not None:
        print_inorder(root['left'])
        print(root['data'], end=' ')
        print_inorder(root['right'])

def print_preorder(root):
    if root is not None:
        print(root['data'], end=' ')
        print_preorder(root['left'])
        print_preorder(root['right'])

# Create a binary tree and insert nodes
root = None
root = insert_node(root, 'F')
root = insert_node(root, 'A')
root = insert_node(root, 'E')
root = insert_node(root, 'K')
root = insert_node(root, 'C')
root = insert_node(root, 'D')
root = insert_node(root, 'H')
root = insert_node(root, 'B')
root = insert_node(root, 'G')

# Print the binary tree using inorder and preorder traversals
print("Inorder traversal: ", end='')
print_inorder(root)
print("\nPreorder traversal: ", end='')
print_preorder(root)
print()