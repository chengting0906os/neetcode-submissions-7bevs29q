class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        int_stack = []
        cur = ""
        k = 0

        # 遇到 k 加上 
        # 遇到 [  k 歸零
        # 遇到 ] 開始 pop()

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == "[":
                str_stack.append(cur)
                int_stack.append(k)
                cur = ""
                k = 0
            elif char == "]":
                inner_str = cur
                prefix = str_stack.pop()
                count = int_stack.pop()
                prefix += inner_str * count
                cur = prefix
            else:
                cur += char
        
        return cur

        