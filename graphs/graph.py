class Node:
    def __init__(self, id, data) -> None:
        self.id = id
        self.data = data


class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
        self.num_nodes = 0

    def add_vertex(self, id, data=None):
        if id in self.adj_list.keys():
            print(f"Node with id {id} already exists!")
            return
        _node = Node(id, data)
        self.adj_list[id] = {"node": _node, "edges": []}
        self.num_nodes += 1

    def add_edge(self, node1_idx, node2_idx):
        # undirected
        assert node1_idx in self.adj_list.keys()
        assert node2_idx in self.adj_list.keys()
        node_1 = self.adj_list[node1_idx]["node"]
        node_1_connections = [x.id for x in self.adj_list[node1_idx]["edges"]]

        node_2 = self.adj_list[node2_idx]["node"]
        node_2_connections = [x.id for x in self.adj_list[node2_idx]["edges"]]

        if node2_idx not in node_1_connections:
            self.adj_list[node1_idx]["edges"].append(node_2)

        if node1_idx not in node_2_connections:
            self.adj_list[node2_idx]["edges"].append(node_1)

    def show_connections(self):
        for k, v in self.adj_list.items():
            print(k, " ---> ", ", ".join([x.id for x in v["edges"]]))


if __name__ == "__main__":
    mygraph = Graph()
    mygraph.add_vertex("0")
    mygraph.add_vertex("1")
    mygraph.add_vertex("2")
    mygraph.add_vertex("3")
    mygraph.add_vertex("4")
    mygraph.add_vertex("5")
    mygraph.add_vertex("6")
    mygraph.add_edge("3", "1")
    mygraph.add_edge("3", "4")
    mygraph.add_edge("4", "2")
    mygraph.add_edge("4", "5")
    mygraph.add_edge("4", "3")
    mygraph.add_edge("6", "5")
    mygraph.add_edge("5", "4")
    mygraph.add_edge("5", "6")
    mygraph.add_edge("0", "1")
    mygraph.add_edge("0", "2")
    mygraph.add_edge("1", "0")
    mygraph.add_edge("1", "2")
    mygraph.add_edge("1", "3")
    mygraph.add_edge("2", "0")
    mygraph.add_edge("2", "1")
    mygraph.add_edge("2", "4")
    mygraph.show_connections()
