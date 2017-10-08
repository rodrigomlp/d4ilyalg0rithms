#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:15:13 2017

@author: admin
"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.longest = 0
        self.count = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.count += 1
                    current = 1
                    self.countIsland(i, j, current, grid)
        return self.longest
    def countIsland(self, k, z, current, grid):
        print(str(k) + "," + str(z) + "=" + str(current))
        grid[k][z] = -1
        if k > 0 and grid[k-1][z] == 1:
               return self.countIsland(k-1, z, current+1, grid)
        if k < (len(grid)-1) and grid[k+1][z] == 1:
               return self.countIsland(k+1, z, current+1, grid)
        if z > 0 and grid[k][z - 1] == 1:
               return self.countIsland(k, z-1, current+1, grid)
        if z < (len(grid[0])-1) and grid[k][z+1] == 1:
              return self.countIsland(k, z+1, current+1, grid)
        self.longest = max(self.longest, current)
        return current    
       
        
       
arr = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,1,1,0,1,0,0,0,0,0,0,0,0],
       [0,1,0,0,1,1,0,0,1,0,1,0,0],
       [0,1,0,0,1,1,0,0,1,1,1,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,0,0,0,0,0,0,1,1,0,0,0,0]]
obj = Solution()
obj.maxAreaOfIsland(arr)