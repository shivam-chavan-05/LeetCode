# Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        col = len(matrix[0])
        L = 0
        R = (rows * col) - 1

        while L <= R:
            M_index = (L + R) // 2
            M_r = M_index // col
            M_c = M_index % col
            M_val = matrix[M_r][M_c]

            if target == M_val:
                return True
            elif target < M_val:
                R = M_index - 1
            else:
                L = M_index + 1

        return False
