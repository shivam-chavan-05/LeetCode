#Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #gregHogg
        stk = []
        for i in tokens:
            if i in '+-*/':
                pop2, pop1 = stk.pop(), stk.pop()
                if i == '+':
                    stk.append( pop1 + pop2 )
                elif i == '-':
                    stk.append( pop1 - pop2 )
                elif i == '*':
                    stk.append( pop1 * pop2 )
                else:
                    stk.append( int(pop1 / pop2) )
            else:
                stk.append(int(i))

        return stk[0]
