#include <cmath>
#include <complex>
#include <cstring>
#include <iostream>
#include <algorithm>
typedef std::complex<double> Complex;
const int MAX_LEN = 1 << 17;
const double PI = acos(-1.0);
Complex a[MAX_LEN];
Complex b[MAX_LEN];
Complex A[MAX_LEN];

void recursive_fft(Complex* arr, int n, int mod){
    static Complex buffer[MAX_LEN];
    // base case
    if (n == 1){
        return;
    }
    // rearrange even and odd
    int mid = n / 2;
    for (int i = 0; i < mid; ++i) {
        buffer[i] = arr[2 * i];
        buffer[mid + i] = arr[2 * i + 1];
    }
    for (int i = 0; i < n; ++i) {
        arr[i] = buffer[i];
    }
    // recursion
    recursive_fft(arr, mid, mod);
    recursive_fft(arr + mid, mid, mod);
    // merge
    Complex wn = {cos(-mod*2*PI/n), sin(-mod*2*PI/n)};
    Complex w = {1, 0};
    for (int i = 0; i < mid; ++i) {
        buffer[i] = arr[i] + w * arr[mid + i];
        buffer[mid + i] = arr[i] - w * arr[mid + i];
        w *= wn;
    }
    for (int i = 0; i < n; ++i) {
        arr[i] = buffer[i];
    }
}

void iterative_fft(Complex* arr, int n, int mod){
    int rev[MAX_LEN] = {0,}, log2_n = 0;
    while ((1 << log2_n) < n) {log2_n++;}
    for (int i = 0; i < n; ++i) {
        rev[i]=(rev[i>>1]>>1)|((i&1)<<(log2_n-1));/*NOLINT*/
    }
    for (int i = 0; i < n; ++i) {
        A[rev[i]] = arr[i];
    }
    for (int l = 1; (1 << l) <= n; ++l) {
        int m = 1 << l;
        Complex wm = {cos(-mod*2*PI/m),sin(-mod*2*PI/m)};
        for (int i = 0; i < n; i += m) {
            Complex w = {1, 0};
            for (int j = 0; j < m / 2; ++j) {
                Complex u = A[i + j]; Complex v = w * A[i + j + m/2];
                A[i + j] = u + v; A[i + j + m/2] = u - v;
                w *= wm;
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        arr[i] = A[i];
    }
}

void multiply(const char* sa, const char* sb){
    int la = strlen(sa), lb = strlen(sb);
    int n = (int) pow(2, ceil(log2(std::max(la, lb))) + 1);  // 13 * 15: ifft(fft([3,1,0,0]).*fft([5,1,0,0]))
    for (int i = 0; i < la; ++i) {
        a[i] = {sa[la - i - 1] - 48.0, 0};  // '0' == 48
    }
    for (int i = la; i < n; ++i) {
        a[i] = {0, 0};
    }
    for (int i = 0; i < lb; ++i) {
        b[i] = {sb[lb - i - 1] - 48.0, 0};
    }
    for (int i = lb; i < n; ++i) {
        b[i] = {0, 0};
    }
    iterative_fft(a, n, 1);
    iterative_fft(b, n, 1);
    for (int i = 0; i < n; ++i) {
        a[i] *= b[i];
    }
    iterative_fft(a, n, -1);
    for (int i = 0; i < n; ++i) {
        a[i] /= n;
    }
    int ans[MAX_LEN];
    memset(ans, 0, sizeof(ans));
    for (int i = 0; i < n; ++i) {
        ans[i] += int(a[i].real() + 0.5);
        ans[i + 1] = ans[i] / 10;
        ans[i] %= 10;
    }
    int end = n - 1;
    while (end > 0 && ans[end] == 0){  // end > 0 for 0 * 0 = 0
        end--;
    }
    for (int i = end; i >= 0; --i) {
        printf("%c", ans[i]+'0');
    }
    std::cout << std::endl;
}

int main(){
    char sa[MAX_LEN]={0,}, sb[MAX_LEN]={0,};
    while (std::cin >> sa >> sb){
        multiply(sa, sb);
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
    }
    return 0;
}