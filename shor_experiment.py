# RSA FACTORIZATION USING SHOR'S ALGORITHM ON IBM QUANTUM EXPERIENCE
# AUTHOR: DOMINIC UDOUSORO <dominicudousoro@gmail.com>

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.visualization import plot_histogram
from math import gcd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Initialize IBM Quantum Service
# Replace with your API token or use your saved credentials
service = QiskitRuntimeService(channel='ibm_quantum')

# Step 2: Parameters for Shor's Algorithm
N = 15  # Number to factorize
a = 7   # Chosen co-prime to N (arbitrary for this example)

# Step 3: GCD Check
if gcd(a, N) != 1:
    print(f"{a} is not co-prime with {N}, choose a different 'a'")
else:
    print(f"Proceeding with a={a}, co-prime with N={N}")

# Step 4: Quantum Circuit Construction
# Number of qubits: 2n (work qubits) + n (result qubits) + 1 (auxiliary qubit)
num_qubits = 4  # Adjust based on your simulator or hardware constraints
qc = QuantumCircuit(num_qubits + 1, num_qubits)

# Apply Hadamard gates for superposition
for i in range(num_qubits):
    qc.h(i)

# Step 5: Modular Exponentiation Circuit (Simplified Placeholder)
# Replace with detailed implementation of a modular exponentiation circuit
# This step computes |x⟩ -> |x, a^x mod N⟩
qc.cx(0, num_qubits)  # Simplified example gate (modular exponentiation logic)

# Step 6: Apply Quantum Fourier Transform (QFT)
# This is the inverse QFT logic for period finding
for qubit in range(num_qubits // 2):
    qc.swap(qubit, num_qubits - qubit - 1)
for j in range(num_qubits):
    for k in range(j):
        qc.cp(np.pi / (2 ** (j - k)), k, j)
    qc.h(j)

# Step 7: Measurement
qc.measure(range(num_qubits), range(num_qubits))

# Step 8: Set Up the Simulator
simulator = AerSimulator()

# Compile and Run the Circuit
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)

# Step 9: Collect and Visualize Results
result = job.result()
counts = result.get_counts()
print(f"Measurement Counts: {counts}")

# Plot the histogram
plot_histogram(counts)
plt.title(f"Measurement Results for Shor's Algorithm (N={N}, a={a})")
plt.show()

