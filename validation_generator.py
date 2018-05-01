import os
from random import choice
from stat import S_IREAD, S_IRGRP, S_IROTH
from configs import *

alfanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

with open(alunosFile, 'r') as fi:
    with open(validacoesFile, 'w') as fo:
        for line in fi:
            l = line.strip()
            l = line.split(', ')[0]
            v = ''
            for i in range(8):
                v += f'{choice(alfanum)}'
            validacao = f'{prefix}-{v}'
            fo.write(f'{l}, {validacao}\n')

os.chmod(validacoesFile, S_IREAD|S_IRGRP|S_IROTH)