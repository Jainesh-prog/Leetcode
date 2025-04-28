class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count = 0  # \U0001f4c8 Highest number of 1s found so far
        row_index = 0  # \U0001f9f9 Row index where max_count was found

        for i, row in enumerate(mat):
            count = row.count(1)  # \U0001f9ee Count number of 1s in current row

            if count > max_count:
                max_count = count
                row_index = i  # \U0001f4dd Update row index if new maximum

        return [row_index, max_count]
