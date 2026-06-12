class Solution {
public:
    int max_occ(vector<int> &nums, int i) {
        int max = 0;
        while (i < nums.size() && nums[i]) {
            i += 1;
            max += 1;
        }
        return (max);
    }
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max = 0;
        for (size_t i = 0; i < nums.size(); i += 1) {
            if (nums[i] == 1) {
                 int result = max_occ(nums, i);
                 if (result > max)
                    max = result;
            }
        }
        return (max);
    }
};