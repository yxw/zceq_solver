#!/usr/bin/env python3

from ctypes import *
from binascii import hexlify
from bench.solver import Solver 
from bench.test_cases import dataList, soluList 
import os
import time
from datetime import datetime
import gc

gc.enable()

# gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK)

def test_solver(solver):
    right = 0
    wrong = 0
    time_list = []
    for i in range(len(dataList)):
        data = bytes.fromhex(dataList[i])
        solu = bytes.fromhex(soluList[i])

        start = datetime.now()
        ret = solver.validate_solution(data, solu)
        # in miliseconds
        t = (datetime.now() - start).total_seconds() * 1000
        time_list.append(t)

        if ret:
            right += 1
        else:
            wrong += 1
   
    return (right, wrong, time_list) 

def bench_solvers():
    #from pyzceqsolver_leak.solver import Solver as LeakSolver
    #from pyzceqsolver_prod1.solver import Solver as Prod1Solver
    #from pyzceqsolver_prod2.solver import Solver as Prod2Solver
    solver_names = ["latest", "leak", "prod1", "prod2"]
    solver_filenames = ["libzceq_solver_sh.so", "libzceq_solver_sh_leak.so", "libzceq_solver_sh_prod1.so","libzceq_solver_sh_prod2.so"]
    #solvers = [LatestSolver(), LeakSolver(), Prod1Solver(), Prod2Solver()]
    solvers = map(Solver, solver_filenames)
    solver_results = map(test_solver, solvers)

    print("SolverName  right/wrong  avg_time")
    for i, sresult in enumerate(solver_results):
        sname = solver_names[i]
        print("%10s  %5d/%-5d  %.4f (ms)" % (sname, sresult[0], sresult[1], sum(sresult[2])/len(sresult[2]))) 


if __name__ == "__main__":
    bench_solvers()


