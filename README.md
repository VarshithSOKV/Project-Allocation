# Project-Allocation

The primary objective is to optimize the allocation of participants to projects by considering their skill levels and the prerequisites of each project. This program employs the Ford-Fulkerson algorithm to achieve the highest possible number of bipartite matchings between participants and projects, all while adhering to well-defined constraints.


Key Components:


1) Graph Representation:
           The program represents the project allocation problem as a bipartite graph, where participants and projects are nodes, and edges connect participants to projects if they meet the skill requirements.


2) Ford-Fulkerson Algorithm:
           The core of the project is the implementation of the Ford-Fulkerson algorithm to find the maximum number of matchings between participants and projects. This algorithm iteratively augments the flow in the graph to maximize the number of assignments.


3) Skill Levels:
           Skill levels of participants and project requirements are considered as parameters. Skill levels are represented as integers, and participants are matched to projects based on whether they meet or exceed the skill requirements.


4) Constraints:
           The program enforces constraints such as ensuring that one participant can mentor at most one co-participant within the same project. It also ensures that all roles in a project are filled before considering it completed.

5) Output:
           The project outputs the number of projects that can be completed based on the matching results obtained from the Ford-Fulkerson algorithm.

