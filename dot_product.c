#include <stddef.h>

double dot_product(const double *a, const double *b, size_t n) {
    double result = 0.0;
    for (size_t i = 0; i < n; ++i) {
        result += a[i] * b[i];
    }
    return result;
}
