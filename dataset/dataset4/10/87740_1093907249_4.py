ins1()  # insert 1 element in list, including empty list.
app1()  # append 1 element to list.  Same impact as with ins1()
list_ass_slice()  # can assign a sequence to a list slice, expanding list
list_inplace_repeat()  # No impact, early exit for len == 0
list_extend()  # Now used for list-literals of len > 2
list_pop() # No impact, same behavior for list becoming len == 0
list_ass_subscript()  # No impact, list_resize() only called for deletion