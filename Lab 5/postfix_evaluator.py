def centralfunc(self, ab):
    for i in ab:

        try:
            self.push(int(i))

        except ValueError:
            val1 = self.pop()
            val2 = self.pop()

            switcher = {'+': val2 + val1, '-': val2 - val1, '*': val2 * val1, '/': val2 / val1, '^': val2 ** val1}
            self.push(switcher.get(i))
    return int(self.pop())


str = '20 3 1 * + 90 -'

# splitting the given string to obtain  
# integers and operators into a list 
strconv = str.split(' ')
obj = evalpostfix()
print(obj.centralfunc(strconv))
print(evalpostfix().centralfunc())
print(centralfunc('20 3 1 * + 90 -'))
