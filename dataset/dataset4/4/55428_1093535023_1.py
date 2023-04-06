if 'license' in meta:
    if 'License' in meta['classifiers']:
        warnings.append('using a "license" keyword with a "License" classifier, please make sure the keyword does not duplicate the classifier but precises it')
    else:
        warnings.append('using a "license" keyword instead of a classifier, please make sure there is no classifier for this license')