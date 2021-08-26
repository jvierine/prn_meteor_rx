import numpy as n

def bpsk(seed,length):
    # set random seed to generate exactly the same code
    # let's hope python never changes their random number
    # generator!
    n.random.seed(seed)
    code=n.random.random(length)
    code=n.exp(2.0*n.pi*1.0j*code)
    code=n.angle(code)
    code=-1.0*n.sign(code)
    code=code.real
    code=n.array(code,dtype=n.complex64)
    return(code)
