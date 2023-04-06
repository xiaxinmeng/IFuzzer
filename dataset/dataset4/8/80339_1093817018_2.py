
named_entities = []
for entity in entities[0]:
   named_entities.append(name_regex.match(entity.trigger).group(1))
