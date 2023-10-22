#include<iostream>
#include<vector>
using namespace std;

// here, the approach is using Greedy Algorithm
class Solution {
    public:
    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        int left = k, right = k;
        int ans = nums[k];
        int currmin = nums[k];
        while(left > 0 || right < n-1) {
            if((left > 0 ? nums[left-1]:0) < (right<n-1 ? nums[right+1]:0)) {
                right++;
                currmin = min(currmin, nums[right]);
            } else {
                left--;
                currmin = min(currmin, nums[left]);
            } 
            ans = max(ans, currmin*(right-left+1));
        }
        return ans;
    }
};

int main() {
    Solution sln;
    vector<int>nums = {1,4,3,7,4,5};
    int k = 3;
    int ans = sln.maximumScore(nums, k);
    printf("%d\n", ans);
    return 0;
}