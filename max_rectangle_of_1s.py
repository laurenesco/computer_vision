# 2. Max Rectangle of 1s (Region of Interest Detection)

# Given a binary matrix mask (output of an object segmentation model, where 1 = foreground pixel), find the largest axis-aligned rectangle containing only 1s, and return its area. This simulates finding the tightest bounding box of solid foreground within a noisy mask.

# Input: mask = [[1,0,1,0,0],
#                [1,0,1,1,1],
#                [1,1,1,1,1],
#                [1,0,0,1,0]]
# Output: 6

# Constraints: rows, cols <= 200
# Follow-up: Solve in O(rows × cols) time using a histogram + stack approach.
