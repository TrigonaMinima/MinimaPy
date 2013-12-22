# Depth Frist Search algorithm

def func(node):
    return node.getValue() == 6

def DFS(root, func):
    stack = [root]
    while len(stack)>0:
        if func(stack[0]):
            return True
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False
