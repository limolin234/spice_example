import subprocess
from pathlib import Path

import numpy as np


ROOT = Path(__file__).parent.parent
OUTPUT = ROOT / "sim" / "output"


def write_params(path, params):
    with open(ROOT / path, "w") as f:
        for name, value in params.items():
            f.write(f".param {name}={value}\n")


def write_circuit_params():
    write_params("cir/main.par", {"RV": "1k"})


def write_sim_params():
    write_params(
        "sim/tb.par",
        {
            "TSTEP": "100u",
            "TSTOP": "10m",
            "VAMP": "1",
            "FREQ": "50",
            "PHASE": "0",
        },
    )


def run_ngspice():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ngspice", "-b", "sim/tb.cir"], cwd=ROOT)


def read_result():
    data = np.loadtxt(OUTPUT / "val.csv")
    return {
        "time": data[:, 0],
        "vin": data[:, 3],
    }


def plot_result(result):
    import matplotlib.pyplot as plt

    plt.figure()
    plt.plot(result["time"], result["vin"], label="vin")
    plt.xlabel("time / s")
    plt.ylabel("voltage / V")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT / "wave.png")
    plt.show()


def main():
    write_circuit_params()
    write_sim_params()
    run_ngspice()
    result = read_result()
    plot_result(result)


if __name__ == "__main__":
    main()
