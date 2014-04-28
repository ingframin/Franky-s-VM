from isa import *
import cProfile

def load_prg(filename):
    f = open(filename)
    rd = f.read()
    f.close()
    rds = rd.split('\n')
    for i in rds:
        if i == '' or i[0] == ':':
            prg_mem.append('nop')
            continue
        prg_mem.append(i)
        
def execute(instr):
    ins = instr.split()
    
    opcode = ins[0]
    params = []
    if len(ins)>1:
        params = ins[1].split(',')

    if len(params) == 1:
        isa[opcode](params[0])
    elif len(params) == 2:
        isa[opcode](params[0],params[1])
    elif len(params) == 3:
        isa[opcode](params[0],params[1],params[2])
    else:
        isa[opcode]()
    
def debug():
    
    print('F01 Virtual Machine, debug mode')
    
    while True:
        a = input('=>')
        if a == 'status':
            for i in range(len(memory)):
                if memory[i] != 0:
                    print('addr = %d,value = %d'%(i,memory[i]))
            
            print(reg_pool)
            print(srv_reg)
            continue
        if a == 'exit':
            break
        
        try:
            execute(a)
        except:
            print('wrong instruction')

        if srv_reg['PC'] == -1:
            break

def main(filename):
    print('F01 Virtual Machine')
    load_prg(filename)
    f = open('log.txt','w')
    while True:
       
        fetch()
        
        f.write(str(srv_reg))
        f.write('\n')
        try:
            execute(srv_reg['IR'])
        except:
            print('wrong instruction')
            debug()
      
        f.write(str(reg_pool))
        f.write('\n')
        
        if srv_reg['PC'] == -1:
            break
    f.close()
    print('END')
    
main('prg.asm')    
#debug()
#cProfile.run('main("prg.asm")')
