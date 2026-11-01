def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    stack = []

    brackets = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in brackets.values():
            stack.append(char)

        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False

    return len(stack) == 0