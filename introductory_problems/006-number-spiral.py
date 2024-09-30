def number_at_position(y, x):
    layer = max(y, x)
    if layer % 2:
        if x == layer:
            return layer * layer - (y - 1)
        else:
            return (layer - 1) ** 2 + x
    else:
        if y == layer:
            return layer * layer - (x - 1)
        else:
            return (layer - 1) ** 2 + y
t=int(input())
for _ in range(t):
    y, x = map(int, input().split())
    print(number_at_position(y, x))