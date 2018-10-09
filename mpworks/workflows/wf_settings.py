__author__ = 'Anubhav Jain'
__copyright__ = 'Copyright 2013, The Materials Project'
__version__ = '0.1'
__maintainer__ = 'Anubhav Jain'
__email__ = 'ajain@lbl.gov'
__date__ = 'May 10, 2013'

# don't change nnodes unless other parts of code are also changed
# nodes configuration will be ignored on SLURM due to different naming convention (nnodes vs nodes)
QA_VASP = {'queue': 'debug', 'nnodes': 2, 'nodes': 2, 'walltime': '6:00:00'}
QA_VASP_SMALL = {'queue': 'debug', 'nnodes': 2, 'nodes': 2, 'walltime': '6:00:00'}  # small walltime jobs
QA_DB = {'queue': 'debug', 'nnodes': 1, 'nodes': 1, 'ntasks_per_node': 1, 'walltime': '2:00:00'} # run db and boltztrap in 1 core
# QA_DB = {'nnodes': None, 'nodes': None, 'ntasks_per_node': None, 'queue': 'serial', 'qos': 'QosPartitionSerial', 'walltime': '2:00:00'}
QA_CONTROL = {'queue': 'debug', 'nnodes': 1, 'nodes': 1, 'ntasks_per_node': 1, 'walltime': '00:30:00'}
# QA_CONTROL = {'nnodes': None, 'nodes': None, 'ntasks_per_node': None, 'queue': 'serial', 'qos': 'QosPartitionSerial', 'walltime': '00:30:00'}

MOVE_TO_GARDEN_DEV = False
MOVE_TO_GARDEN_PROD = False

GARDEN = '/project/projectdirs/matgen/garden'

RUN_LOCS = [GARDEN, GARDEN + '/dev',
            '/project/projectdirs/matgen/garden/control_blocks',
            '/project/projectdirs/matgen/scratch',
            '/global/scratch/sd/matcomp/', '/global/homes/m/matcomp',
            '/scratch/scratchdirs/matcomp/', '/scratch2/scratchdirs/matcomp/',
            '/global/scratch/sd/matcomp/aj_tests/',
            '/global/scratch/sd/matcomp/wc_tests/',
            '/global/scratch/sd/matcomp/aj_prod/',
            '/global/scratch2/sd/matcomp/mp_prod/',
            '/global/scratch2/sd/matcomp/mp_prod_hopper/']
