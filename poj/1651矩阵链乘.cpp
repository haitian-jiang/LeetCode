#include <cstdio>
#include <algorithm>

const int MAX_N = 120;
const int INF = 2147483647;
int size[MAX_N];
int dp_memory[MAX_N][MAX_N];

int dp(int start, int end){
    if (start == end or dp_memory[start][end]){
        return dp_memory[start][end];
    }
    int result = INF;
    for (int k = 0; k < end - start; ++k) {
        int mult_time = dp(start, start + k) + dp(start + k + 1, end) + size[start-1]*size[start+k]*size[end];
        result = std::min(result, mult_time);
    }
    dp_memory[start][end] = result;
    return result;
}

int main(){
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", size + i);
    }
    printf("%d", dp(1, n - 1));
}