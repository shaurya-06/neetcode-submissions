class Solution:
    def isValid(self, s: str) -> bool:

        if s == "":
            return False
        
        stack = []

        for char in s:
            last_char = len(stack) - 1
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" and stack and stack[last_char] == "(":
                stack.pop(last_char)
            elif char == "}" and stack and stack[last_char] == "{":
                stack.pop(last_char)
            elif char == "]" and stack and stack[last_char] == "[":
                stack.pop(last_char)
            else:
                return False

        if stack != []:
            return False

        return True
