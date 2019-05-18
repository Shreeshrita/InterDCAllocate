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

def allocate_demand(flows, edge_capacities, demand_vector, flows_in_edges, min_flow_allocation):
    for i in flows: # Shouldnt we just do it along the path which we calculate the edge capacity
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
                print("Allocating {} for flow {} and path = {}".format(min_flow_allocation, i, path))
                for index in range(0, len(path) - 1):
                    tuple = (str(path[index]), str(path[index + 1]), 0)
                    # print("Subtracting for flow = {}, path = {}, tuple = {}".format(i, path, tuple))
                    edge_capacities[tuple] -= min_flow_allocation

            demand_vector[i] += min_flow_allocation
            break

    print("Edge Capacities after iteration 0 = {}".format(edge_capacities))
    print("Demand Vectors = {}".format(demand_vector))
    return demand_vector,edge_capacities
