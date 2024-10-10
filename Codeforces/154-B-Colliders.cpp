#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

const int MAXN = 100000;

vector<int> primes;
vector<int> spf(MAXN + 1);  // Smallest prime factor (for prime factorization)

// Fungsi untuk melakukan sieve of Eratosthenes dan menentukan faktor prima terkecil
void sieve() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXN; ++i) {
        if (spf[i] == i) {  // i adalah bilangan prima
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

// Fungsi untuk mendapatkan faktor-faktor prima dari bilangan x
vector<int> get_prime_factors(int x) {
    vector<int> factors;
    while (x != 1) {
        int prime_factor = spf[x];
        while (x % prime_factor == 0) x /= prime_factor;
        factors.push_back(prime_factor);
    }
    return factors;
}

int main() {
    int n, m;
    cin >> n >> m;

    sieve();  // Lakukan sieve untuk mendapatkan faktor prima

    vector<bool> is_active(n + 1, false);  // status aktif/nonaktif collider
    unordered_map<int, int> prime_to_collider;  // Peta untuk melacak collider mana yang memiliki faktor prima tertentu

    while (m--) {
        char op;
        int i;
        cin >> op >> i;

        if (op == '+') {  // Aktivasi collider
            if (is_active[i]) {
                cout << "Already on" << endl;
            } else {
                // Dapatkan faktor-faktor prima dari collider i
                vector<int> factors = get_prime_factors(i);
                bool conflict = false;
                int conflicting_collider = -1;

                // Cek apakah ada konflik dengan collider aktif
                for (int prime : factors) {
                    if (prime_to_collider.count(prime)) {
                        conflict = true;
                        conflicting_collider = prime_to_collider[prime];
                        break;
                    }
                }

                if (conflict) {
                    cout << "Conflict with " << conflicting_collider << endl;
                } else {
                    // Jika tidak ada konflik, aktifkan collider i dan tandai semua faktor primanya
                    is_active[i] = true;
                    for (int prime : factors) {
                        prime_to_collider[prime] = i;
                    }
                    cout << "Success" << endl;
                }
            }
        } else if (op == '-') {  // Deaktivasi collider
            if (!is_active[i]) {
                cout << "Already off" << endl;
            } else {
                // Dapatkan faktor-faktor prima dari collider i
                vector<int> factors = get_prime_factors(i);
                is_active[i] = false;

                // Hapus collider dari peta faktor prima
                for (int prime : factors) {
                    if (prime_to_collider[prime] == i) {
                        prime_to_collider.erase(prime);
                    }
                }
                cout << "Success" << endl;
            }
        }
    }

    return 0;
}
