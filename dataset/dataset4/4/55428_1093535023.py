if 'platform' in meta:
    if 'Operating System' in meta['classifiers']:
        warnings.append('the "platform" keyword duplicates the "Platform" classifier')
    else:
        warnings.append('using a "platform" keyword instead of a classifier, please make sure there is no classifier for this platform')