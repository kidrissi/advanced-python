
import heapq


def heap():
    """
    Main function to run the program.
    """
    tab = [2, 8, 5, 3, 9, 1]

    heapq.heapify(tab)
    print(tab)
    sorted_tab = []
    # heapq.heappop(tab)
    # print(tab)
    while tab:
        sorted_tab.append(heapq.heappop(tab))

    print(sorted_tab)


if __name__ == "__main__":
    heap()
