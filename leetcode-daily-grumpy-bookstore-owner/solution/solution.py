from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Calculate the number of satisfied customers without using the secret technique
        satisfied_customers = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied_customers += customers[i]
        
        # Calculate the number of customers that can be potentially satisfied by using the technique
        additional_satisfied_customers = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_satisfied_customers += customers[i]
        
        # This is the maximum additional satisfied customers in the initial window
        max_additional_satisfied_customers = additional_satisfied_customers
        
        # Use a sliding window to calculate the maximum number of additional satisfied customers
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfied_customers += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied_customers -= customers[i - minutes]
            max_additional_satisfied_customers = max(max_additional_satisfied_customers, additional_satisfied_customers)
        
        return satisfied_customers + max_additional_satisfied_customers

# Example usage:
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3

solution = Solution()
print(solution.maxSatisfied(customers, grumpy, minutes))  # Output: 16
