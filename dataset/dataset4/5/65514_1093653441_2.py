import email._header_value_parser, email.headerregistry
def get_unstructured(value):
    value = value.replace("=?UTF-8?Q?=20", " =?UTF-8?Q?")
    return email._header_value_parser.get_unstructured(value)
email.headerregistry.UnstructuredHeader.value_parser = staticmethod(get_unstructured)