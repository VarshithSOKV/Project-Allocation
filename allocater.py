import numpy as np
"""All the below code is ford fulkerson algorithm for maximum bipartite matching from geeks and geeks(with small modifications for this problem)"""


# Python program to find
# maximal Bipartite matching.

class GFG:
	def __init__(self,graph):
		
		# residual graph
		self.graph = graph
		self.ppl = len(graph)
		self.jobs = len(graph[0])

	# A DFS based recursive function
	# that returns true if a matching
	# for vertex u is possible
	def bpm(self, u, matchR, seen):

		# Try every job one by one
		for v in range(self.jobs):

			# If applicant u is interested
			# in job v and v is not seen
			if self.graph[u][v] and seen[v] == False:
				
				# Mark v as visited
				seen[v] = True

				'''If job 'v' is not assigned to
				an applicant OR previously assigned
				applicant for job v (which is matchR[v])
				has an alternate job available.
				Since v is marked as visited in the
				above line, matchR[v] in the following
				recursive call will not get job 'v' again'''
				if matchR[v] == -1 or self.bpm(matchR[v],matchR, seen):
					matchR[v] = u
					return True
		return False

	# Returns maximum number of matching
	def maxBPM(self):
		'''An array to keep track of the
		applicants assigned to jobs.
		The value of matchR[i] is the
		applicant number assigned to job i,
		the value -1 indicates nobody is assigned.'''
		matchR = [-1] * self.jobs
		
		# Count of jobs assigned to applicants
		result = 0
		for i in range(self.ppl):
			
			# Mark all jobs as not seen for next applicant.
			seen = [False] * self.jobs
			
			# Find if the applicant 'u' can get a job
			if self.bpm(i, matchR, seen):
				result += 1
		return result,matchR


"""bpGraph =[[0, 1, 1, 0, 0, 0],
		[1, 0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0, 0],
		[0, 0, 1, 1, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 1]]"""

"""From here I have done by myself"""

N = int(input())
Nlevels=[]                              #keeps levels of all participants
for i in range(N):
    x1 = np.array(input().split())[-5:]
    x = list(x1.astype(int))
    Nlevels.append(x)
#print(Nlevels)

M = int(input())
Mlevels = []                            #keeps levels of all projects
for i in range(M):
    x1 = np.array(input().split())[-5:]
    x = list(x1.astype(int))
    Mlevels.append(x)
#print(Mlevels)

jobs_levels = list(np.array(Mlevels).reshape(-1))       #no of jobs are 5*M
#print(jobs_levels)

participant_levels = []
for i in range(N):
    x = []
    for _ in range(M):
        x.append(Nlevels[i])
    x = list(np.array(x).reshape(-1))
    participant_levels.append(x)

#print(participant_levels)

bggraph = []
for i in range(N):
    x = np.array(participant_levels[i]) >= np.array(jobs_levels)
    y = np.zeros(len(x))
    for j in range(len(x)):
        if(x[j] == True and jobs_levels[j]!=0):
            y[j]=1
    bggraph.append(list(y.astype(int)))
#print(bggraph)
g = GFG(bggraph)

x,y = g.maxBPM()        #x is no of jobs occupied

#print(x)

no_of_projects = 0
for i in range(M):
    flag = True
    for j in range(5):
        if(y[5*i + j] == -1 and jobs_levels[5*i + j] !=0):      #if y = -1 and jobs_levels != 0 => not recruited in required job
            flag = False
    if(flag == True):
        no_of_projects += 1

print(no_of_projects)
