def printmatrix(A):
    for x in range(0, len(A)):
        print(A[x]);

tableX = [[1,150],[1,250],[1,450],[1,600],[1,725]];
tableY = [[74.3],[127],[230],[289],[367]];


def matrixCalc(A, B):
    returnMatrix = [];
    for i in range(0, len(A)):
        returnMatrix.append([]);
        for j in range(0, len(B[0])):
            returnMatrix[i].append([]);

    for i in range(0, len(A)):
        
        for j in range(0, len(B[0])):
            returnMatrix[i][j] = 0;
            for k in range(0, len(A[0])):
                returnMatrix[i][j] += A[i][k] * B[k][j];
    
    return returnMatrix;

def transpose(table):
    returnMatrix = [];

    for i in range(0, len(table[0])):
        returnMatrix.append([]);
        for j in range(0, len(table)):
            returnMatrix[i].append([]);
    
    
    for i in range(0, len(returnMatrix)):
        for j in range(0, len(returnMatrix[i])):
            returnMatrix[i][j] = table[j][i];


    return returnMatrix;

def invert(table):
    #Only works for 2x2
    if len(table) > 2:
        print("Only works for 2x2 Matrix")
        return;

    if len(table[0]) > 2:
        print("Only works for 2x2 Matrix")
        return;
    invertionFormula = (1/((table[0][0]*table[1][1]) - (table[0][1] * table[1][0])));

    return [[table[1][1] * invertionFormula, -1 * table[0][1] * invertionFormula],
            [-1 * table[1][0] * invertionFormula, table[0][0] * invertionFormula]];

def kvadratmetod(xTable, yTable):
    A = matrixCalc(transpose(tableX), tableX)
    C = matrixCalc(transpose(tableX), tableY)
    return matrixCalc(invert(A), C);


printmatrix(kvadratmetod(tableX, tableY))