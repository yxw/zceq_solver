from __future__ import print_function
from pyzceqsolver.solver import Solver
import string
import sys

s = Solver()

org_solution = [123] * 512
min = s.list_to_minimal(org_solution)
back = s.minimal_to_list(min)
assert back == org_solution

for character in string.printable:
    block_header = character * 140
    if sys.version_info >= (3, 0):
        block_header = bytes(block_header, 'ascii')

    n = s.find_solutions(block_header)
    print(n, 'solution(s) found for "%s"' % character)

    for e in range(n):
        solution = s.get_solution(e)
        assert len(solution) == 1344

        # Try to validate a given solution
        # -1 = internal error, 0 = invalid solution, 1 = valid solution

        result = s.validate_solution(block_header, solution)
        if result != 1:
            print("Error: invalid solution (%d)" % result)

        result = s.validate_solution(block_header, solution[::-1])
        if result != 0:
            print("Error: solution should be rejected (%d)" % result)
