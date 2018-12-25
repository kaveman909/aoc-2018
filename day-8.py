from anytree import Node, RenderTree
i = 0
node_name = 0
data = [int(i) for i in open('day-8-test.txt').readline().split(' ')]


def get_node(parent_node=None):
    global i
    global node_name
    node = Node("Node {}".format(node_name),
                parent=parent_node, meta=list())
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
print(RenderTree(tree))
