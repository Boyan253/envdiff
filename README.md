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
