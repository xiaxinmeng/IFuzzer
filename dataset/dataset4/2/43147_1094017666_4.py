if newChild.parentNode is not None:
   newChild.parentNode.removeChild(newChild)
if newChild is oldChild:
   return