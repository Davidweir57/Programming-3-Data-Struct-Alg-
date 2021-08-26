def make_adjacency_matrix(edge_list):
    """ this function create an adjacency matrix representation of a graph using the supplied edge list
    """
    # Maybe start with an empty adjacency matrix
    adjacency_matrix = []
    values = []

    for lst in edge_list:
        for rel in lst:
            if rel not in values:
                values.append(rel)
    
    for lst in edge_list:
        tmp = []
        for ele in values:
            if ele in lst:
                tmp.append(1)
            else:
                tmp.append(0)
        
        adjacency_matrix.append(tmp)
    
    return adjacency_matrix

def main():
    edge = [['A', 'B',], ['A', 'C']]
    adj = make_adjacency_matrix(edge)

    print(adj)

if __name__ == "__main__":
    main()