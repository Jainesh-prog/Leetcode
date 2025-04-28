class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []  # \U0001f4e6 Use a stack to build the result

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # \U0001f9f9 Remove last char if it's the same
            else:
                stack.append(char)  # ✅ Otherwise add current char

        return ''.join(stack)  # \U0001f9f5 Build final string from stack
