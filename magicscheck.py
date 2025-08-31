import numpy as np
matrix = np.random.randint(1,50,size = (4,4))
print("Original matrix :" , matrix)
sum_row = np.sum(matrix , axis=1)
print("Sum of rows : " ,sum_row)
sum_cols = np.sum(matrix , axis=0)
print("Sum of columns : " ,sum_cols)
diag_1 = np.sum(np.diag(matrix))
diag_2 = np.sum(np.diag(np.fliplr(matrix)))

# Magic constant (from first row sum)
magic_const = sum_row[0]

# Check condition
if (np.all(sum_row == magic_const) and 
    np.all(sum_cols == magic_const) and 
    diag_1 == magic_const and 
    diag_2 == magic_const):
    print("✅ The matrix IS a Magic Square")
else:
    print("❌ The matrix is NOT a Magic Square")