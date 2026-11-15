class Solution {
public:
    int countConsistent(vector<int>& nums) {
        int ans=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            int m=nums[i],bita=nums[i];
            for(int j=i;j<n;j++){
                bita=bita&nums[j];
                m=min(m,nums[j]);
            
            if (m==bita){
                ans++;
            }
            }
        }
        return ans;
    }
};