flat_array = []

def flatTheArray(element):
    if isinstance(element, list):
        for item in element:
            flatTheArray(item)
    else:
        flat_array.append(element)

multidimensional_array = [[1, 2, [3]], 4, [5, [6, 7]], [8, [9, [10]]],True,[False,[True,30,["Last element"]]]]
flatTheArray(multidimensional_array)
print(flat_array)
