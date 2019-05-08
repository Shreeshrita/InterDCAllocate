import networkx as nx
import matplotlib.pyplot as plt
import pdb

def min_flow_allocate(flows_in_edges, edge_capacities):
    min_flow_allocation = 100000
    for edge in edge_capacities:
        # print(edge)
        if len(flows_in_edges[edge]) > 0:
            per_flow_alloc = edge_capacities[edge] / len(flows_in_edges[edge])
        min_flow_allocation = min(min_flow_allocation, per_flow_alloc)
    print("Min flow allocation in iteration 0 = {}".format(min_flow_allocation))
    return  min_flow_allocation

def allocate_demand(flows, edge_capacities, demand_vector):
    for i in flows:
        for path in flows[i]:
            possible = True
            for index in range(0, len(path) - 1):
                tuple = (str(path[index]), str(path[index + 1]), 0)
                if tuple not in flows_in_edges:
                    print("Not Possible to satisfy flow = {} on path = {}".format(i,
                                                                                  path))  # TODO: if not possible revert
                    possible = False
                    break
            if (possible):
                # print("Allocating {} for flow {} and path = {}".format(min_flow_allocation, i, flows[i]))
                for index in range(0, len(path) - 1):
                    tuple = (str(path[index]), str(path[index + 1]), 0)
                    # print("Subtracting for flow = {}, path = {}, tuple = {}".format(i, path, tuple))
                    edge_capacities[tuple] -= min_flow_allocation

            demand_vector[i] += min_flow_allocation

    print("Edge Capacities after iteration 0 = {}".format(edge_capacities))
    print("Demand Vectors = {}".format(demand_vector))
    return demand_vector,edge_capacities

G=nx.MultiDiGraph()
G.add_nodes_from(["E1","E2","E3","F1","F2","F3", "A","B","C","D","E","F"],supply=0)
# nx.set_node_attributes(G,"supply",0)
G.node["E1"]['supply'] = 80
G.node["E2"]['supply'] = 60
G.node["E3"]['supply'] = 80
G.node["F1"]['supply'] = -80
G.node["F2"]['supply'] = -60
G.node["F3"]['supply'] = -80
customers = [1,2,3]
flows = {1:[['E1','F','B','D','F1'],['E1','F','C','E','F1']],2:[['E2','F','C','E','F2'],['E2','F','A','E','F2']],3:[['E3','A','C','E','F3'],['E3','F','B','D','E','F3']]}
# paths = {1:[['E1','F','B','C']]}'
term_points = {1:["E1","F1"],2:["E2","F2"],3:["E3","F3"]}
# elist = [('E1', 'F', "capacity"=60,"cost"=1)]
G.add_edge('E1','F', capacity = 60, flows = [])
G.add_edge('E1','A', capacity = 60, flows = [])
G.add_edge('E2','F', capacity = 60, flows = [])
G.add_edge('E2','A', capacity = 60, flows = [])
G.add_edge('E3','F', capacity = 60, flows = [])
G.add_edge('E3','A', capacity = 60, flows = [])
G.add_edge('F','B', capacity = 100, flows = [])
G.add_edge('F','A', capacity = 60, flows = [])
G.add_edge('F','C', capacity = 100, flows = [])
G.add_edge('A','B', capacity = 100, flows = [])
G.add_edge('A','C', capacity = 100, flows = [])
G.add_edge('B','C', capacity = 100, flows = [])
G.add_edge('B','D', capacity = 80, flows = [])
G.add_edge('C','D', capacity = 80, flows = [])
G.add_edge('C','E', capacity = 90, flows = [])
G.add_edge('D','E', capacity = 60, flows = [])
G.add_edge('D','F1', capacity = 60, flows = [])
G.add_edge('D','F2', capacity = 60, flows = [])
G.add_edge('E','F2', capacity = 60, flows = [])
G.add_edge('E','F3', capacity = 60, flows = [])

# G.add_edge('E1','F', capacity = 60, flows = [1])
# G.add_edge('E1','A', capacity = 60, flows = [1])
# G.add_edge('E2','F', capacity = 60, flows = [2])
# G.add_edge('E2','A', capacity = 60, flows = [2])
# G.add_edge('E3','F', capacity = 60, flows = [3])
# G.add_edge('E3','A', capacity = 60, flows = [3])
# G.add_edge('F','B', capacity = 100, flows = [1,3])
# G.add_edge('F','A', capacity = 60, flows = [1,2])
# G.add_edge('F','C', capacity = 100, flows = [1,2])
# G.add_edge('A','B', capacity = 100, flows = [1,2])
# G.add_edge('A','C', capacity = 100, flows = [2,3])
# G.add_edge('B','C', capacity = 100, flows = [1,2,3])
# G.add_edge('B','D', capacity = 80, flows = [1,3])
# G.add_edge('C','D', capacity = 80, flows = [1,3])
# G.add_edge('C','E', capacity = 90, flows = [1,2,3])
# G.add_edge('D','E', capacity = 60, flows = [1,2,3])
# G.add_edge('D','F1', capacity = 60, flows = [1])
# G.add_edge('D','F2', capacity = 60, flows = [2])
# G.add_edge('E','F2', capacity = 60, flows = [2])
# G.add_edge('E','F3', capacity = 60, flows = [3])


print("Nodes of graph: ")
print(G.nodes())
print(nx.get_node_attributes(G,"supply"))
print("Edges of graph: ")
print(G.edges())
# adding a list of edges:
# G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

# nx.draw_networkx(G, with_labels=True, pos={"E1":(0,0), "E2":(0,1),"E3":(0,2),"F":(1,2),
#                                            "A":(1,0), "B":(2,0), "C":(2,2), "D":(3,2),
#                                            "E":(3,0), "F1":(4,0), "F2":(4,1),"F3":(4,2)})
# plt.savefig("simple_path.png") # save as png
# plt.show() # display

edges = nx.edges(G)
print(edges)
edge_capacities = (nx.get_edge_attributes(G,"capacity"))
flows_in_edges = (nx.get_edge_attributes(G,"flows"))
print("Edge Capacities are {}".format(edge_capacities))
print("No of edges = {}".format(len(edge_capacities)))

for i in flows:
    for path in flows[i]:
        for index in range(0,len(path)-1):
            tuple = (str(path[index]), str(path[index+1]),0)
            if tuple in flows_in_edges:
                # print(flows_in_edges[tuple])
                if i not in flows_in_edges[tuple]:
                    flows_in_edges[tuple].append(i)

print("Flows allocation to edges = {}".format(flows_in_edges))
demand_vector = {1: 0, 2: 0, 3: 0}
min_flow_allocation = min_flow_allocate(flows_in_edges, edge_capacities)

demand_vector, edge_capacities = allocate_demand(flows, edge_capacities, demand_vector)
remove_flows = []
for customer in demand_vector:
    print(flows[customer][0][-1])
    G.node[flows[customer][0][0]]['supply'] -= demand_vector[customer]
    G.node[flows[customer][0][-1]]['supply'] +=  demand_vector[customer]
    if (G.node[flows[customer][0][0]]['supply']==0) and (G.node[flows[customer][0][-1]]['supply']==0):
        remove_flows.append(customer)
print("Nodes and supply = {}".format(nx.get_node_attributes(G,"supply")))

for i in remove_flows:
    for path in flows[i]:
        for index in range(0,len(path)-1):
            tuple = (str(path[index]), str(path[index+1]),0)
            if tuple in flows_in_edges:
                # print(flows_in_edges[tuple])
                if i in flows_in_edges[tuple]:
                    flows_in_edges[tuple].remove(i)
    flows.pop(i)

# pdb.set_trace()
remove_edge_tuples = []
for edge in edge_capacities:
    if edge_capacities[edge] <=0:
        print("Edge Capacity <= 0 for edge {}".format(edge))
        print("Edge points = {} and {}".format(str(edge[0]), str(edge[1])))
        remove_edge_tuples.append((str(edge[0]), str(edge[1]), 0))
        G.remove_edge(str(edge[0]),str(edge[1]))

for i in flows:
    for path in flows[i]:
        for index in range(0, len(path) - 1):
            tuple = (str(path[index]), str(path[index + 1]), 0)
            if tuple  in remove_edge_tuples:
                flows[i].remove(path)
                break

print("New flows are = {} and flows_in_edges = {}".format(flows,flows_in_edges))


edge_capacities = (nx.get_edge_attributes(G,"capacity"))
flows_in_edges = (nx.get_edge_attributes(G,"flows"))

print("Edge Capacities are {}".format(edge_capacities))
print("No of edges = {}".format(len(edge_capacities)))

min_flow_allocation = min_flow_allocate(flows_in_edges, edge_capacities)

demand_vector, edge_capacities = allocate_demand(flows, edge_capacities, demand_vector)

# for edge in edge_capacities:


