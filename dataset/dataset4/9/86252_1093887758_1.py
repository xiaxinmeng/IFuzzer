import ast
from collections import defaultdict

def collect_contexts(tree):
    contexts = defaultdict(list)
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            contexts[node.ctx].append(node.id)
    return contexts
    
print(collect_contexts(ast.parse("a, b = c, d")))