
def find_expression():
    for a in ['+', '-', '*']:
        for b in ['+', '-', '*']:
            for c in ['+', '-', '*']:
                for d in ['+', '-', '*']:
                    expr = f"1{a}2{b}3{c}4{d}5"
                    try:
                        if eval(expr) == 25:
                            print(f"1 {a} 2 {b} 3 {c} 4 {d} 5 = 25")
                    except:
                        pass


