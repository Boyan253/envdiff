import envdiff


def test_parse_skips_comments_and_blanks():
    env = envdiff.parse_env("# comment\n\nA=1\n")
    assert env == {"A": "1"}

def test_parse_strips_quotes():
    assert envdiff.parse_env('A="hello world"')["A"] == "hello world"
