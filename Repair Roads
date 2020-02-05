#include <bits/stdc++.h>
using namespace std;
int p[10005],t[10005],n;
vector <int> vec[10005];
void dfs(int pos,int fa)
{int nt[3],cnt=0,d=0;
nt[0]=nt[1]=nt[2]=0;
for (int i=0;i<vec[pos].size();i++)
{if (vec[pos][i]==fa) {continue;}
dfs(vec[pos][i],pos);d++;
cnt+=p[vec[pos][i]];
nt[t[vec[pos][i]]]++;
}
if (d==0)
{p[pos]=0;t[pos]=2;return;}
if (nt[0]==0)
{if (nt[2]!=0) {p[pos]=cnt+1;t[pos]=0;}
else {p[pos]=cnt;t[pos]=2;}
}
else
{p[pos]=cnt-nt[0]/2;
if (nt[0]&1) {t[pos]=0;}
else {t[pos]=1;}
}
}
int main (){
    int cas,i,u,v;
    scanf ("%d",&cas);
    while (cas--)
    {scanf ("%d",&n);
    for (i=1;i<=n;i++)
    {vec[i].clear();}
    for (i=1;i<n;i++)
    {scanf ("%d%d",&u,&v);
    u++;v++;
    vec[u].push_back(v);
    vec[v].push_back(u);
    }
    dfs(1,0);
    printf ("%d\n",p[1]);
    }
    return 0;
}
