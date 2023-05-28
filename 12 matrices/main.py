class Matrix:
    # construct from -> order tuple,element list,zero Boolean
    def __init__(self,order,elements,zeroFill=False) -> None:
        m=[

        ]
        rows,columns=order
        if rows*columns==len(elements) or zeroFill==True:
            self.rows=rows
            self.columns=columns
            self.order=f"{rows} x {columns}"
            if rows*columns ==len(elements):
                i=0
                j=columns
                while j<=len(elements):
                    row=elements[i:j]
                    m.append(row)
                    i,j=j,j+columns
                self.matrix=m
            else:
                pass

        else:
            raise ValueError("Incorrect order for the matrix")
    def __str__(self) -> str:
        return f"{self.matrix}"

    # get - return element of a matrix using (i,j)
    # add two matrices
    # multiplication by scalar
    # multipliation of matrix

order=(2,3)
inp=[1,2,3,4,5,6]
m=Matrix(order,inp)
print(m.order)
print()