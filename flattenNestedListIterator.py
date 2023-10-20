class NestedIterator:
    '''This is the question no. 341'''
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while(self.stack):
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1]+top.getList()[::-1]
        return False
    
nes = NestedIterator()
