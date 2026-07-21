def convolve2d(image, kernel, stride=1):
    p = 0
    stride = 1
    
    # Step 1: Get image and filter dimensions
    img_h = len(image)
    img_w = len(image[0])
    ker_h = len(kernel)
    ker_w = len(kernel[0])
    
    # Step 2: Calculate output dimensions
    
    # Calculate output size
    out_h = (img_h - ker_h + 2*p) // stride + 1
    out_w = (img_w - ker_w + 2*p) // stride + 1
    
    # Step 3: Create output image
    output = [[0.0 for _ in range(out_w)] for _ in range(out_h)]
    
    # Step 4: Slide filter over image
    for out_row in range(out_h):
        for out_col in range (out_w):
            
            accumulated = 0.0
            
            # Step 5: Perform element-wise multiply and then sum
            for ker_row in range (ker_h):
                for ker_col in range (ker_w):
                    
                    # Map kernel coords to image coords
                    img_row = out_row * stride + ker_row
                    img_col = out_col * stride + ker_col
                    
                    accumulated += kernel[ker_row][ker_col] * image[img_row][img_col]
                
            # Step 6: Store the result in output
            output[out_row][out_col] = accumulated
    
    # Step 7: Return feature map
    return output
    
# Box blur (averaging)
box_blur = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
]

# Edge detection (Sobel - horizontal edges)
sobel_x = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
]

# Gaussian blur (approximation)
gaussian = [
    [1/16, 2/16, 1/16],
    [2/16, 4/16, 2/16],
    [1/16, 2/16, 1/16],
]
    
image = [
    [10, 10, 10, 10, 10],
    [10, 50, 50, 50, 10],
    [10, 50, 50, 50, 10],
    [10, 50, 50, 50, 10],
    [10, 10, 10, 10, 10],
]

# Sharpening kernel
kernel = [
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0],
]

result = convolve2d(image, gaussian)

for row in result:
    print([int(v) for v in row])
