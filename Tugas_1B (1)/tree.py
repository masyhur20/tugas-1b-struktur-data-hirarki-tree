from node import Node

class Tree:
    def __init__(self):
        self.root = None

    def insert_node(self, parent_id, id, jabatan):
        new_node = Node(id, jabatan)
        parent = self.search_id(self.root, parent_id)

        if parent is None:
            print("Parent tidak ditemukan")
            return

        parent.children.append(new_node)

    def search_id(self, node, id):
        if node.id == id:
            return node

        for child in node.children:
            result = self.search_id(child, id)

            if result is not None:
                return result

        return None

    def search_node(self, node, jabatan):
        if node.jabatan == jabatan:
            return node

        for child in node.children:
            result = self.search_node(child, jabatan)

            if result is not None:
                return result

        return None

    def preorder(self, node):
        if node is None:
            return
        print(node.jabatan)

        for child in node.children:
            self.preorder(child)

    def inorder(self, node):
        if node is None:
            return

        if len(node.children) > 0:
            self.inorder(node.children[0])

        print(node.jabatan)

        for child in node.children[1:]:
            self.inorder(child)

    def postorder(self, node):
        if node is None:
            return

        for child in node.children:
            self.postorder(child)

        print(node.jabatan)