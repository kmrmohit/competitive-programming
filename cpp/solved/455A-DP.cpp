#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

/**
 * basically sort and keep unique element in the array and individual counts
 * now an element c has three options: it will be the centre element or it will get deleted when the left has value c-1 or when the right has value c+1
 * dp[i] will give us the max sum earned till i-th index, it can be observed that for calculating i we have only three options
 * dp[i] = max(ar[i]+dp[i-2],dp[i-1])
 * 
 * Time Complexity: O(nlogn) , can be solved in O(n)
 * Space Complexity: O(n)
*/

//2 2 3 4 5
//ans[0] = 4
//ans[1] = 4
//ans[2] = 4
//ans[3] = 8
//ans[4] = 9

int main() {
    int n;
    cin >> n;
    long long int ar[n];
    map<long long int,int>mp;
    for(int i=0;i<n;i++){
        cin >> ar[i];
        if(mp.find(ar[i])==mp.end()){
            mp[ar[i]]=1;
        } else mp[ar[i]]++;
    }
    sort(ar,ar+n);
    
    long long int ans[n];
    ans[0] = mp[ar[0]]*ar[0];
    
    for(int i=1;i<n;i++) {
        if(ar[i]==ar[i-1]){
            ans[i]=ans[i-1];continue;
        }
        int li = lower_bound(ar,ar+i,ar[i]-1) - ar - 1;
        if(li+1 == i) {
            ans[i] = mp[ar[i]]*ar[i] + ans[i-1];

        } else {
        if(li < 0) {
            ans[i] = max(mp[ar[i]]*ar[i],ans[li+1]);
        } else {
            ans[i] = max(mp[ar[i]]*ar[i]+ans[li],ans[li+1]);
        }
        }
        //cout << i << " " << ar[i] << " " << li << " " << ans[i] << "\n";
    }
    cout << ans[n-1] << "\n";
    return 0;
}