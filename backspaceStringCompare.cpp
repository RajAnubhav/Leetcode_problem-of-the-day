#include<bits/stdc++.h>
using namespace std;

class Solution {
    public:
    string processString(string str) {
        string processed;
        for(char c: str) {
            if(c == '#' && !processed.empty())
                processed.pop_back();
            else if(c!='#')
                processed.push_back(c);
        }
        return processed;
    }
    bool backspaceCompare(string s, string t) {
        return processString(s) == processString(t);
    }
};

int main() {
    Solution sln;
    string s = "ab#c", t = "ad#c";
    bool ans = sln.backspaceCompare(s, t);
    cout<<ans<<endl;
    return 0;
}