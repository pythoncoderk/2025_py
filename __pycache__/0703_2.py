s = "(()())"

stack = []
for char in s:
    if char == "(":
        stack.append(char)
    elif char == ")":
        if not stack:
            print("No")
        stack.pop()
print("Yes" if not stack else "No")
