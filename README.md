## Leveraging AI in RSA Factorization Using Shor's Algorithm on IBM Quantum Experience

**Author: Dominic Udousoro <dominicudousoro@gmail.com>**

This study adopted a structured experimental approach leveraging IBM Quantum Experience for RSA key factorization using Shor’s algorithm and AI models for monitoring and analysis of the impact of quantum computing advancements on the security of classical cryptographic protocols and explores the role of Artificial Intelligence (AI) in developing quantum-resilient cybersecurity solutions.

# Experimental Setup
The IBM Quantum Experience platform was selected as the quantum computing platform for its access to both simulators and real quantum hardware. It offers flexibility and credibility for experimentation. Real devices such as ibmq_manila and ibmq_guadalupe were employed to account for real-world noise and constraints in quantum computations. TensorFlow and Scikit-learn Python-based libraries were used to develop machine learning models to analyze quantum computation outcomes and identify patterns in the RSA keys factorization.

# RSA Key Selection
RSA keys of varying sizes (N=15, 21, 35, 39) were selected due to the current qubit limitations of publicly accessible quantum hardware. These keys provided a manageable basis to evaluate the effectiveness of Shor’s algorithm.

# RSA Keys for the experiment
rsa_keys = [15, 21, 35, 39]

# Quantum Circuit Design and Execution
The study implemented Shor’s algorithm using Qiskit to construct the quantum circuits required for factorizing RSA keys. These circuits were executed on both simulators (Qiskit Aer) and real quantum hardware to evaluate performance discrepancies.

# AI Integration for Analysis
AI models were developed to process outputs from the quantum experiments. Using logistic regression and neural networks, these models predicted patterns in factorization success rates and identified trends based on RSA key size and quantum backend performance.


