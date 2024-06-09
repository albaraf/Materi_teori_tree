nilai_nilai = ['J', 'R', 'D', 'G', 'T', 'E', 'M', 'H', 'P', 'A', 'F', 'Q']

def create_node(nilai):
    return {'nilai': nilai, 'kiri': None, 'kanan': None}

def insert_node(root, nilai):
    if root is None:
        return create_node(nilai)
    if nilai < root['nilai']:
        if root['kiri'] is None:
            root['kiri'] = create_node(nilai)
        else:
            insert_node(root['kiri'], nilai)
    else:
        if root['kanan'] is None:
            root['kanan'] = create_node(nilai)
        else:
            insert_node(root['kanan'], nilai)
    return root

def traversal_inorder(root):
    if root is not None:
        traversal_inorder(root['kiri'])
        print(root['nilai'], end=" ")
        traversal_inorder(root['kanan'])

root = None
for nilai in nilai_nilai:
    root = insert_node(root, nilai)

print("Traversal inorder:")
traversal_inorder(root)
print()