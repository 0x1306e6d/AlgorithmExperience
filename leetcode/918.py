import sys
import unittest

from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        arr = A + A

        max_subarray_sum = -sys.maxsize
        subarray = []
        subarray_sum = 0
        for i in arr:
            if subarray_sum + i > i:
                if len(subarray) >= len(A):
                    next_subarray = subarray[1:]
                    while next_subarray:
                        if next_subarray[0] <= 0:
                            next_subarray.pop(0)
                        else:
                            break
                    next_subarray.append(i)

                    subarray = next_subarray
                    subarray_sum = sum(next_subarray)
                else:
                    subarray.append(i)
                    subarray_sum = subarray_sum + i
            else:
                subarray = [i]
                subarray_sum = i
            max_subarray_sum = max(max_subarray_sum, subarray_sum)

        return max_subarray_sum


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        A = [1, -2, 3, -2]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.maxSubarraySumCircular(A), output)

    def test_example2(self):
        # Input
        A = [5, -3, 5]
        # Output
        output = 10

        solution = Solution()
        self.assertEqual(solution.maxSubarraySumCircular(A), output)

    def test_example3(self):
        # Input
        A = [3, -1, 2, -1]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.maxSubarraySumCircular(A), output)

    def test_example4(self):
        # Input
        A = [3, -2, 2, -3]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.maxSubarraySumCircular(A), output)

    def test_example5(self):
        # Input
        A = [-2, -3, -1]
        # Output
        output = -1

        solution = Solution()
        self.assertEqual(solution.maxSubarraySumCircular(A), output)


if __name__ == "__main__":
    unittest.main()
