from Array_Rotate_Image import Solution


def test1():
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    output_matrix = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    s.rotate(matrix)

    assert matrix == output_matrix


def test2():
    s = Solution()
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    output_matrix = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]
    s.rotate(matrix)

    assert matrix == output_matrix
