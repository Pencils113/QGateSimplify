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
