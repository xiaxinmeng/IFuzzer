def get_event_loop():
    current_loop = _get_running_loop()
    if current_loop is not None:
        return current_loop
    warnings.warn("...", DeprecationWarning)  
    return get_event_loop_policy().get_event_loop()