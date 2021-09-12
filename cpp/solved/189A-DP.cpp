#include <iostream>
#include <cstring>
using namespace std;


void arrange(int* a,int* b,int* c) {
    if(*b < *a) {
        swap(*a,*b);
    }
    if(*c < *a) {
        swap(*a,*c);
    }
    if(*b > *c) {
        swap(*b,*c);
    }
    return;
}


int main() {
    int n,a,b,c;
    cin >> n >> a >> b >> c;
    long long int dp[5001];
    memset(dp,-1,5000);
    dp[0] = 0;
    arrange(&a,&b,&c);
    ///cout << a << " " << b << " " << c << "\n";
    for(int i=1;i<=n;i++){
        if(i >= a) {
            if(i < b) {
                dp[i] = dp[i-a]+1;
            } else if(i < c) {
                dp[i] = max(dp[i-a],dp[i-b])+1;
            } else {
                dp[i] = max(dp[i-a],max(dp[i-b],dp[i-c]))+1;
            }
            if(dp[i] == 0)dp[i] = -1;
            //cout << i << " " << dp[i] << "\n";
        }
    }

    cout << dp[n] << "\n";
    return 0;
}