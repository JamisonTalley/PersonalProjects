#dict_graph.py
#Jamison Talley
#16-2-23

#this program is my implementation of a dictionary based directed
#graph. This program is still a work in progress, but it serves as
#a funcional demonstration of how directed graphs can be modeled using
#dictionaries
class dict_graph:
    def __init__(self, nodes=[], node_edges=None, edge_costs=None):
        self.nodes = []
        self.edges = {}
        self.edge_cost = {}
        if node_edges == None:
            node_edges = [[] for i0 in range(len(nodes))]
        if edge_costs == None:
            edge_costs = [[] for i0 in range(len(nodes))]
        for i1 in range(len(nodes)):
            self.add_node(nodes[i1], node_edges[i1], edge_costs[i1])

    def add_node(self, name, node_edges=[], edge_costs=[]):
        self.nodes.append(name)
        self.edges[name] = node_edges
        self.edge_cost[name] = edge_costs
        return

    def add_edge(self, node_a, node_b, cost=1):
        node_edges = (self.edges.pop(node_a)[:])
        edge_costs = (self.edge_cost.pop(node_a)[:])

        if node_b not in node_edges:
            node_edges.append(node_b)
            edge_costs.append(cost)
        else:
            for i1 in range(len(node_edges)):
                if node_edges[i1] == node_b:
                    edge_costs[i1] = cost
        
        self.edges[node_a] = node_edges
        self.edge_cost[node_a] = edge_costs
        return

    def debug(self):
        print(self.edges)
        print()
        print(self.edge_cost)

    def __str__(self):
        return str(self.edges)

def main():
    graph = dict_graph(['5','3','7','2','4','8'],
                       [['3','7'], [], [], [], [], []],
                       [[17,1], [], [], [], [], []])
    graph.add_edge('5', '3', 8)
    graph.add_edge('5', '7')
    graph.add_edge('7', '8')
    graph.add_edge('4', '8')
    graph.debug()



if __name__ == "__main__":
    main()