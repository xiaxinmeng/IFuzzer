# Implementation note:
# The class keeps compatibility with AbstractChildWatcher ABC
# To achieve this it has empty attach_loop() method
# and doesn't accept explicit loop argument
# for add_child_handler()/remove_child_handler()
# but retrieves the current loop by get_running_loop()