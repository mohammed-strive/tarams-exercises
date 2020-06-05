import random

def quick_sort(items):
    if len(items) < 2:
        return items

    seed = random.choice(items)

    left  = [item for item in items if item <= seed]
    right = [item for item in items if item > seed]

    return quick_sort(left) + quick_sort(right)

if __name__ == '__main__':
    items = [5, 0, 1, 10, 100, 90, 78, 2, -1]
    print(quick_sort(items))
