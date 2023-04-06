
name_regex = compile(r'\[\"([a-zA-Z\s]*)\"{1}')

named_entities = [name_regex.match(entity.trigger).group(1) for entity in entities[0]]
