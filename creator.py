import os

problem_name: str = str(input("problem: "))
os.mkdir(problem_name)

os.chdir(problem_name)
open("main.py", "w").write("from solve import Solution\ndef main():\n\tprint(Solution().m_solution())\nif __name__ == \"__main__\":\n\tmain()\n")
open("solve.py", "w").write("class Solution:\n\tdef m_solution(self):\n\t\tpass")
