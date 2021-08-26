def make_edge_list(adjacency):
    """ this function create an edge list representation of a graph using the supplied adjacency matrix
    """
    # Maybe start with an empty edge_list
    edge_list = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Insert code here
    for lst in adjacency:
        tmp = []
        count = 0
        for rel in lst:
            if rel == 1:
                tmp.append(alphabet[count])
            count += 1
        edge_list.append(tmp)

    return edge_list

def main():
    adj = [[1, 1, 1], [0, 1, 1]]
    edge = make_edge_list(adj)

    print(edge)

if __name__ == "__main__":
    main()