"""
Given a string of digits S, insert a minimum number of opening and closing parentheses into it such that the resulting string is balanced and each digit d is inside exactly d pairs of matching parentheses.

Let the nesting of two parentheses within a string be the substring that occurs strictly between them. An opening parenthesis and a closing parenthesis that is further to its right are said to match if their nesting is empty, or if every parenthesis in their nesting matches with another parenthesis in their nesting. The nesting depth of a position p is the number of pairs of matching parentheses m such that p is included in the nesting of m.

For example, in the following strings, all digits match their nesting depth: 0((2)1), (((3))1(2)), ((((4)))), ((2))((2))(1). The first three strings have minimum length among those that have the same digits in the same order, but the last one does not since ((22)1) also has the digits 221 and is shorter.

Given a string of digits S, find another string S', comprised of parentheses and digits, such that:
all parentheses in S' match some other parenthesis,
removing any and all parentheses from S' results in S,
each digit in S' is equal to its nesting depth, and
S' is of minimum length.

Input
The first line of the input gives the number of test cases, T. T lines follow. Each line represents a test case and contains only the string S.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the string S' defined above.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ length of S ≤ 100.

Test set 1 (Visible Verdict)
Each character in S is either 0 or 1.

Test set 2 (Visible Verdict)
Each character in S is a decimal digit between 0 and 9, inclusive.
1
111
(111)
121
(1(2)1)
"""

def nest(S):
    count = 0
    for i in range(len(S)):
        print("for 1")
        st1 = ""
        if S[i] == "10": break
        if count == int(S[i]): 
            print("if 1")
            print(count)
            print(st1)
        else:
            print("else 1")
            count += int(S[i]) # c = 1
            print(count)
            for j in range(count):
                print("for 2")
                st1 = st1 + "("  #(
                print(st1)
            st1 += S[i]
        if S[i] == S[i + 1]:
            print("if 2")
            print(i+1, st1)
        else:
            print("else 2")
            for j in range(int(S[i+1]) - int(S[i])):
                print(count)
                st1 = st1 + ")"
                print(st1)
                count -= 1
    if count != 0:
        print(count)
        while count > 0:
            print(count)
            st1 = st1 + ")" 
            count -= 1

    return st1


T = int(input("Total Test Cases: "))
if T <= 100:
    for i in range(T):
        S = input("String of number: ")
        if S <= 100:
            print()
            st1 = nest(S + "10")
            print("Case #", i+1, ": ", st1)
