import ast
import operator


operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}



def calculateResult(calculation):
    
    tree = ast.parse(calculation, mode="eval")
    
    def calculate(node):
        if isinstance(node, ast.Constant):
            return float(node.value)
        
        if isinstance(node, ast.BinOp):
            left = calculate(node.left)
            right = calculate(node.right)
            
            operation = operators[type(node.op)]
            
            return operation(left, right)
        
        if isinstance(node, ast.UnaryOp):
            value = calculate(node.operand)
            operation = operators[type(node.op)]
            
            return operation
        
        raise ValueError("Invalid Calculation")
    
    return calculate(tree.body)