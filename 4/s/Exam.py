############################################################
# Exam.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################


############################################################
#  NOTHING CAN BE CHANGED BELOW
###########################################################
class Solution:
    def isEscapePossible(self, b: 'List of list of size 2', s:'list of size 2', t:'list of size 2') -> bool:
        show = False
        R = 1000000
        C = 1000000
        dir = [[-1,0],[1,0],[0,-1],[0,1]] #directional moves
        work = [0]
        ans = [] #all directions you explored
        is_escape_possible = [False] #True/False
        s = Exam(R,C,b,s,t,dir,is_escape_possible,ans,work,show)
        return is_escape_possible[0]


########################################
#Nothing can be changed in class Exam
########################################
class Exam:
    def __init__(self, 
          r:'int', #Max rows
          c:'int', #Max columns
          blocked: 'List of list of size 2', #[[0,1],[1,0]]
          source: 'list of size 2', #[0,0]
          target: 'list of size 2', #[0,2]
          dir:'list of list', #[[0,1],[1,0]] #Direction you can move from current position
          is_escape_possible:'List of size 1', #True/False
          ans:'list of list', #You fill all directions that you explored
          work:'List of size 1',#You fill number of steps
          show:'Bool',#if show is True, show each step of the algorithm
        )->'None':

        self._r = r
        self._c = c
        self. _blocked = blocked
        self._dir = dir
        self._is_escape_possible = is_escape_possible
        self._ans = ans
        self._work = work
        self._show = show

        #YOU CAN HAVE your data structure. All must be private
        self._s = tuple(source)
        self._t = tuple(target)
        self._block_set = set()
        self._visisted_set = set()
        
        # MUST WRITE THIS ROUTINE
        self._alg() #this will fill self._is_escape_possible[0] True or False
        

    ############################################################
    # TIME: 
    # SPACE:
    ############################################################
    def _alg(self)->'None':
        if (len(self._blocked) == 0):
            self._is_escape_possible[0] = True
        self._dfs()
        
    ############################################################
    # DFS
    ############################################################
    
    def _dfs(self) -> 'None':
        for e in self._blocked:
            self._block_set.add(tuple(e))
        start_in_blocked_set = (self._s) in self._block_set
        target_in_blocked_set = (self._t) in self._block_set
        if (start_in_blocked_set or target_in_blocked_set):
            return False
        
        s = self._s 
        self._dfs_r(s) #starting point
        
        
    def _dfs_r(self, s:'(x,y)') -> 'None':
        if (self._is_escape_possible[0] == False):
            if (self._show):
                print(s, end = '')
                
            if (self._reached_dest(s)):
                self._is_escape_possible[0] = True 
    
            for d in self._dir:
                if (is_escape_possible[0] == False):
                    n = self._next_move(s, d)
                    self._visisted_set.add(s)
                    if (self._is_valid_move(n)):
                        self._ans.append(d)
                        self._dfs_r(n) # recursion on new n 
                           
                           
    def _is_valid_move(self, new_move:'tuple of size 2') -> "bool":
        self._increment_work()
        if new_move[0] >= 0 and new_move[0] < self._r:
            if new_move[1] >= 0 and new_move[1] < self._c:
                in_blocked_set = new_move in self._block_set
                in_visited_set = new_move in self._visisted_set
                if (not(in_blocked_set) and not(in_visited_set)): # Theta(1)
                    return True
        return False
    
    
    def _next_move(self, currentPos:'(cx, cy)', direction:'[x,y]') -> '(nx, ny)':
        self._increment_work()
        assert(len(m) == 2)
        return ((currentPos[0] + direction[0]),(currentPos[1] + direction[1]) )
    
    
    def _reached_dest(self, currentPos:'tuple of size 2') -> 'bool':
        if ((currentPos[0] == self._t[0]) and (currentPos[1] == self._t[1])):
            return True
        return False
        
    ############################################################
    # TIME: THETA(1)
    # SPACE: THETA(1)
    ############################################################
    def _increment_work(self)->'None':
        self._work[0] += 1

    ############################################################
    # TIME: THETA(1)
    # SPACE: THETA(1)
    ############################################################
    def _append_ans(self,n:'list of [x,y]'):
        self._ans.append(n)

          
############################################################
#  NOTHING CAN BE CHANGED BELOW. THIS MUST BE LAST
#
'''
    2
    4
    1 1 1 1
    1 1 1 1
    1 1 1 1
    1 1 1 1
    3
    1 0 0
    0 0 0
    0 0 1

    output
    POSSIBLE
    NOT POSSIBLE
'''
###########################################################
if (True): 
  n = int(input().strip()) #Number of testcase
  for i in range(n):
    b = [] #
    s = [0,0]        
    d = [[0,1],[1,0]] #Direction you can move from current position 
    N =  int(input().strip()) # size of matrix
    t = [N-1,N-1] # fixed position
    for j in range(N):
      row = list(map(int, input().strip().split()))
      for k in range(N):
        if (row[k] == 0):
          #0 is blocked position
          b.append([j,k])
    work = [0]
    ans = [] #all directions you explored
    is_escape_possible = [False] #True/False
    s = Exam(N,N,b,s,t,d,is_escape_possible,ans,work,False)
    if (is_escape_possible[0]):
        print("POSSIBLE")
    else:
        print("NOT POSSIBLE")


