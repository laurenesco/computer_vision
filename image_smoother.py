# Given a 2D integer array img representing grayscale pixel values, return an array of the same size where each pixel is the average of itself and all its existing 8 neighbors (rounded down). Edge/corner pixels average over fewer neighbors.

# Input: img = [[1,1,1],
#               [1,0,1],
#               [1,1,1]]
# Output: [[0,0,0],
#          [0,0,0],
#          [0,0,0]]

# Constraints: 1 <= img.length, img[0].length <= 200, 0 <= img[i][j] <= 255
# Follow-up: Can you do it in O(1) extra space (in-place)?

from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """
        Given a 2D grid of grayscale pixel values, return a new grid where
        each cell is the floor average of itself and all existing
        8-directional neighbors.
        """
        
        if not img or not img[0]:
            return []
            
        rows = len(img)
        cols = len(img[0])
        
        output = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # For each img[row][col]
        for row in range(rows):
            for col in range(cols):
                
                total = 0
                neighbors = 0
                
                # print(f"in image, row: {row}, col: {col}")
            
                # Create small matrix to view neighbors
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        
                        # print(f"in kernel, row: {i}, col: {j}")
                
                        # If neighbor is valid, sum and increment neighbors
                        if i >= 0 and i < rows and j >= 0 and j < cols:
                            # print("valid neighbor")
                            total += img[i][j]
                            neighbors += 1
                
                # Calculate average and place it in output
                output[row][col] = total // neighbors

        return output


def run_tests():
    sol = Solution()

    test_cases = [
        # (input, expected_output)
        (
            [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]],
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
        ),
        (
            [[100, 200, 100],
             [200, 50, 200],
             [100, 200, 100]],
            [[137, 141, 137],
             [141, 138, 141],
             [137, 141, 137]]
        ),
        (
            [[5]],
            [[5]]
        ),
        (
            [[1, 2],
             [3, 4]],
            [[2, 2],
             [2, 2]]
        ),
    ]

    for i, (img, expected) in enumerate(test_cases):
        result = sol.imageSmoother(img)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: {status}")
        if status == "FAIL":
            print(f"  Input:    {img}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")


if __name__ == "__main__":
    run_tests()
