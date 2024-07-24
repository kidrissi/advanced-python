import heapq


def heap(tab):
    """
    Main function to run the program.
    """
    _tab = tab
    heapq.heapify(_tab)
    sorted_tab = []
    while tab:
        sorted_tab.append(heapq.heappop(tab))
    return sorted_tab