#include <cstring>
#include <algorithm>
#include <iostream>

typedef long long int ll;
using namespace std;

int main() {
    int n;
    cin >> n;
    ll costs[n];
    for(int i=0;i<n;i++){
        cin >> costs[i];
    }
    sort(costs,costs+n);
    int q;
    cin >> q;
    ll spend[q];
    for(int i=0;i<q;i++){
        cin >> spend[i];
        int l = upper_bound(costs,costs+n,spend[i]) - costs;
        cout << l << "\n";
    }


    return 0;
}