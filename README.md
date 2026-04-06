# envdiff

> Compare .env files and tell you which keys are missing, extra or empty before the deploy fails.

## Why

The deploy fails at 6pm because someone added `REDIS_URL` to `.env.example` and
nobody added it to the server. `envdiff` catches that in CI in a second.
