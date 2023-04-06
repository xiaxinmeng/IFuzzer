if is_backtrack_point: # may backtrack if the tail fail
    LASTMARK_SAVE()
elif is_repeat_body:   # is a sub-pattern inside (...)* or (...)*?
    LASTMARK_SAVE()
    MARK_PUSH()