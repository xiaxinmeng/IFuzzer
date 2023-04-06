class Super:
   params = {
       'name': 'John',
       'surname': 'Doe',
   }

class Sub(Super):
   params = Super.params + {
       'surname': 'Show',
       'age': 32,
   }