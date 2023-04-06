def mwh_nested_finally(output):
    try:
        output.append(2)
    finally:
        output.append(4)
        try:
            output.append(6)
        finally:
            output.append(8)
        output.append(9)

mwh_nested_finally.jump = (4, 9)
mwh_nested_finally.output = [2, 9]