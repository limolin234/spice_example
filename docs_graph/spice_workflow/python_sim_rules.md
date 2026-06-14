# Python Simulation Rules

Every `sim.py` should use this simple function shape:

```python
write_circuit_params()
write_sim_params()
run_ngspice()
result = read_result()
plot_result(result)
```

Fixed responsibilities:

- `write_circuit_params`: writes `cir/main.par`.
- `write_sim_params`: writes `sim/tb.par` or `sim/<mode>/tb.par`.
- `run_ngspice`: runs `ngspice -b .../tb.cir` from the case root.
- `read_result`: reads `output/val.csv`.
- `plot_result`: writes plot files under `output/`.

`tb.cir` contains the excitation source statements directly. Python changes their values by writing `tb.par`, not by generating a separate source file.

Python may perform parameter sweeps. ngspice should still perform internal analysis sweeps such as `.tran`, `.ac`, or `.dc`.

Do not use bash loops for experiment logic.
