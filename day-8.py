from anytree import Node, PostOrderIter
i = 0
node_name = 0
data = [int(i) for i in open('day-8.txt').readline().split(' ')]


def get_node(parent_node=None):
    global i
    global node_name
    node = Node("Node {}".format(node_name),
                parent=parent_node, meta=list(), value=0)
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

for node in PostOrderIter(tree):
    if node.children:
        for j, child in enumerate(node.children):
            for k in node.meta:
                if k == (j + 1):
                    node.value += child.value
    else:
        node.value = sum(node.meta)

print("Part 2: {}".format(tree.root.value))
