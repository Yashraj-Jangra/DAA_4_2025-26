#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// The complex recursive function
void complexRec(int n) {
    if (n <= 2) {
        return;
    }

    // Work Phase: Allocations and bitwise logic
    int p = n;
    while (p > 0) {
        vector<int> temp(n);
        for (int i = 0; i < n; i++) {
            temp[i] = i ^ p;
        }
        p >>= 1;
    }

    vector<int> small(n);
    for (int i = 0; i < n; i++) {
        small[i] = i * i;
    }

    if (n % 3 == 0) {
        reverse(small.begin(), small.end());
    } else {
        reverse(small.begin(), small.end());
    }

    // Three-way recursion
    complexRec(n / 2);
    complexRec(n / 2);
    complexRec(n / 2);
}

int main() {
    cout << "Testing complexRec in a simple loop..." << endl;
    cout << "======================================" << endl;

    // Simple loop test from 10 to 100
    for (int i = 10; i <= 100; i += 10) {
        cout << "Testing n = " << i << "... " << flush;
        
        complexRec(i);
        
        cout << "Completed!" << endl;
    }

    cout << "======================================" << endl;
    cout << "All tests finished." << endl;

    return 0;
}