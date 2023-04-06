def v12_to_13(manager, case):
    with suppress(KeyError):
        case['sample_id'] = case.pop('caseid')