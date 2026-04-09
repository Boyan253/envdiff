# envdiff

> Compare .env files and tell you which keys are missing, extra or empty before the deploy fails.

## Why

The deploy fails at 6pm because someone added `REDIS_URL` to `.env.example` and
nobody added it to the server. `envdiff` catches that in CI in a second.

## Usage

```
python envdiff.py .env.example .env
python envdiff.py .env.example .env --allow-extra
python envdiff.py .env.production.example .env.production --allow-empty
```

Exit code is 1 if anything is wrong, so it drops straight into a pipeline.

## Output

```
missing  REDIS_URL
empty    STRIPE_SECRET
extra    OLD_FEATURE_FLAG
```

| line | meaning |
|------|---------|
| `missing` | in the template, absent from the real file — always an error |
| `empty`   | present but blank — error unless `--allow-empty` |
| `extra`   | only in the real file — error unless `--allow-extra` |

## Parsing rules

- `#` comments and blank lines are ignored.
- `export FOO=bar` is accepted.
- Surrounding single or double quotes are stripped.
- Only the first `=` splits, so connection strings survive intact.
