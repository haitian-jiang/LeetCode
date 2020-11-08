#include <cmath>
#include <complex>
#include <cstring>
#include <iostream>
#include <algorithm>
typedef std::complex<double> Complex;
const int MAX_LEN = 65536 * 2;
const double PI = acos(-1.0);/*NOLINT*/
Complex a[MAX_LEN];
Complex b[MAX_LEN];

void fft(Complex* a, int n, int mod){
    static Complex buffer[MAX_LEN];
    // base case
    if (n == 1){
        return;
    }
    // rearrange even and odd
    int mid = n / 2;
    for (int i = 0; i < mid; ++i) {
        buffer[i] = a[2 * i];
        buffer[mid + i] = a[2 * i + 1];
    }
    for (int i = 0; i < n; ++i) {
        a[i] = buffer[i];
    }
    // recursion
    fft(a, mid, mod);
    fft(a + mid, mid, mod);
    // merge
    Complex wn = {cos(-mod*2*PI/n), sin(-mod*2*PI/n)};
    Complex w = {1, 0};
    for (int i = 0; i < mid; ++i) {
        buffer[i] = a[i] + w * a[mid + i];
        buffer[mid + i] = a[i] - w * a[mid + i];
        w *= wn;
    }
    for (int i = 0; i < n; ++i) {
        a[i] = buffer[i];
    }
}

void multiply(const char* sa, const char* sb){
    int la = strlen(sa), lb = strlen(sb);
    int n = (int) pow(2, ceil(log2(std::max(la, lb))) + 1);
    int ans[MAX_LEN];
    memset(ans, 0, sizeof(ans));
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
    fft(a, n, 1);
    fft(b, n, 1);
    for (int i = 0; i < n; ++i) {
        a[i] *= b[i];
    }
    fft(a, n, -1);
    for (int i = 0; i < n; ++i) {
        a[i] /= n;
    }
    for (int i = 0; i < n; ++i) {
        ans[i] += int(a[i].real() + 0.5);
        ans[i + 1] = ans[i] / 10;
        ans[i] %= 10;
    }
    int end = n - 1;
    while (end > 0 && ans[end] == 0){
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
