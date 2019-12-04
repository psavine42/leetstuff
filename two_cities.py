from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/two-city-scheduling/

        initially, take count the number of binary assignments {A,B}
        which are optimally 1 and 1, also keep the cost to swap each assignment
        from A to B and from B to A

        then, calculate the number of swaps to meet the requirments.
        then just take that number of elements from the swap correct list and add to

        Complexity - the sort bit of the lists is NlogN, the other steps are linear.
        Space - N to keep the list of swap costs.

        The two lists are better if the input is more evenly distributed

        """

        N = len(costs)
        swap_ab = []
        swap_ba = []
        numB, numA = 0, 0
        cost = 0
        for c1, c2 in costs:
            if c1 <= c2:
                numA += 1
                swap_ab.append(c2 - c1)
            else:
                swap_ba.append(c1 - c2)
                numB += 1
            cost += min(c1, c2)

        if numA > numB:
            change = swap_ab
            n = N // 2 - numB
        elif numA < numB:
            change = swap_ba
            n = N // 2 - numA
        else:
            return cost

        change.sort()

        cost += sum(change[0:n] )
        return cost

    def v2(self, costs):
        costs.sort()
