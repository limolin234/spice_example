# Agent Tasks

Agents may help with:

- creating `sim/<mode>/tb.cir`;
- creating `sim/<mode>/sim.py`;
- generating `tb.par` from natural language;
- adding Python plots and simple post-processing;
- wiring an existing human-authored `cir/main.cir` into a testbench.

Agents should avoid:

- rewriting hand-authored circuit topology in `cir/` unless asked;
- turning circuit structure into large Python strings;
- inventing new directory conventions;
- putting sweeps in bash.

When asked to add a simulation:

1. Identify the case root.
2. Preserve existing `cir/` modules.
3. Create or update only the relevant `sim/` subtree.
4. Keep `sim.py` close to the fixed function shape.
5. Use `run.sh` as the launch entry.
