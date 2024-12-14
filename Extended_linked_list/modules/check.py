from src.main_lb1 import Extended_Linked_List
def check(arr1, arr2):
    ell = Extended_Linked_List(3)
    for i in arr1:
        ell.push_back(i)
        print(ell)
    for i in arr2:
        print(ell.search(ell.search_by_value_first(i)) == i)
        ell.pop(ell.search_by_value_first(i))
        print(ell)
if __name__ == "__main__":
    check([i for i in range(15)], [1,2,3,4,5,6,7])
