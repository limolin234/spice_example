# Agent Guide

This template uses a text-first ngspice workflow. Read the docs graph first:

- `docs_graph/spice_workflow/spice_workflow.md`
- `docs_graph/spice_workflow/file_structure.md`
- `docs_graph/spice_workflow/agent_tasks.md`

Hard rules:

1. Do not replace hand-written circuit topology with Python-generated netlists unless explicitly asked.
2. Human-authored circuit modules live under `cir/`; agents normally help connect testbenches and Python simulation scripts.
3. Python simulation scripts use the fixed workflow: generate parameters, run ngspice, read output, plot.
4. Shell scripts are only launch glue; do not put parameter sweeps in bash.
