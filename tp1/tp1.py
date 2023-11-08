import numpy as np
from qiskit import *
from qiskit import Aer
from qiskit.visualization import plot_histogram, plot_state_city

circ = QuantumCircuit(3)

#draw circuit

circ.h(0)
circ.cx(0,1)
circ.h(2)
circ.cx(2,1)
circ.x(2)
circ.cx(2,0)
circ.x(2)
circ.barrier()
circ.swap(0,1)
circ.x(0)
circ.x(1)
circ.cx(2,1)
circ.x(2)
circ.cx(2,0)
circ.x(2)

print(circ.draw())

meas = QuantumCircuit(3)
meas.measure_all()

# backend = Aer.get_backend('statevector_simulator')
# job = backend.run(circ)
# result = job.result()
# outputState = result.get_statevector(circ,decimals = 3)
# print(outputState)
# plot_state_city(outputState, filename="state_city_plot.png")

backend = BasicAer.get_backend('qasm_simulator') # the device to run on
circ = circ.compose(meas)
result = backend.run(transpile(circ, backend), shots=1000).result()
counts  = result.get_counts(circ)
print(counts)
plot_histogram(counts,filename="output.png")
