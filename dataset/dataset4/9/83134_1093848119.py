@example("#")
@example("\n\\\n")
@example("#\n\x0cpass#\n")
@given(source_code=hypothesmith.from_grammar().map(fixup).filter(str.strip))
def test_tokenize_round_trip_string(source_code):
    tokens = list(tokenize.generate_tokens(io.StringIO(source_code).readline))
    outstring = tokenize.untokenize(tokens)  # may have changed whitespace from source
    output = tokenize.generate_tokens(io.StringIO(outstring).readline)
    assert [(t.type, t.string) for t in tokens] == [(t.type, t.string) for t in output]