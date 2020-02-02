/*
Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle in a fixed direction.
The task is to choose the safe place in the circle so that when you perform these operations starting from 1st place in the circle, you are the last one remaining and survive.
 
Input Format:
The first line of input contains an integer T denoting the number of test cases . Then T test cases follow. Each test case contains 2 integers n and k .

Output Format:
For each test case, in a new line, output will be the safe position which satisfies the above condition.

Your Task:
This is a function problem. You are required to complete the function josephus that takes two parameters n and k and returns an integer denoting safe position .

Constraints:
1 <= T <= 100
1 <= k, n <= 20

Example:
Input:
2
3 2
5 3
Output
3
4
*/
#include <bits/stdc++.h>
using namespace std;


int josephus(int n, int k);

int main() {
	int t;
    cout << "Enter number of test cases" << endl;
	cin >> t;
	while(t--)
	{
		int n, k;
		cin >> n >> k;
		cout<< josephus(10,4) << endl;
        cout << "--------" << endl;
	}
	return 0;
}

int josephus(int n, int k) {
    int arr[] = {};
    for (int i = 0; i <= n; i++) {
        arr[i] = i + 1;
    }
    cout << arr;
}
