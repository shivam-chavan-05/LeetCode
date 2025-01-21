#Valid Parantheses
class Solution:
    def isValid(self, s: str) -> bool:
        #gregHogg
        hashmap = {')':'(', '}':'{', ']':'['}
        stk = []
        for i in s:
            if i not in hashmap:
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[i]:
                        return False

                
        return not stk
