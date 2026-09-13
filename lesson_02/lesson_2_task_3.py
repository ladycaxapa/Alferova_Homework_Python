def square(side):
    area = side * side
    if area % 1 != 0:
        return int(area) + 1
    else:
        return int(area)


print(square(4.1))
