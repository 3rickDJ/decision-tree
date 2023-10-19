from treelib import Node, Tree
tree = Tree()
tree.create_node("Harry", "harry", data=[1,2,3])
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mark", "mark", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
data = tree.to_dict()
tree.save2file("hola.txt")
tree.show()

