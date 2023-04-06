from bisect import *

less_than = lambda x,y: x[:3]<y[:3]
lp = bisect_left(word_list, given_rev_word, lt=less_than)
rp = bisect_right(word_list, given_rev_word, lt=less_than)
# return the union of flag_list[lp:rp]