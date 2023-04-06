
lists_to_filter = [
    ['a', 'exclude'],
    ['b']
]
# notice that when 'exclude' is the last element, the code returns the expected result
for exclude_label in ['exclude', 'something']:
    lists_to_filter = (labels_list for labels_list in lists_to_filter if exclude_label not in labels_list)
    # notice that changing the line above to the commented line below (i.e. expanding the generator to a list) will make the code output the expected result, 
    # i.e. the issue is only when using filter on another filter, and not on a list
    # lists_to_filter = [labels_list for labels_list in lists_to_filter if exclude_label not in labels_list]
lists_to_filter = list(lists_to_filter)
print(lists_to_filter)
