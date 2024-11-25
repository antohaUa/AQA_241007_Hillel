class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
        self._initialized = True  # flag to check that init done and both ( width and height are present)

    def __setattr__(self, key, value):
        if key in ("width", "height"):
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"{key} must be a positive number")
        super().__setattr__(key, value)

        # Automatically calculate the area
        if hasattr(self, '_initialized'):
            if key in ("width", "height"):
                super().__setattr__("area", self.width * self.height)


# Usage
rect = Rectangle(4, 5)
print(rect.area)  # Output: 20

rect.width = 6
print(rect.area)  # Output: 30
