import numpy as np

gate_dict = {
    # Pauli gates
    "I"          : np.array([[1, 0], [0, 1]]),
    "X"          : np.array([[0, 1], [1, 0]]),
    "Y"          : np.array([[0, -1j], [1j, 0]]),
    "Z"          : np.array([[1, 0], [0, -1]]),
    # Clifford gates
    "H"          : np.array([[1, 1], [1, -1]]) / np.sqrt(2),
    "jI"         : np.array([[1j, 0], [0, 1j]]),
    "C_XYZ"      : np.array([[1-1j, -1-1j], [1-1j, 1+1j]]) / 2,
    "C_ZYX"      : np.array([[1+1j, 1+1j], [-1+1j, 1-1j]]) / 2,
    "H_XY"       : np.array([[0, 1-1j], [1+1j, 0]]) / np.sqrt(2),
    "H_YZ"       : np.array([[1, -1j], [1j, -1]]) / np.sqrt(2),
    "S"          : np.array([[1, 0], [0, 1j]]),
    "S_DAG"      : np.array([[1, 0], [0, -1j]]),
    "SQRT_X"     : np.array([[1+1j, 1-1j], [1-1j, 1+1j]]) / 2,
    "SQRT_X_DAG" : np.array([[1-1j, 1+1j], [1+1j, 1-1j]]) / 2,
    "SQRT_Y"     : np.array([[1+1j, -1-1j], [1+1j, 1+1j]]) / 2,
    "SQRT_Y_DAG" : np.array([[1-1j, 1-1j], [-1+1j, 1-1j]]) / 2,
}

clifford_pauli_dict = {
    "H X"          : np.matmul(gate_dict["H"], gate_dict["X"]),
    "X H"          : np.matmul(gate_dict["X"], gate_dict["H"]),
    "Y H"          : np.matmul(gate_dict["Y"], gate_dict["H"]),

    "C_XYZ X"      : np.matmul(gate_dict["C_XYZ"], gate_dict["X"]),
    "X C_XYZ"      : np.matmul(gate_dict["X"], gate_dict["C_XYZ"]),
    "Y C_XYZ"      : np.matmul(gate_dict["Y"], gate_dict["C_XYZ"]),
    "Z C_XYZ"      : np.matmul(gate_dict["Z"], gate_dict["C_XYZ"]),

    "C_ZYX X"     : np.matmul(gate_dict["C_ZYX"], gate_dict["X"]),
    "X C_ZYX"     : np.matmul(gate_dict["X"], gate_dict["C_ZYX"]),
    "Y C_ZYX"     : np.matmul(gate_dict["Y"], gate_dict["C_ZYX"]),

    "H_XY X"       : np.matmul(gate_dict["H_XY"], gate_dict["X"]),
    "X H_XY"       : np.matmul(gate_dict["X"], gate_dict["H_XY"]),
    "Y H_XY"       : np.matmul(gate_dict["Y"], gate_dict["H_XY"]),
    "Z H_XY"       : np.matmul(gate_dict["Z"], gate_dict["H_XY"]),

    "H_YZ X"       : np.matmul(gate_dict["H_YZ"], gate_dict["X"]),
    "X H_YZ"       : np.matmul(gate_dict["X"], gate_dict["H_YZ"]),
    "Y H_YZ"       : np.matmul(gate_dict["Y"], gate_dict["H_YZ"]),
    "Z H_YZ"       : np.matmul(gate_dict["Z"], gate_dict["H_YZ"]),

    "S X"          : np.matmul(gate_dict["S"], gate_dict["X"]),
    "X S"          : np.matmul(gate_dict["X"], gate_dict["S"]),
    "Y S"          : np.matmul(gate_dict["Y"], gate_dict["S"]),
    "H S"          : np.matmul(gate_dict["H"], gate_dict["S"]),

    "S_DAG X"      : np.matmul(gate_dict["S_DAG"], gate_dict["X"]),
    "X S_DAG"      : np.matmul(gate_dict["X"], gate_dict["S_DAG"]),
    "Y S_DAG"      : np.matmul(gate_dict["Y"], gate_dict["S_DAG"]),
    "H S_DAG"      : np.matmul(gate_dict["H"], gate_dict["S_DAG"]),
    "H_XY S_DAG"   : np.matmul(gate_dict["H_XY"], gate_dict["S_DAG"]),
    "H_YZ S_DAG"  : np.matmul(gate_dict["H_YZ"], gate_dict["S_DAG"]),

    "SQRT_X X"     : np.matmul(gate_dict["SQRT_X"], gate_dict["X"]),
    "X SQRT_X"     : np.matmul(gate_dict["X"], gate_dict["SQRT_X"]),
    "Y SQRT_X"     : np.matmul(gate_dict["Y"], gate_dict["SQRT_X"]),
    "H SQRT_X"     : np.matmul(gate_dict["H"], gate_dict["SQRT_X"]),
    "H_XY SQRT_X"  : np.matmul(gate_dict["H_XY"], gate_dict["SQRT_X"]),

    "SQRT_X_DAG X" : np.matmul(gate_dict["SQRT_X_DAG"], gate_dict["X"]),
    "X SQRT_X_DAG" : np.matmul(gate_dict["X"], gate_dict["SQRT_X_DAG"]),
    "Y SQRT_X_DAG" : np.matmul(gate_dict["Y"], gate_dict["SQRT_X_DAG"]),
    "H SQRT_X_DAG" : np.matmul(gate_dict["H"], gate_dict["SQRT_X_DAG"]),

    "SQRT_Y X"     : np.matmul(gate_dict["SQRT_Y"], gate_dict["X"]),
    "X SQRT_Y"     : np.matmul(gate_dict["X"], gate_dict["SQRT_Y"]),
    "Y SQRT_Y"     : np.matmul(gate_dict["Y"], gate_dict["SQRT_Y"]),
    "H SQRT_Y"     : np.matmul(gate_dict["H"], gate_dict["SQRT_Y"]),
    "H_YZ SQRT_Y"  : np.matmul(gate_dict["H_YZ"], gate_dict["SQRT_Y"]),

    "SQRT_Y_DAG X" : np.matmul(gate_dict["SQRT_Y_DAG"], gate_dict["X"]),
    "X SQRT_Y_DAG" : np.matmul(gate_dict["X"], gate_dict["SQRT_Y_DAG"]),
    "Y SQRT_Y_DAG" : np.matmul(gate_dict["Y"], gate_dict["SQRT_Y_DAG"]),
    "H SQRT_Y_DAG" : np.matmul(gate_dict["H"], gate_dict["SQRT_Y_DAG"]),
    "H_XY SQRT_Y_DAG" : np.matmul(gate_dict["H_XY"], gate_dict["SQRT_Y_DAG"]),
}


def decode(gate):
    for key in gate_dict.keys():
        if np.allclose(gate, gate_dict[key]):
            return key
        
    for key in gate_dict.keys():
        if np.allclose(gate, -1 * gate_dict[key]):
            return "-" + key
    
    for key in gate_dict.keys():
        if np.allclose(gate, 1j * gate_dict[key]):
            return "j" + key
        
    for key in gate_dict.keys():
        if np.allclose(gate, -1j * gate_dict[key]):
            return "-j" + key
        
    for key in clifford_pauli_dict.keys():
        if np.allclose(gate, clifford_pauli_dict[key]):
            return key
        
    for key in clifford_pauli_dict.keys():
        if np.allclose(gate, -1 * clifford_pauli_dict[key]):
            return "-" + key
    
    for key in clifford_pauli_dict.keys():
        if np.allclose(gate, 1j * clifford_pauli_dict[key]):
            return "j" + key
        
    for key in clifford_pauli_dict.keys():
        if np.allclose(gate, -1j * clifford_pauli_dict[key]):
            return "-j" + key
        
    return gate


def simplify(str_i, raw=False):
    ins = str_i.replace('j', 'jI').replace('II', 'I').split(' ')
    for i in range(len(ins)):
        ins[i] = gate_dict[ins[i]]

    result = gate_dict["I"]

    for gate in ins:
        result = np.matmul(result, gate)

    if not raw:
        return decode(result)
    
    return result