class Memory:

    def __init__(self, size):
        self.content = [0 for x in range(size)]
        #flags
        self.ovf = 0
        self.unf = 0

    def store(self,address,data):
        if address > len(self.content):
            self.ovf = 1
            return

        if address < 0:
            self.unf = 1
            return

        self.content[address] = data

    def load(self,address):
        if address > len(self.content):
            self.ovf = 1
            return

        if address < 0:
            self.unf = 1
            return
        
        return self.content[address]

    def free(self,s_addr,e_addr):
        if s_addr > e_addr:
            return

        if s_addr<0 or e_addr<0:
            self.unf = 1
            return
        if e_addr > len(self.content) or s_addr > len(self.content):
            self.ovf = 1
            return

        for i in range(s_addr,e_addr,1):
            self.content[i] = 0

    def mmove(self,s_addr,d_addr):
        if s_addr<0 or d_addr <0:
            self.unf = 1
            return
        if s_addr > len(self.content) or d_addr>len(self.content):
            self.ovf = 1
            return

    def memcpy(self,s_addr,d_addr,n):
        if d_addr+n > len(self.content):
            self.ovf = 1
            return

        self.content[d_addr:d_addr+n] = self.content[s_addr:s_addr+n]

    def msort(self,addr,n):
        if addr < 0:
            self.unf = 1
            return
        if addr>len(self.content):
            self.ovf = 1
            return
        self.content[addr:addr+n] = sorted(self.content[addr:addr+n])
        
