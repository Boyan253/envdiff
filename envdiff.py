#!/usr/bin/env python3
"""Compare two .env files: missing keys, extra keys, empty values."""

import argparse
import sys


def parse_env(text):
    """Parse dotenv text into an ordered dict, ignoring comments and blanks."""
    out = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.lower().startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        out[key] = value
    return out


def compare(reference, actual):
    """Return (missing, extra, empty) key lists."""
    missing = [k for k in reference if k not in actual]
    extra = [k for k in actual if k not in reference]
    empty = [k for k in reference if k in actual and actual[k] == ""]
    return missing, extra, empty


def read(path):
    with open(path, encoding="utf-8") as fh:
        return parse_env(fh.read())


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("reference", help="the template, e.g. .env.example")
    ap.add_argument("actual", help="the real file, e.g. .env")
    ap.add_argument("--allow-extra", action="store_true",
                    help="do not fail on keys that are only in the real file")
    ap.add_argument("--allow-empty", action="store_true",
                    help="do not fail on keys present but blank")
    args = ap.parse_args(argv)

    missing, extra, empty = compare(read(args.reference), read(args.actual))
    for key in missing:
        print("missing  %s" % key)
    for key in empty:
        print("empty    %s" % key)
    for key in extra:
        print("extra    %s" % key)

    bad = bool(missing)
    bad = bad or (bool(empty) and not args.allow_empty)
    bad = bad or (bool(extra) and not args.allow_extra)
    if not (missing or extra or empty):
        print("env files agree", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
