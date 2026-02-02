#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int>> matrix;

matrix multiplyMatrix(matrix a, matrix b){
    matrix c(2, vector<int>(2, 0));
    for (int row = 0; row < 2; row++){
        for (int col = 0; col < 2; col++){
            for (int k = 0; k < 2; k++){
                c[row][col] += a[row][k] * b[k][col];
            }
        }
    }
    return c;
}

matrix toPow(matrix x, int n){
    matrix result(2, vector<int>(2, 0));
    result[0][0] = 1;
    result[1][1] = 1;

    for (int i = 0; i < n; i++){
        result = multiplyMatrix(result, x);
    }
    return result;
}


void printMat(matrix mat){
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 2; j++){
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}

int main(){
    matrix x = {{1, 1}, {1, 0}};
    // for (int i = 2; i < 10; i+=3){
    //     matrix y = toPow(x, i);
    //     cout << y[0][0] << endl;
    // }
    int temp = 0; int i = 2; int sum = 0;
    while (true){
        matrix y = toPow(x, i);
        temp = y[0][0];
        if (temp > 4000000) break;
        sum += temp;
        i += 3;
    }
    cout << sum << endl;
}