from email.headerregistry import HeaderRegistry
from email.policy import SMTP

def test_unstructured_encoded_word_folding():
    header = HeaderRegistry()('DKIM-Signature', 'a' * 85)
    folded = header.fold(policy=SMTP.clone(refold_source=None))
    print(f'\nDKIM-Signature: {header}')
    print(folded)
    assert '=?utf-8?q?' not in folded