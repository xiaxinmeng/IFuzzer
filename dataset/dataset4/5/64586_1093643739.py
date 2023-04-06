def test_tokenize():
    input = "if False:\n\tx=3\n\ty=3\n"
    g = list(generate_tokens(io.StringIO(input).readline))
    assert untokenize(g) == input