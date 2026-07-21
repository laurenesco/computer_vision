from typing import List

"""
1. Image Convolution with Zero Padding

Problem:
You are given a grayscale image represented as a 2D integer matrix image of size m x n, and a square convolution kernel kernel of size k x k (k is odd). Apply the convolution operation to the image using zero-padding so that the output image has the same dimensions as the input image.

Convolution here means: for each output pixel, flip the kernel both horizontally and vertically, then compute the sum of element-wise products with the corresponding neighborhood in the (zero-padded) input image.

Return the resulting image as a 2D list of integers.

Constraints:

1 <= m, n <= 200
1 <= k <= min(m, n), k is odd
-1000 <= image[i][j] <= 1000
-10 <= kernel[i][j] <= 10
The output values do not need to be clipped/normalized — return raw integer sums.
"""

class Solution:
    def convolve2D(self, image: List[List[int]], kernel: List[List[int]]) -> List[List[int]]:
        
        # Get dimensions
        img_h = len(image)
        img_w = len(image[0])
        ker_h = len(kernel)
        ker_w = len(kernel[0])
        
        # Flip kernel
        flipped_kernel = [row[::-1] for row in kernel[::-1]]
        
        # Set up padded image
        pad = ker_h // 2
        padded = [[0 for _ in range (img_w + 2 * pad)] for _ in range (img_h + 2 * pad)]
        for i in range(img_h):
            for j in range(img_w):
                padded[i + pad][j + pad] = image[i][j]
        
        output = [[0 for _ in range(img_w)] for _ in range(img_h)]
        
        # Iterate over output
        for row in range(img_h):
            for col in range(img_w):
                kernel_sum = 0
                
                # Get element wise sum
                for ker_row in range(ker_h):
                    for ker_col in range(ker_w):
                        
                        kernel_sum += padded[row + ker_row][col + ker_col] * kernel[ker_row][ker_col]
                        
                    output[row][col] = kernel_sum

        return output


def run_tests():
    sol = Solution()
    test_cases = [
        {
            "image": [[1,2,3],
                      [4,5,6],
                      [7,8,9]],
            "kernel": [[0,0,0],
                       [0,1,0],
                       [0,0,0]],
            "expected": [[1,2,3],
                         [4,5,6],
                         [7,8,9]]
        },
        {
            "image": [[1,1,1],
                      [1,1,1],
                      [1,1,1]],
            "kernel": [[1,1,1],
                       [1,1,1],
                       [1,1,1]],
            "expected": [[4,6,4],
                         [6,9,6],
                         [4,6,4]]
        },
        {
            "image": [[5]],
            "kernel": [[2]],
            "expected": [[10]]
        },
        {
            "image": [[1,2],
                      [3,4]],
            "kernel": [[0,1],
                       [0,0]],
            "expected": [[2,0],
                         [4,0]]
        },
    ]

    passed = 0
    for i, tc in enumerate(test_cases):
        result = sol.convolve2D(tc["image"], tc["kernel"])
        ok = result == tc["expected"]
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i + 1}: {status}")
        if not ok:
            print(f"  Input image:  {tc['image']}")
            print(f"  Kernel:       {tc['kernel']}")
            print(f"  Expected:     {tc['expected']}")
            print(f"  Got:          {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed.")


if __name__ == "__main__":
    run_tests()
