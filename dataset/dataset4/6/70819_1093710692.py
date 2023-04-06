factory = DateFactory()
factory.reset()
today = factory.today
now = factory.now
layers.MockAndMonkeyLayer.register_reset(factory.reset)

__all__.extend([
    'factory',
    'now',
    'today',
    ])