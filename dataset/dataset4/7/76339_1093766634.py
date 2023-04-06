@suppress(KeyError)
def v12_to_13(manager, case):
    case['sample_id'] = case.pop('caseid')