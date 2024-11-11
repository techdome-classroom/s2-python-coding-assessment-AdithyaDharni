class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # This is a closing bracket
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    print(f"Mismatch found: expected {mapping[char]}, but got {top_element} for {char}")
                    return False
            else:
                # This is an opening bracket
                stack.append(char)
                print(f"Stack after adding {char}: {stack}")

        # Check if there are any unmatched opening brackets left
        if stack:
            print(f"Unmatched opening brackets remain in stack: {stack}")
            return False
        
        return True

