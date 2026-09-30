# ci-runner-fixture-py (public)

A small Python project used as a CI test fixture for
[DevAnsh-Digital-Solutions/github-action-runner](https://github.com/DevAnsh-Digital-Solutions/github-action-runner).
It has no functional purpose beyond giving the runner's Python checks
something real to lint, test, cover and scan.

`main` is green. Each failing path is exercised on its own branch:

| Branch | Change | Check that should fail |
|---|---|---|
| `fail/lint` | unused import + bad import order | lint |
| `fail/unit-test` | a deliberately wrong assertion | unit test |
| `fail/coverage` | an untested module drags coverage below 80% | coverage |
| `fail/secret-scan` | an obviously fake credential | secret scan |

The workflow (`.github/workflows/ci.yml`) enables lint, unit test, coverage and secret scan (no dependency scan), scoped per the
runner's `docs/CHECK-POLICY.md`.
