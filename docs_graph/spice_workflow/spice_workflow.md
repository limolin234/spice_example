# SPICE Workflow

This project standardizes a small text-first ngspice workflow:

```text
human circuit topology -> Python-generated params -> ngspice -> Python plots
```

The template is intentionally simple. The goal is reliable agent assistance, not a general EDA framework.

The testbench is not split into a separate source fragment. `tb.cir` is the complete test platform: it includes test parameters, declares excitation sources, instantiates the DUT, selects the analysis, and writes output.

Stable examples:

- `example/`: minimal template.
- `three_phase_rlc_load/`: worked three-phase unbalanced RLC load example.

Use `run.sh` from an example root:

```bash
./run.sh
./run.sh ac
./run.sh tran
```

No argument runs `./sim/sim.py`. With an argument, it runs `./sim/$1/sim.py`.
