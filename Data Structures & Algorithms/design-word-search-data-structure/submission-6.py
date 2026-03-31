class TrieNode:
    def __init__(self): 
        self.children = {}
        self.is_word = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True
        
    def search(self, word: str) -> bool:
        # 創建一個 dfs func 參數為 idx 和 root
        # return dfs(i, root)
        # 需要一個 cur 指針，一開始指向 root
        # 需要另一個 idx j traverse word to len(word)
        # c = word[j]
        # 如果 c != '.' 不在 cur.children 內 return False 或是指針繼續往下
        # 如果是 '.' 所有 cur.children.values() 都要找，def(j+1, child)
        # 內部如果 return True 就是 True 否則就是 False

        def dfs(i, root):
            cur = root
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.is_word
        return dfs(0, self.root)