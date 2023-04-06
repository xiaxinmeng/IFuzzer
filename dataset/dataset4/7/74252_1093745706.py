import traits.api as trapi
import traitsui.api as trui

from traits.api import HasTraits, Str, Range, Enum

class Person(HasTraits):
    name = Str('Jane Doe')
    age = Range(low=0)
    gender = Enum('female', 'male')

person = Person(age=30)

from traitsui.api import Item, RangeEditor, View

person_view = View(
    Item('name'),
    Item('gender'),
    Item('age', editor=RangeEditor(mode='spinner')),
    buttons=['OK', 'Cancel'],
    resizable=True,
)


person.configure_traits(view=person_view)