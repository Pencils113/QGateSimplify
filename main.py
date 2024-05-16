from simplify import simplify, gate_dict

def test(test_str):
    print(f"{test_str} = {simplify(test_str)}")

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
