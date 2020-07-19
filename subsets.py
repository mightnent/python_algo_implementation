"""
given a set of distinct integers, return all the possible subsets, i.e. powersets
cannot contain duplicate subsets
input: arr of int
output: 2d array, with each sub array being a subset
edge cases: large input sets?
assumption: no duplicate set allowed. i.e. [2,1] and [1,2] cannot be output
"""

class solutions():
    def powerset(self,arr):
        queue = [[]]
        for i in arr:
            size = len(queue)
            for j in queue:
                if size == 0:
                    break
                copy = j[:]
                copy.append(i)
                queue.append(copy)
                size -=1

        return queue
    
    def powerset_pythonic(self,arr):
        queue = [[]]
        for i in arr:
            queue += [j +[i] for j in queue]
        return queue

new_set = solutions()
arr = [1,2,3]
