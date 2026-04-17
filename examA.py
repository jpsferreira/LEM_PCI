# let a(m,n) be a matrix and x(n) be a vector
# functions here
# exercise 1
# create a function to compute the vector y in which:
# - first elements are the negatives of a
# - then, followed by the positives with more than 3 digits
# - then, last element is the factorial of the maximum of the last two rows.  
def create_vector(a):
    y, pos =  [], []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] < 0:
                y.append(a[i][j])
            elif a[i][j] > 9:
                pos.append(a[i][j])
    y.extend(pos)
    maxx =a[-2][0]
    for i in range(len(a)-2, len(a)):
        for j in range(len(a[i])):
            if a[i][j] > maxx:
                maxx = a[i][j]
    fact = 1
    for i in range(1, maxx + 1):
        fact *= i
    y.append(fact)
    return y

# create a matrix b where
# - first and last row are the same as vector x
# - second and almost last row are the same, and the product of the last two columns of matrix a
# - the remaining elements have the value 2
def create_matrix(a,x):
    b = [[2 for j in range(len(x))] for i in range(len(a))]
    b[0] = x
    b[-1] = x
    prod = 1
    for i in range(len(a)):
        prod *= a[i][-1]*a[i][-2]
    b[1] = [prod for j in range(len(x))]
    b[-2] = b[1]

    return b

# swap second maximum with the minimum. vector x
def swap(x):
    if len(x) < 2:
        return x
    min_idx, max_idx, second_max_idx = 0, 0, 0
    for i in range(1, len(x)):
        if x[i] < x[min_idx]:
            min_idx = i
        if x[i] > x[max_idx]:
            second_max_idx = max_idx
            max_idx = i
        elif x[i] > x[second_max_idx] and i != max_idx:
            second_max_idx = i

    if second_max_idx != min_idx:
        aux = x[second_max_idx]
        x[second_max_idx] = x[min_idx]
        x[min_idx] = aux

    return x
# test code here
###
a = [[-11, 12, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
print(create_vector(a))

## 
x = [1, 2, 3, 4]
print(create_matrix(a,x))

##
x = [5, 3, 8, 1, 4]
print(f"Before swap: {x}")
print(f"After swap: {swap(x)}")

