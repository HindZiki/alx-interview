def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Première ligne du triangle

    for i in range(1, n):
        row = [1]  # Chaque ligne commence par 1
        for j in range(1, i):
            # Chaque élément est la somme des deux éléments situés au-dessus
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Chaque ligne se termine par 1
        triangle.append(row)

    return triangle
