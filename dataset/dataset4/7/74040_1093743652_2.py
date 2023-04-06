readline.read_history_file(".history")

print("current_history_length", readline.get_current_history_length())
print("history_length", readline.get_history_length())
print("history_get_item(1)", readline.get_history_item(1))
print("history_get_item(1000)", readline.get_history_item(1000))

input()

readline.write_history_file(".history")