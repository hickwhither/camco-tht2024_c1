#include <bits/stdc++.h>
using namespace std;

string a[] = {
    "PLACE_FLAG",
    "MOVE_UP",
    "MOVE_DOWN",
    "MOVE_LEFT",
    "MOVE_RIGHT"
};

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

string team, opponent_step;
int t;
int s[41][41];

signed main()
{
    
    cin >> team >> t;
    for(int i=1; i<=40; ++i)
    for(int j=1; j<=40; ++j) cin >> s[i][j];

    for(int i=1; i<=t; ++i){
        cout << a[rng()%5] << endl; // endl include flush
        cin >> opponent_step;
    }

    return 0;
}


