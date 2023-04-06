if version in git_tag and "dirty" not in commit_id:
    print_simplified_message()
else:
    print_current_message()