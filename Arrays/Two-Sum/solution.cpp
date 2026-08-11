#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Map to store: Key = number, Value = its original index
        std::unordered_map<int, int> numMap;
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            
            // Check if the required complement already exists in our map
            if (numMap.find(complement) != numMap.end()) {
                // Return the index of the complement and the current index
                return {numMap[complement], i};
            }
            
            // If not found, insert the current number and its index into the map
            numMap[nums[i]] = i;
        }
        
        // Return an empty vector if no solution is found (though the problem guarantees one)
        return {};
    }
};


