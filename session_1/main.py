import heap_fun
import big_call_heap

if __name__ == "__main__":
    tab = [1, 3, 2, 8, 9, 5]
    print("initial tab is :", tab)
    heap_result = heap_fun.heap(tab)
    print("sorted tab is :", heap_result)
    print("100 sorted number: ")
    big_heap_result = heap_fun.heap(big_call_heap.big_tab(1000000, 100000000)) # million sorted numbers
    print(big_heap_result)
