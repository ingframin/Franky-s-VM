#Machine components
memory = None
R = None
PC = None
IR = None
SP = None
SS = None
flags= None
prg_mem = None
IO_mem = None
status = None
opcodes = {}

def load_isa(filename):
	pass
	
def init(mem_size, rp_size, iom_size):
	'''init function
	initialize all the components of the virtual machine'''
	
    memory = [0 for x in range(mem_size)]
    R = [0 for x in range(rp_size)]
    PC = 0
    IR = 0
    SP = mem_size-1
    SS = 0
    flags= {'zero':0, 'eq':0, 'div0':0, 'suf':0}
    prg_mem = []
    IO_mem = [0 for x in range(iom_size)]
    status = {}
    status['R'] = []
    status['PC'] = []
    status['flags'] = []
    status['SP'] = []
    status['SS'] = []


def nop():
	pass

def halt():
	PC = -1

def fetch():
	IR = prg_mem[PC]
	PC += 1

def move(s,d):
	R[d] = R[s]

def load(addr,reg):
	R[reg] = memory[addr]

def store(reg,addr):
	memory[addr] = R[reg]

def mmove(addr_s,addr_d):
	memory[addr_d] = memory[addr_s]

def push(reg):
	memory[SP] = R[reg]
	SP -= 1
	SS += 1

def pop(reg):
	if SS == 0:
		flags['suf'] = 1
		return
	else:
		flags['suf'] = 0
	
	SP += 1
	R[reg] = memory[SP]
	SS -= 1

def io_read(addr):
	IO_mem[addr] = input()

def io_write(addr):
	print(IO_mem[addr])

def add(r1,r2,rd):
	R[rd] = R[r1]+R[r2]
	if R[rd] ==0:
		flags['zero'] = 1
	else:
		flags['zero'] = 0

def sub(r1,r2,rd):
	R[rd] = R[r1]-R[r2]
	if R[rd] ==0:
		flags['zero'] = 1
	else:
		flags['zero'] = 0
		
def mul(r1,r2,rd):
	R[rd] = R[r1]*R[r2]
	if R[rd] ==0:
		flags['zero'] = 1
	else:
		flags['zero'] = 0

def div(r1,r2,rd):
	if R[r2] == 0:
		flags['div0'] = 1
	else:
		flags['div0'] = 0

	R[rd] = R[r1]/R[r2]
	
	if R[rd] ==0:
		flags['zero'] = 1
	else:
		flags['zero'] = 0
		
def rem(r1,r2,rd):
	if R[r2] == 0:
		flags['div0'] = 1
	else:
		flags['div0'] = 0
		
	R[rd] = R[r1]%R[r2]

	if R[rd] ==0:
		flags['zero'] = 1
	else:
		flags['zero'] = 0
	
def pow(r1,r2,rd):
	R[rd] = R[r1]**R[r2]
	if R[rd] ==0:
		flags['zero'] = 1
	else:
		flags['zero'] = 0
		
def shl(reg,n):
	R[reg] <<= n

def shr(reg,n):
	R[reg] >>= n
	
def cmp(r1,r2):
	if R[r1] == R[r2]:
		flags['eq'] = 1
	else:
		flags['eq'] = 0
		
def jmp(addr):
	PC = addr

def je(r1,r2,addr):
	if R[r1] == R[r2]:
		PC = addr
		flags['eq'] = 1
	else:
		flags['eq'] = 0

def jne(r1,r2,addr):
	if R[r1] != R[r2]:
		PC = addr
		flags['eq'] = 0
	else:
		flags['eq'] = 1

def jg(r1,r2,addr):
	if R[r1] > R[r2]:
		PC = addr
	
def jge(r1,r2,addr):
	if R[r1] >= R[r2]:
		PC = addr
		
def jl(r1,r2,addr):
	if R[r1] < R[r2]:
		PC = addr
	
def jle(r1,r2,addr):
	if R[r1] <= R[r2]:
		PC = addr
		
def jz(addr):
	if flags['zero'] == 1:
		PC = addr
		
def jnz(addr):
	if flags['zero'] == 0:
		PC = addr

def dup():
	memory[SP] = memory[SP-1]
	SP -= 1
	SS += 1

def swap():
	if SS<2:
		return
	memory[SP-1],memory[SP-2] = memory[SP-2],memory[SP-1]

def call(p_addr,p_len,addr):
	status['R'].append(R)
	status['PC'].append(PC)
	status['flags'].append(flags)
	status['SP'].append(SP)
	status['SS'].append(SS)
	PC = addr
	SS = 0
	
def ret(r_addr, r_len):
	R = status['R'].pop()
	PC = status['PC'].pop(PC)
	flags = status['flags'].pop(flags)
	SP = status['SP'].pop(SP)
	SS = status['SS'].pop(SS)
	PC += 1
