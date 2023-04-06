from lxml.builder import E
from lxml import etree

tree = etree.ElementTree(
    E.Hello(
        "Good morning!",
        E.World("How do you do", humour = "excellent"),
        "Fine",
        E.Goodbye(),
        ),
    )