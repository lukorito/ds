# You are given 20 black and white cells. The leftmost one is white, the rightmost one is black, the colors of all other cells are hidden. You can reveal the color of a cell by clicking on it. Your goal is to find two adjacent cells of different colors by using at most 5 clicks.

arr = ["W","W","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B"]

def find_adjascent_colors(arr):
    # find black and white adjascent colors
    
    mid = round(len(arr) / 2) - 1
    right = mid + 1
    left = mid - 1
    if mid > 0:
        if arr[mid] == "W":
            if arr[right] == "B":
                print("found")
                return True
            elif arr[left] == "B":
                return {mid, left}
        elif arr[mid] == "B":
            if arr[right] == "W":
                return {mid, right}
            elif arr[left] == "W":
                return {mid, left}   
        if arr[mid] == "W":
            return find_adjascent_colors(arr[mid:])
        else:
            return find_adjascent_colors(arr[:mid])

print(find_adjascent_colors(arr))