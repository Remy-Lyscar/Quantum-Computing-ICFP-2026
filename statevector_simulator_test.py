import numpy as np
import matplotlib.pyplot as plt

from tools import Circuit, gate_dic
from state_vector_qpu import State, StateVectorQPU

# a couple of tests
psi = State(2)
assert(np.linalg.norm(psi.to_vec() - np.array([1, 0, 0, 0]))<1e-13)

psi.apply(gate_dic["H"], [0])
assert(np.linalg.norm(psi.to_vec() - np.array([1, 0, 1, 0])/np.sqrt(2))<1e-13)

psi.apply(gate_dic["CNOT"], [0, 1])
assert(np.linalg.norm(psi.to_vec() - np.array([1, 0, 0, 1])/np.sqrt(2))<1e-13)

psi.apply(gate_dic["CNOT"], [0, 1])
assert(np.linalg.norm(psi.to_vec() - np.array([1, 0, 1, 0])/np.sqrt(2))<1e-13)

psi.apply(gate_dic["CNOT"], [1, 0])
assert(np.linalg.norm(psi.to_vec() - np.array([1, 0, 1, 0])/np.sqrt(2))<1e-13)

psi.apply(gate_dic["RY"](np.pi/2), [1])
assert(np.linalg.norm(psi.to_vec() - np.array([1, 1, 1, 1])/2)<1e-13)

