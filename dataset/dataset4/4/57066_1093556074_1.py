def enable_ki_protection(func):
    func._trio_keyboard_interrupt_protection_enabled = True
    return func