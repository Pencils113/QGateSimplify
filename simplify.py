import numpy as np

gate_dict = {
    "I" : np.array([[1, 0], [0, 1]]),
    "X" : np.array([[0, 1], [1, 0]]),
    "Y" : np.array([[0, -1j], [1j, 0]]),
    "Z" : np.array([[1, 0], [0, -1]]),
    "H" : np.array([[1, 1], [1, -1]]) / np.sqrt(2),
    "HX" : np.array(([1, 1], [-1, 1])) / np.sqrt(2),
    "XH" : np.array(([1, -1], [1, 1])) / np.sqrt(2),
    "YH" : np.array(([-1j, 1j], [1j, 1j])) / np.sqrt(2),
    "jI" : np.array([[1j, 0], [0, 1j]])
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