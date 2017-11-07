
        
            
memory = [0 for x in range(2**16)]
reg_pool = {'R0':0,'R1':0,'R2':0,'R3':0,'R4':0,'R5':0,'R6':0,'R7':0,\
            'R8':0,'R9':0,'R10':0,'R11':0,'R12':0,'R13':0,'R15':0}
srv_reg = {'PC':0,'IR':'halt','SP':2**16 -1}
prg_mem = []


def fetch():
    srv_reg['IR'] = prg_mem[srv_reg['PC']]
    srv_reg['PC'] += 1

def move(s,d):
    reg_pool[d]=reg_pool[s]

def add(a1,a2,d):
    reg_pool[d]=reg_pool[a1]+reg_pool[a2]

def halt():
    srv_reg['PC'] = -1

def load(ms,d):
    reg_pool[d] = memory[int(ms)]

def store(s,md):
    memory[int(md)] = reg_pool[s]

def stv(v,md):
    memory[int(md)] = int(v)

def sub(s1,s2,d):
    reg_pool[d] = reg_pool[s1]-reg_pool[s2]

def mul(m1,m2,d):
    reg_pool[d] = reg_pool[m1]*reg_pool[m2]

def div(d1,d2,d):
    reg_pool[d] = reg_pool[d1]/reg_pool[d2]

def bxor(x1,x2,d):
    reg_pool[d] = reg_pool[x1]^reg_pool[x2]

def band(a1,a2,d):
    reg_pool[d] = reg_pool[a1]&reg_pool[a2]

def bor(o1,o2,d):
    reg_pool[d] = reg_pool[o1]|reg_pool[o2]

def bnot(n1,d):
    reg_pool[d]=~reg_pool[n1]

def jmp(tag):
    srv_reg['PC']=int(tag)

def nop():
    pass

def je(j1,j2,d):
    if reg_pool[j1]==reg_pool[j2]:
        srv_reg['PC'] = reg_pool[d]

def jne(j1,j2,d):
    if reg_pool[j1]!=reg_pool[j2]:
        srv_reg['PC'] = reg_pool[d]

def jge(j1,j2,d):
    if reg_pool[j1]>=reg_pool[j2]:
        srv_reg['PC'] = reg_pool[d]
def jle(j1,j2,d):
    if reg_pool[j1]<=reg_pool[j2]:
        srv_reg['PC'] = reg_pool[d]

def jg(j1,j2,d):
    if reg_pool[j1]>reg_pool[j2]:
        srv_reg['PC'] = reg_pool[d]

def jl(j1,j2,d):
    if reg_pool[j1]<reg_pool[j2]:
        srv_reg['PC'] = reg_pool[d]

def reset():
    srv_reg['PC'] = 0

def push(reg):
    memory[srv_reg['SP']] = reg_pool[reg]
    srv_reg['SP'] -= 1

def pop(reg):
    srv_reg['SP'] += 1
    reg_pool[reg] = memory[srv_reg['SP']]
    

def sl(v,reg):
    reg_pool[reg] = reg_pool[reg]<<v

def sr(v,reg):
    reg_pool[reg] = reg_pool[reg]>>v
    
def call(tag):
    
    for r in sorted(reg_pool):
        push(r)
    
    reg_pool['R1'] = srv_reg['PC']
    push('R1')
    
    srv_reg['PC'] = int(tag)
    

def ret():
    pop('R0')
    srv_reg['PC'] = reg_pool['R0']+1
    
    for r in sorted(reg_pool,reverse = True):
        pop(r)
      
def mmove(src,dst):
    memory[dst] = memory[src]

        
isa = {}

isa['fetch'] = fetch    
isa['move'] = move
isa['add'] = add
isa['halt'] = halt
isa['load'] = load
isa['store'] = store
isa['stv'] = stv
isa['sub'] = sub
isa['mul'] = mul
isa['div'] = div
isa['xor'] = bxor
isa['and'] = band
isa['or'] = bor
isa['not'] = bnot
isa['jmp'] = jmp
isa['nop'] = nop
isa['je'] = je
isa['jne'] = jne
isa['jge'] = jge
isa['jle'] = jle
isa['jg'] = jg
isa['jl'] = jl
isa['reset'] = reset
isa['push'] = push
isa['pop'] = pop
isa['sr'] = sr
isa['sl'] = sl
isa['call'] = call
isa['ret'] = ret
isa['mmove'] = mmove
