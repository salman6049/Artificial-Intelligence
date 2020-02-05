#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) FOR(i, 0, n)
#define pb push_back
typedef long long ll;

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

const int N = 10000, MOD = 1000000007;
int fac[N];
vector<int> e[N];

int f(int n)
{
  int path = n, ans = 1;
  REP(i, n)
    if (e[i].size() == 1)
      path--;
  REP(i, n)
    if (e[i].size() > 1) {
      int leaf = 0, inner = 0;
      for (auto v: e[i])
        if (e[v].size() == 1)
          leaf++;
        else
          inner++;
      if (inner > 2)
        return 0;
      ans = ll(ans)*fac[leaf]%MOD;
    }
  return path == 1 ? ans : ans*2%MOD;
}

int main()
{
  for (int cc = ri(); cc--; ) {
    int n = ri();
    REP(i, n)
      e[i].clear();
    fac[0] = 1;
    FOR(i, 1, n)
      fac[i] = ll(fac[i-1])*i%MOD;
    REP(i, n-1) {
      int x = ri(), y = ri();
      e[x].pb(y);
      e[y].pb(x);
    }
    printf("%d\n", f(n));
  }
}
