import sys
from os import listdir
from os.path import isdir, isfile, join

DEF_BIN="bimodal-no-no-no-lru-1core"
BENCHMARKS_DIR="cvp_traces"
JOB_HEADER='''#!/bin/bash
#SBATCH --job-name=serial_job_test # Job name
#SBATCH --mail-type=END,FAIL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=oatoor@tamu.edu # Replace with your email address
#SBATCH --ntasks=1 # Run on a single CPU
#SBATCH --time=12:00:00 # Time limit hrs:min:sec
#SBATCH --output=serial_test_%j.log # Standard output and error log
'''
LINES='''echo "./run_champsim.sh $bin 1 30 $bench"
./run_champsim.sh $bin 1 30 $bench'''

binary_name = DEF_BIN
start = 0
end = 0
try:
    binary_name, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
except:
    pass

if isdir(BENCHMARKS_DIR):
    benchmarks = [f for f in listdir(BENCHMARKS_DIR) if isfile(join(BENCHMARKS_DIR, f))]

    text = [JOB_HEADER]
    for i in range(start, end):
        line = LINES.replace('$bin', binary_name, 2)
        try:
            line = line.replace('$bench', benchmarks[i], 2)
        except:
            break
        text.append(line)

    print '\n'.join(text)
