from anytree import Node, PostOrderIter
from anytree.exporter import DotExporter
i = 0
node_name = 0
data = [int(i) for i in open('day-8.txt').readline().split(' ')]


def get_node(parent_node=None):
    global i
    global node_name
    node = Node(str(node_name), parent=parent_node, meta=list(), value=0)
    node_name += 1
    n_children = data[i]
    n_metachars = data[i + 1]
    i += 2
    for _ in range(n_children):
        get_node(node)
    for _ in range(n_metachars):
        node.meta.append(data[i])
        i += 1
    return node


tree = get_node()
meta_sum = sum([sum(node.meta) for node in PostOrderIter(tree)])
print("Part 1: {}".format(meta_sum))

# This works because PostOrderIter iterates starting at the leaves, and
# works its way towards the root.  Therefore, parents without children will
# run first, getting a value.  Parents with children are then guaranteed that
# their children's value will have been computed already.
for node in PostOrderIter(tree):
    if node.children:
        for k in node.meta:
            l = k - 1
            if (l >= 0) and (l < len(node.children)):
                node.value += node.children[l].value
    else:
        node.value = sum(node.meta)

print("Part 2: {}".format(tree.root.value))
DotExporter(tree, nodenamefunc=lambda node: "Node: {}\nValue: {}".format(
    node.name, node.value)).to_dotfile("tree.dot")
