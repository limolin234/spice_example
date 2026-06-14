# Netlist Rules

Circuit modules:

- Use `.subckt ... .ends` for reusable topology.
- Use `X...` instances for subcircuits.
- Prefer explicit parameter passing:

```spice
Xb0 in out rlc_series RV={RV0} LV={LV0} CV={CV0}
```

Parameters:

- Define parameters in `.par` files:

```spice
.param RV0=10
```

- Reference parameters with braces:

```spice
R0 in out {RV0}
```

Top-level testbench:

- Only the direct ngspice entry file has `.end`.
- Include fragments such as `.par`, `.inc`, and subcircuit files should not contain `.end`.
- `tb.cir` should be a complete test platform, not a thin instantiation shell.
- Put excitation sources directly in `tb.cir`.
- Put analysis cards such as `.tran {TSTEP} {TSTOP}` outside `.control` when using parameter substitution.
- Use `.control` for `run` and `wrdata` in the fixed template.

Transient source:

```spice
V0 in 0 SIN(0 {VAMP} {FREQ} 0 0 0)
```

AC source:

```spice
V0 in 0 DC 0 AC {VAC} 0
```
