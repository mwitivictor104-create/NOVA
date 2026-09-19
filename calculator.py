"""
NOVA Calculator
Safe mathematical expression evaluator.
"""

import ast
import operator
import math


_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


_FUNCTIONS = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "abs": abs,
}


def _evaluate(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Invalid value")

    if isinstance(node, ast.Num):
        return node.n

    if isinstance(node, ast.BinOp):
        operation = _OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Operator not allowed")

        left = _evaluate(node.left)
        right = _evaluate(node.right)

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        operation = _OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Operator not allowed")

        return operation(_evaluate(node.operand))

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Function not allowed")

        function = _FUNCTIONS.get(node.func.id)

        if function is None:
            raise ValueError("Function not allowed")

        arguments = [_evaluate(arg) for arg in node.args]

        return function(*arguments)

    raise ValueError("Invalid expression")


def calculate(expression):
    """
    Calculate a mathematical expression.

    Examples:
        calculate("25*4")
        calculate("100/5")
        calculate("sqrt(144)")
    """

    if not expression:
        return None

    expression = str(expression).strip()

    if len(expression) > 200:
        raise ValueError("Expression is too long")

    tree = ast.parse(expression, mode="eval")

    result = _evaluate(tree.body)

    if isinstance(result, float) and result.is_integer():
        return int(result)

    return result


def calculator(expression):
    """Compatibility alias for NOVA."""
    return calculate(expression)
