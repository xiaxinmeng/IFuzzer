# Look for a lower case letter, followed by
# a period, question mark or exclamation mark followed by 
# (maybe a quotation mark, followed by)
# a new line.
# This newline is only one whitespace character, but should be
# treated as two at the end of a sentence -- so add in a space.
fix_sentence_re = re.compile(r'([%s][\.\!\?][\"\']?)(\r\n|\n|\r)'
                             % string.lowercase)


if fix_sentence_endings:  text = re.sub(fix_sentence_re, r"\1 \2", text)