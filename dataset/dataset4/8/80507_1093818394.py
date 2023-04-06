class Bicycle:
       __slots__ = 'category', 'model', 'size', 'price'

Bicycle.category.__doc__ = 'Primary use: road, cross-over, or hybrid'
Bicycle.model.__doc__ = 'Unique six digit vendor-supplied code'
Bicycle.size.__doc__ = 'Rider size: child, small, medium, large, extra-large'
Bicycle.price.__doc__ = 'Manufacturer suggested retail price'