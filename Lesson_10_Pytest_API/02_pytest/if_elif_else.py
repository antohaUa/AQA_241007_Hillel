"""Min from four algorithm."""


def min_from_four(w, x, y, z):
    """Get min value from four defined elements."""
    if w <= x and w <= y and w <= z:
        return 'w'
    else:
        if x < w and x < y and x < z:
            return 'x'
        else:
            if y < x and y < w and y < z:
                return 'y'
            else:
                if z < w and z < x and z < y:
                    return 'z'
