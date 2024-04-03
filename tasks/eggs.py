def eggs_solution(breaks):
    for i in range(1,101):
        if breaks(i):
            return i - 1
    return 100
def egg_drop(num_floors, num_eggs):
    def binary_search(low, high)
        while low < high:
            mid = (low + high) // 2
            if drop_floor(mid) == "break":
                high = mid
            else:
                low = mid + 1
        return low

    def drop_floor(floor):
        if floor >= critical_floor:
            return "break" 
        else:
            return "safe"   
    critical_floor = binary_search(1, num_floors + 1)

    return critical_floor
