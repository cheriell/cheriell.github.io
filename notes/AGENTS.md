---
layout: default
title: AI Agent Guide
---

# AI Agent Guide


```markdown
# AI Agent Guide


## AI Agents: Code of Conduct

Please follow these rules in our collaboration.

Dos and Don'ts:

- Prefer minimal changes. Only update code that is necessary
for the requested modification.
- Avoid large multi-file refactors unless explicitly requested.
- Avoid modifying existing config YAML files. Create a new config file instead and override only the necessary parameters.
- Always ask before attempting to run commands.
- Never add/commit git changes.

Before editing code:

- Identify the relevant files.
- Explain the change briefly.
- Propose edits.
- Ask for approval before start editing.


## Read Important Docs

How-to for AI agents:

- [TASK_RECIPES.md](./docs/TASK_RECIPES.md): How to do tasks.

Understanding the project and the codebase:

- [PROJECT_CONTEXT.md](./docs/PROJECT_CONTEXT.md): Understanding the project, including stages in the experimental pipeline and what we are up to now.
- [REPO_INDEX.md](./docs/REPO_INDEX.md): Navigating this repository.

When unsure about project structure or experiment logic,
read PROJECT_CONTEXT.md and REPO_INDEX.md before exploring the repository.

Understanding the experiments:

- [EXP_REGISTRY.md](./docs/EXP_REGISTRY.md): Understanding experiments.
- [CONFIG_MAP.md](./docs/CONFIG_MAP.md): Understanding hydra configuration files for various experiments.

## Running Experiments

Short running instruction to help with getting started. More information in [PROJECT_CONTEXT](./docs/PROJECT_CONTEXT.md).

Current experiments are launched using:

    python3 train.py --config-path=configs/runs --config-name=<run-name>
```