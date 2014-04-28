class Stack:
    
    def __init__(self,max_size):
        self.max_size = max_size #stack max size
        self.content = []
        self.SP = -1 #stack pointer
        self.SS = 0 #stack size
        #flags
        self.ovf = 0 #stack overflow
        self.unf = 0 #stack underflow
        
    def push(self,data):
        if self.SS == self.max_size:
            self.ovf = 1
            return

        self.content.append(data)
        self.SP += 1
        self.SS = len(self.content)

    def pop(self):
        if self.SS == 0:
            self.unf = 1
            return
        self.SP -= 1
        self.SS -= 1
        return self.content.pop()

    def dup(self):
        if self.SS == self.max_size:
            self.ovf = 1
            return
        
        if self.SS <1:
            self.unf = 1
            return
        self.content.append(self.content[-1])
        self.SP += 1
        self.SS += 1

    def swap(self):
        if self.SS < 2:
            self.unf = 1
            return

        self.content[-1],self.content[-2] = self.content[-2],self.content[-1]
        
        
