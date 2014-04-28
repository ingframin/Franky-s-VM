class Machine:

    def __init__(self, mem_size, rp_size, iom_size, s_status = {}):
        self.memory = [0 for x in range(mem_size)]
        self.R = [0 for x in range(rp_size)]
        self.PC = 0
        self.IR = 0
        self.SP = mem_size-1
        self.SS = 0
        self.flags= {'zero':0, 'eq':0, 'div0':0, 'suf':0}
        self.prg_mem = []
        self.IO_mem = [0 for x in range(iom_size)]
        self.status = s_status
        self.ret_mem = {}
        
        if s_status == {}:
            
            self.status['R'] = []
            self.status['PC'] = []
            self.status['flags'] = []
            self.status['SP'] = []
            self.status['SS'] = []
        
        
    def fetch(self):
        self.IR = prg_mem[self.PC]
        self.PC += 1

    def halt(self):
        self.PC = -1

    def move(self,s,d):
        self.R[d] = self.R[s]

    def load(self,addr,reg):
        self.R[reg] = self.memory[addr]

    def store(self,reg,addr):
        self.memory[addr] = self.R[reg]

    def mmove(self,addr_s,addr_d):
        self.memory[addr_d] = self.memory[addr_s]

    def push(self,reg):
        self.memory[self.SP] = self.R[reg]
        self.SP -= 1
        self.SS += 1
        
    def pop(self,reg):
        if self.SS == 0:
            self.flags['suf'] = 1
            return
        else:
            self.flags['suf'] = 0
        
        self.SP += 1
        self.R[reg] = self.memory[self.SP]
        self.SS -= 1
        
    def io_read(self,addr):
        self.IO_mem[addr] = input()

    def io_write(self,addr):
        print(self.IO_mem[addr])

    def add(self,r1,r2,rd):
        self.R[rd] = self.R[r1]+self.R[r2]
        if self.R[rd] ==0:
            self.flags['zero'] = 1
        else:
            self.flags['zero'] = 0

    def sub(self,r1,r2,rd):
        self.R[rd] = self.R[r1]-self.R[r2]
        if self.R[rd] ==0:
            self.flags['zero'] = 1
        else:
            self.flags['zero'] = 0
            
    def mul(self,r1,r2,rd):
        self.R[rd] = self.R[r1]*self.R[r2]
        if self.R[rd] ==0:
            self.flags['zero'] = 1
        else:
            self.flags['zero'] = 0

    def div(self,r1,r2,rd):
        if self.R[r2] == 0:
            self.flags['div0'] = 1
        else:
            self.flags['div0'] = 0

        self.R[rd] = self.R[r1]/self.R[r2]
        
        if self.R[rd] ==0:
            self.flags['zero'] = 1
        else:
            self.flags['zero'] = 0
            
    def rem(self,r1,r2,rd):
        if self.R[r2] == 0:
            self.flags['div0'] = 1
        else:
            self.flags['div0'] = 0
            
        self.R[rd] = self.R[r1]%self.R[r2]

        if self.R[rd] ==0:
            self.flags['zero'] = 1
        else:
            self.flags['zero'] = 0
            
    def pow(self,r1,r2,rd):
        self.R[rd] = self.R[r1]**self.R[r2]
        if self.R[rd] ==0:
            self.flags['zero'] = 1
        else:
            self.flags['zero'] = 0
            
    def shl(self,reg,n):
        self.R[reg] <<= n

    def shr(self,reg,n):
        self.R[reg] >>= n
        
    def cmp(self,r1,r2):
        if self.R[r1] == self.R[r2]:
            self.flags['eq'] = 1
        else:
            self.flags['eq'] = 0
            
    def jmp(self,addr):
        self.PC = addr

    def je(self,r1,r2,addr):
        if self.R[r1] == self.R[r2]:
            self.PC = addr
            self.flags['eq'] = 1
        else:
            self.flags['eq'] = 0

    def jne(self,r1,r2,addr):
        if self.R[r1] != self.R[r2]:
            self.PC = addr
            self.flags['eq'] = 0
        else:
            self.flags['eq'] = 1

    def jg(self,r1,r2,addr):
        if self.R[r1] > self.R[r2]:
            self.PC = addr
            
    def jge(self,r1,r2,addr):
        if self.R[r1] >= self.R[r2]:
            self.PC = addr
            
    def jl(self,r1,r2,addr):
        if self.R[r1] < self.R[r2]:
            self.PC = addr
            
    def jle(self,r1,r2,addr):
        if self.R[r1] <= self.R[r2]:
            self.PC = addr
            
    def jz(self,addr):
        if self.flags['zero'] == 1:
            self.PC = addr
            
    def jnz(self,addr):
        if self.flags['zero'] == 0:
            self.PC = addr

    def dup(self):
        self.memory[self.SP] = self.memory[self.SP-1]
        self.SP -= 1
        self.SS += 1

    def swap(self):
        if self.SS<2:
            return
        self.memory[self.SP-1],self.memory[self.SP-2] = self.memory[self.SP-2],self.memory[self.SP-1]

    def call(self,p_addr,p_len,addr):
        self.status['R'].append(self.R)
        self.status['PC'].append(self.PC)
        self.status['flags'].append(self.flags)
        self.status['SP'].append(self.SP)
        self.status['SS'].append(self.SS)
        self.PC = addr
        self.SS = 0

    def ret(self, r_addr, r_len):
        self.R = self.status['R'].pop()
        self.PC = self.status['PC'].pop(self.PC)
        self.flags = self.status['flags'].pop(self.flags)
        self.SP = self.status['SP'].pop(self.SP)
        self.SS = self.status['SS'].pop(self.SS)
        self.PC += 1
    
        
