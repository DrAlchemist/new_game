class Wait:
    def __init__ (self, num, place):
        self.num = num
        self.place = place

    def show(self):
        print("Location", str(self.num) + "th",  self.place)

AClass = Wait(3, "Wall street")
AClass.show()

# 1 0 0
# 0 1 0
# 0 0 1

class Matrix:
    A = [[],[],[]]
    B = [[],[],[]]
    C = [[],[],[]]

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def determenant(self):
        detA = (self.A[0][0]*self.A[1][1]*self.A[2][2]+self.A[0][1]*self.A[1][2]*self.A[2][0]+self.A[1][0]*self.A[2][1]*self.A[0][2]) - (self.A[0][2]*self.A[1][1]*self.A[2][0]+self.A[0][1]*self.A[1][0]*self.A[2][2]+self.A[2][1]*self.A[1][2]*self.A[0][0])
        detB = (self.B[0][0]*self.B[1][1]*self.B[2][2]+self.B[0][1]*self.B[1][2]*self.B[2][0]+self.B[1][0]*self.B[2][1]*self.B[0][2]) - (self.B[0][2]*self.B[1][1]*self.B[2][0]+self.B[0][1]*self.B[1][0]*self.B[2][2]+self.B[2][1]*self.B[1][2]*self.B[0][0])
        
        print("det A =", detA)
        print("det B =", detB)

    def sum_matrix(self):
        for i in range(len(self.A)):
            row = []
            for j in range(len(self.A[0])):
                row.append(self.A[i][j] + self.B[i][j])
            self.C[i] = row

        print("Sum of matrices:")
        for row in self.C:
            print(row)


matA = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
matB = [[1, 5, 6], [-5, 4, 9], [-3, 6, 9]]

informmatrix = Matrix(matA, matB)
informmatrix.determenant()
informmatrix.sum_matrix()