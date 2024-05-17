from simplify import simplify, gate_dict
import numpy as np

def test(test_str):
    out = simplify(test_str)
    if type(out) is np.ndarray and len(out.shape) > 1:
        print(f"{test_str} = \n{out}")
    else:
        print(f"{test_str} = {out}")

if __name__=="__main__":
    test("H H")
    test("H Z")
    test("X Y")
    test("Y X")
    test("X Y X Y")
    test("H X Y I H X Y I")
    test("X Y Z X Y Z X Y Z X Y Z")
    test("j H Y H")
    test("j I")
    test("I j")
    test("X*X")
    test("I*I X*X I*I")
    test("H*H Z*Z H*H")

    # Identities:
    for gate in gate_dict.keys():
        for gate2 in gate_dict.keys():
            test(f"{gate} {gate2}")

    # Conjugations:
    for pauli in [" I ", " X ", " Y ", " Z "]:
        test("H" + pauli + "H")
        test("C_XYZ" + pauli + "C_ZYX")
        test("C_ZYX" + pauli + "C_XYZ")
        test("H_XY" + pauli + "H_XY")
        test("H_YZ" + pauli + "H_YZ")
        test("S" + pauli + "S_DAG")
        test("S_DAG" + pauli + "S")
        test("SQRT_X" + pauli + "SQRT_X_DAG")
        test("SQRT_X_DAG" + pauli + "SQRT_X")
        test("SQRT_Y" + pauli + "SQRT_Y_DAG")
        test("SQRT_Y_DAG" + pauli + "SQRT_Y")
