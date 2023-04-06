def clamp(value=0.5, minimum=0, maximum=1):
    """Clamps the *value* between the *minimum* and *maximum* and returns it..

<And some extra explanatory documentation with examples>
"""

    return max(minimum, min(value, maximum))