
from ortools.linear_solver import pywraplp
import time

def main():
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return

    x1 = solver.NumVar(0, solver.Infinity(), 'x1')
    x2 = solver.NumVar(0, solver.Infinity(), 'x2')
    x3 = solver.NumVar(0, solver.Infinity(), 'x3')
    x4 = solver.NumVar(0, solver.Infinity(), 'x4')

    solver.Add(x1 - x2 - x3 - 2 * x4 >= 2)
    solver.Add(x1 + x2 + x4 <= 8)
    solver.Add(x1 + 2 * x2 - x3 == 4)

    solver.Maximize(x1 + x2 - 2 * x3 + 2 * x4)
    start = time.perf_counter_ns()
    status = solver.Solve()
    end = time.perf_counter_ns()

    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal solution:")
        print("Objective value:", round(solver.Objective().Value(),3))
        print("x1:", round(x1.solution_value(),3))
        print("x2:", round(x2.solution_value(),3))
        print("x3:", round(x3.solution_value(),3))
        print("x4:", round(x4.solution_value(),3))
        print("Time taken:", (end - start) * 10**-6, "milliseconds")


if __name__ == "__main__":
    main()

