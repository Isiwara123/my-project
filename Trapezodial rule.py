# Python3 code to implement Trapezoidal rule 

# Defining values used for input
y = [3.1, 4.4, 6.4, 6.6, 5.9, 5.6, 5.1, 4.9, 4.6]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Number of sub intervals
n = 8

# Define range of definite integral 
x0 = x[0]
xn = x[n]

# Function to evalute the value of integral 
def trapezoidal (x0, xn, n): 
    
    # Calculate h value
    h = (xn - x0) / n
    
    # Compute sum of first and last terms to create formula
    Total = y[0] + y[n]
    
    # Add middle terms to formula
    for i in range(1, n):
        Total += 2*y[i] 
        i += 1
    
    # Finalize the trapezodial formula
    return ((h / 2) * Total)

print ("The total profit of the beverage company over nine-month" 
       "period is ","%.4f" % trapezoidal(x0, xn, n), 
       "in thousand of dollars. ")

print("this code is updated by Isiwara")
print("this is edited by python branch")