def helper(current, total):
    if current <= total:
        print(f"Day {current}")
        helper(current + 1, total)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    helper(1, days)
    print("Harvest time!")
