def create_node(data):
    return {'data': data, 'kiri': None, 'kanan': None}

def build_tree(inorder, preorder, start, end, index):
    if start > end or index >= len(preorder):
        return None

    root = create_node(preorder[index])
    index += 1

    if start == end:
        return root

    for i in range(start, end + 1):
        if inorder[i] == root['data']:
            root['kiri'] = build_tree(inorder, preorder, start, i - 1, index)
            root['kanan'] = build_tree(inorder, preorder, i + 1, end, index)
            break

    return root

def print_postorder(root):
    if root is None:
        return

    print_postorder(root['kiri'])
    print_postorder(root['kanan'])
    print(root['data'], end=" ")

inorder = "EACKFHDBG"
preorder = "FAEKCDHGB"

root = build_tree(inorder, preorder, 0, len(inorder) - 1, 0)
print("Postorder traversal: ", end="")
print_postorder(root)