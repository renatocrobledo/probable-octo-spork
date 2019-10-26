def eval_postfix(text):
    s = list()
    for symbol in text:
        if symbol in "0123456789":
            s.append(int(symbol))
            plus = None
        elif not s.is_empty():
            if symbol == "+":
                plus = s.pop() + s.pop()
            elif symbol == "-":
                plus = s.pop() - s.pop()
            elif symbol == "*":
                plus = s.pop() * s.pop()
            elif symbol == "/":
                plus = s.pop() / s.pop()
        if plus is not None:
            s.append(plus)
        else:
             raise Exception("unknown value %s"%symbol)
    return s.pop()


eval_postfix('243')