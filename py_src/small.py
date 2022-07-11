memory = [0 for x in range(2**16)]
reg_pool = {'R0':0,'R1':0,'R2':0,'R3':0,'R4':0,'R5':0,'R6':0,'R7':0,\
            'R8':0,'R9':0,'R10':0,'R11':0,'R12':0,'R13':0,'R15':0}
alu_reg = {'ACC':0,'AND':0,'OR':0,'XOR':0,'NOT1':0,'NOT2':0}
srv_reg = {'PC':0,'IR':'','SP':2**16 -1}
flags={'zero':False,'overflow':False,'larger':False,'smaller':False,'equal':False,'different':False}

def load(address,reg):
    reg_pool[reg] = memory[address]

def store(reg, address):
    memory[address] = reg_pool[reg]

def push(reg):
    memory[srv_reg['SP']] = reg_pool[reg]
    srv_reg['SP'] -= 1

def pop(reg):
    reg_pool[reg] = memory[srv_reg['SP']]
    srv_reg['SP'] += 1

def jmp(address,cond='-'):
    f1 = 'e' in cond and flags['equal']
    f2 = 'd' in cond and flags['different']
    f3 = 'l' in cond and flags['larger']
    f4 = 's' in cond and flags['smaller']
    f5 = '-' in cond
    if f1 or f2 or f3 or f4 or f5:
        srv_reg['PC'] = address
    
def add(reg1,reg2):
    alu_reg['ACC']=reg_pool[reg1]+reg_pool[reg2]
    flags['zero'] = srv_reg['ACC'] == 0

def sub(reg1,reg2):
    srv_reg['ACC']=reg_pool[reg1]-reg_pool[reg2]
    flags['zero'] = srv_reg['ACC'] == 0

def cmp(reg1,reg2):
    flags['larger'] = reg_pool[reg1] > reg_pool[reg2]
    flags['smaller'] = reg_pool[reg1] < reg_pool[reg2]
    flags['equal'] = reg_pool[reg1] == reg_pool[reg2]
    flags['different'] = reg_pool[reg1] != reg_pool[reg2]
    
def logic(reg1,reg2):
    alu_reg['AND'] = reg_pool[reg1] & reg_pool[reg2]
    alu_reg['OR'] = reg_pool[reg1] | reg_pool[reg2]
    alu_reg['XOR'] = reg_pool[reg1] ^ reg_pool[reg2]
    alu_reg['NOT1'],alu_reg['NOT2'] = ~reg_pool[reg1],~reg_pool[reg2]

#isa dictionary
isa = {'load':load,'store':store,'push':push,'pop':pop,'jmp':jmp, 'add':add,'sub':sub,'cmp':cmp,'logic':logic}