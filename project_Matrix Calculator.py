# =========================================
# ADVANCED MATRIX CALCULATOR
# =========================================

# -------- Display Matrix in Bracket Style --------
def print_matrix(matrix, name=""):
    if name != "":
        print(f"\n{name} =")

    for row in matrix:
        print("[ ", end="")
        for val in row:
            print(f"{val:4}", end=" ")
        print("]")


# -------- Input Matrix --------
def input_matrix(rows, cols, name):
    matrix = []
    print(f"\nEnter values for Matrix {name}")

    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"{name}[{i}][{j}] = "))
            row.append(val)
        matrix.append(row)

    return matrix


# -------- Addition --------
def add_matrices(matrices):
    result = matrices[0]

    for m in matrices[1:]:
        temp = []
        for i in range(len(result)):
            row = []
            for j in range(len(result[0])):
                row.append(result[i][j] + m[i][j])
            temp.append(row)
        result = temp

    return result


# -------- Subtraction --------
def subtract_matrices(matrices):
    result = matrices[0]

    for m in matrices[1:]:
        temp = []
        for i in range(len(result)):
            row = []
            for j in range(len(result[0])):
                row.append(result[i][j] - m[i][j])
            temp.append(row)
        result = temp

    return result


# -------- Multiplication --------
def multiply_matrix(A, B):
    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    return result


# -------- Transpose --------
def transpose_matrix(A):
    result = []

    for i in range(len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        result.append(row)

    return result


# =========================================
# MAIN PROGRAM
# =========================================

while True:

    print("\n================================")
    print("        MATRIX CALCULATOR")
    print("================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")

    try:
        choice = int(input("Select operation: "))
    except:
        print("Invalid input! Try again.")
        continue

    # ---------- ADDITION ----------
    if choice == 1:

        count = int(input("How many matrices (2 or 3)? "))

        if count == 2 or count == 3:

            rows = int(input("Rows: "))
            cols = int(input("Columns: "))

            matrices = []

            for i in range(count):
                matrices.append(input_matrix(rows, cols, chr(65+i)))

            result = add_matrices(matrices)

            # Display Expression
            print("\n------ RESULT ------")
            for i in range(count):
                print_matrix(matrices[i], f"Matrix {chr(65+i)}")
                if i < count-1:
                    print("   +")

            print("   =")
            print_matrix(result, "Result")

        else:
            print("Only 2 or 3 matrices allowed!")

    # ---------- SUBTRACTION ----------
    elif choice == 2:

        count = int(input("How many matrices (2 or 3)? "))

        if count == 2 or count == 3:

            rows = int(input("Rows: "))
            cols = int(input("Columns: "))

            matrices = []

            for i in range(count):
                matrices.append(input_matrix(rows, cols, chr(65+i)))

            result = subtract_matrices(matrices)

            print("\n------ RESULT ------")
            for i in range(count):
                print_matrix(matrices[i], f"Matrix {chr(65+i)}")
                if i < count-1:
                    print("   -")

            print("   =")
            print_matrix(result, "Result")

    # ---------- MULTIPLICATION ----------
    elif choice == 3:

        r1 = int(input("Rows of Matrix A: "))
        c1 = int(input("Columns of Matrix A: "))
        r2 = int(input("Rows of Matrix B: "))
        c2 = int(input("Columns of Matrix B: "))

        A = input_matrix(r1, c1, "A")
        B = input_matrix(r2, c2, "B")

        if c1 == r2:
            result = multiply_matrix(A, B)

            print("\n------ RESULT ------")
            print_matrix(A, "Matrix A")
            print("   ×")
            print_matrix(B, "Matrix B")
            print("   =")
            print_matrix(result, "Result")
        else:
            print("Multiplication not possible!")

    # ---------- TRANSPOSE ----------
    elif choice == 4:

        rows = int(input("Rows: "))
        cols = int(input("Columns: "))

        A = input_matrix(rows, cols, "A")
        result = transpose_matrix(A)

        print("\n------ RESULT ------")
        print_matrix(A, "Matrix A")
        print("Transpose =")
        print_matrix(result, "Result")

    else:
        print("\n✨ Nothing for now... Choose a valid option ✨")