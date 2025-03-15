import ast
import math

def safe_eval(expression):
    try:
        tree = ast.parse(expression, mode='eval')
        print(ast.dump(tree, indent=4)) 

        allowed_operators = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)
        # Expression:単一式, BinOp:二項演算子, Constant:数値, UnaryOp:単項演算(-x, +x), Pow:累乗, Call:関数
        allowed_nodes = (ast.Expression, ast.BinOp, ast.Constant, ast.UnaryOp, ast.Call)

        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp):
                if type(node.op) not in allowed_operators:
                    raise ValueError("使用できない演算子があるよ")
                if not isinstance(node.left, (ast.Constant, ast.BinOp, ast.UnaryOp, ast.Call)) or \
                   not isinstance(node.right, (ast.Constant, ast.BinOp, ast.UnaryOp, ast.Call)):
                    raise ValueError("安全な型ではないよ")

        return eval(expression, {"__builtins__": None}, {"math": math})
        
    except Exception as e:
        return f"エラー: {e}"

def calculator():
    while True:
        expression = input("計算式を入力 : ")

        if expression.lower() == "exit":
            print("電卓を終了")
            break

        result = safe_eval(expression)
        print("結果:", result)
        
calculator()