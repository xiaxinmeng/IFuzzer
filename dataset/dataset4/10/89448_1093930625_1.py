pointer_to_char_from_c_in_my_structure = POINTER(c_char)(my_structure_object.first_char)

print("\nContents of pointer_to_char_from_c_in_my_structure:")
print(pointer_to_char_from_c_in_my_structure.contents)
print("\npointer_to_char_from_c_in_my_Structure[0]:")
print(pointer_to_char_from_c_in_my_structure[0])

print("\nValues from my_structure_object:")
character_counter = 0
while character_counter < sizeof(my_structure_object):
    print(pointer_to_char_from_c_in_my_structure[character_counter])
    character_counter += 1