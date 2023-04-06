from enum import IntEnum

class myIntEnum(IntEnum):
    x = 1
    
    def __str__(self):
        return 'aaaaAAAa'
    
f'{myIntEnum.x}, {str(myIntEnum.x)}'