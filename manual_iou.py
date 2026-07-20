def calculate_iou(box1, box2):
    """
    Calculate Intersection over Union (IoU) between two bounding boxes.

    Parameters:
        box1 (list or tuple): [x1, y1, x2, y2] — top-left and bottom-right coordinates
        box2 (list or tuple): [x1, y1, x2, y2] — top-left and bottom-right coordinates

    Returns:
        float: IoU value between 0 and 1
    """
    
    # Get intersection coordinates
    x_left = max(box1[0], box2[0])
    y_top = max(box1[1], box2[1])
    x_right = min(box1[2], box2[2])
    y_bottom = min(box1[3], box2[3])
    
    # Calculate area of intersection 
    inter_w = max(x_right - x_left, 0)
    inter_h = max(y_bottom - y_top, 0)
    inter_area = inter_w * inter_h
    
    # Calculate area of both original boxes
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    
    # Calculate union area
    union_area = box1_area + box2_area - inter_area
    
    if union_area == 0:
        return 0
        
    IoU = inter_area / union_area
    
    return IoU
    
box_a = [50, 50, 150, 150]   # [x1, y1, x2, y2]
box_b = [100, 100, 200, 200]

iou_value = calculate_iou(box_a, box_b)
print(f"IoU: {iou_value:.4f}")  # Output: IoU: 0.1429
