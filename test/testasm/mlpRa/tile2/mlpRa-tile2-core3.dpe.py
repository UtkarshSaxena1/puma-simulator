
import sys, os
import numpy as np
import math
sys.path.insert (0, '/home/rodrigo/workspace/dpe-research/dpe_emulate/include/')
sys.path.insert (0, '/home/rodrigo/workspace/dpe-research/dpe_emulate/src/')
from data_convert import *
from instrn_proto import *
from tile_instrn_proto import *
dict_temp = {}
dict_list = []
i_temp = i_set(d1=257, imm=10, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=257, r1=257, load_width=10, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=267, imm=788, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=0, r1=267, load_width=16, vec=8)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=267, imm=926, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=128, r1=267, load_width=16, vec=8)
dict_list.append(i_temp.copy())
i_temp = i_mvm(0b11)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=257, r1=257, r2=0, vec=10)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=257, r1=257, r2=128, vec=10)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=267, imm=1054, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=267, r1=267, load_width=10, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=257, r1=257, r2=267, vec=10)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=257, r1=257, vec=10)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=267, imm=1064, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=267, r1=257, counter=1, store_width=10, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_hlt()
dict_list.append(i_temp.copy())
filename = 'mlpRa/tile2/core_imem3.npy'
np.save(filename, dict_list)