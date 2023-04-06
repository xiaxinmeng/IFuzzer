import weakref

## this works:
def testF( event ):    pass
r = weakref.ref( testF )

## this doesnt:
class EventListener:
    def handleEventA( self, event ):
        pass

t = EventListener()
## gives a "dead" ref
r = weakref.ref( t.handleEventA )