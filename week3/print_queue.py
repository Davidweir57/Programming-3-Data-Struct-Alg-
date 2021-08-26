def print_queue(data, front, back):

    if back < front:
        return data[front:] + data[:back]
    else:
        return data[front:back]