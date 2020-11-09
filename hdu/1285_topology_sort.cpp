#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAX_N = 510;
vector<int> G[MAX_N];  // begin from index 1
int in_degree[MAX_N] = {0,};  // begin from index 1
int n = 0, m = 0;
priority_queue<int, vector<int>, greater<int> > Q;
vector<int> sorted;

void read()
{
    while(m--){
        int win = 0, lose = 0;
        cin >> win >> lose;
        G[win].push_back(lose);
    }
}

void calc_in()
{
    for(int from = 1; from <= n; ++from){
        for(vector<int>::iterator p_to = G[from].begin(); p_to < G[from].end(); ++p_to){
            in_degree[*p_to]++;
        }
    }
}

void topology_sort()
{
    for(int node = 1; node <= n; ++node){
        if(in_degree[node] == 0){
            Q.push(node);
        }
    }
    while(!Q.empty()){
        int top = Q.top();
        Q.pop();
        sorted.push_back(top);
        for(vector<int>::iterator p_to = G[top].begin(); p_to < G[top].end(); ++p_to){
            in_degree[*p_to]--;
            if(in_degree[*p_to] == 0){
                Q.push(*p_to);
            }
        }
    }
}

void output()
{
    for(int i = 0; i < n - 1; ++i){
        cout << sorted[i] << " ";
    }
    cout << sorted[n - 1] << endl;
}

int main(int argc, const char *argv[])
{
    while(cin >> n >> m) {
        sorted.clear();
        for(int i = 0; i < MAX_N; ++i){
            G[i].clear();
            in_degree[i] = 0;
        }
        read();
        calc_in();
        topology_sort();
        output();
    }
    return 0;
}
