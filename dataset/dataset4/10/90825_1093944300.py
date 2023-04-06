
from difflib import SequenceMatcher

first = """
UNIQUESTRING
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
"""


second = """

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum  UNIQUESTRING
"""

sm = SequenceMatcher(None, first, second, autojunk=False)
print(sm.real_quick_ratio())
print(sm.quick_ratio())
print(sm.ratio())

print()

sm2 = SequenceMatcher(None, second, first, autojunk=False)
print(sm2.real_quick_ratio())
print(sm2.quick_ratio())
print(sm2.ratio())

