```python
from ibm_quantum_widgets import CircuitComposer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q0 = QuantumRegister(3, 'q0')
creg_c0 = ClassicalRegister(1, 'c0')
circuit = QuantumCircuit(qreg_q0, creg_c0)

circuit.reset(qreg_q0[0])
circuit.reset(qreg_q0[1])
circuit.reset(qreg_q0[2])
circuit.h(qreg_q0[0])
circuit.h(qreg_q0[1])
circuit.ccx(qreg_q0[0], qreg_q0[1], qreg_q0[2])
circuit.measure(qreg_q0[2], creg_c0[0])


editor = CircuitComposer(circuit=circuit)
editor
```




    CircuitComposer(circuit=<qiskit.circuit.quantumcircuit.QuantumCircuit object at 0x7f36b47f5cc0>)

