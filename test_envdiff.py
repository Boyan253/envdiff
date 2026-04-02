import envdiff


def test_parse_skips_comments_and_blanks():
    env = envdiff.parse_env("# comment\n\nA=1\n")
    assert env == {"A": "1"}

def test_parse_strips_quotes():
    assert envdiff.parse_env('A="hello world"')["A"] == "hello world"


def test_parse_handles_export_prefix():
    assert envdiff.parse_env("export A=1") == {"A": "1"}

def test_parse_keeps_equals_in_value():
    assert envdiff.parse_env("URL=postgres://a=b")["URL"] == "postgres://a=b"
