import logging
logging.basicConfig(format='%(asctime)s %(message)s')

def sensitive_function(new_admin: str) -> None:
    logging.warning("hey sysadmin you should give admin access to %s", new_admin)

def process_request(some_user_input: str) -> None:
    logging.warning("totally regular thing happened, and it was %s", some_user_input)