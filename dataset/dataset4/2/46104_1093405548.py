def direction(pt1, pt2):
    """angle of line segment from point 1 to point 2"""
    return atan2(pt2.y - pt1.y, pt2.x - pt1.x)

my_points.sort(key=lambda pt: direction(reference_pt, pt))