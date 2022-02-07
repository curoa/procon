################################

# ref. https://atcoder.jp/contests/typical90/submissions/24203987
class Convolution:

    def __init__(self):
        self.g = self.primitive_root()
        self.flg_first_butterfly = True
        self.flg_first_butterfly_inv = True
        self.sum_e = [0] * 30
        self.sum_ie = [0] * 30

    @staticmethod
    def primitive_root():
        if (MOD == 2):
            return 1
        if (MOD == 167772161):
            return 3
        if (MOD == 469762049):
            return 3
        if (MOD == 754974721):
            return 11
        if (MOD == 998244353):
            return 3
        divs = [0] * 20
        divs[0] = 2
        count = 1
        x = (MOD - 1) // 2
        while not x % 2 != 0:
            x //= 2
        for i in range(3, x + 1, 2):
            if i**2 > x:
                break
            if x % i == 0:
                divs[count] = i
                count += 1
                while not x % i != 0:
                    x //= i
        if x > 1:
            divs[count] = x
            count += 1
        g = 2
        while True:
            ok = True
            for i in range(count):
                if pow(g, (MOD-1) // divs[i], MOD) == 1:
                    ok = False
                    break
            if ok:
                return g
            g += 1
        raise RuntimeError

    def butterfly(self, a):
        n = len(a)
        h = (n - 1).bit_length()
        if self.flg_first_butterfly:
            self.flg_first_butterfly = False
            es = [0] * 30
            ies = [0] * 30
            mod_m = MOD - 1
            count = (mod_m & -1 * mod_m).bit_length() - 1
            e = pow(self.g, mod_m >> count, MOD)
            ie = pow(e, MOD - 2, MOD)
            for i in range(count - 2, -1, -1):
                es[i] = e
                ies[i] = ie
                e *= e; e %= MOD;
                ie *= ie; ie %= MOD
            now = 1
            for i in range(count - 1):
                self.sum_e[i] = (es[i] * now) % MOD
                now *= ies[i]; now %= MOD;
        for ph in range(1, h + 1):
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            now = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p] * now
                    a[i + offset] = (l + r) % MOD
                    a[i + offset + p] = (l - r) % MOD
                now *= self.sum_e[(~s & -1 * ~s).bit_length() - 1]
                now %= MOD

    def butterfly_inv(self, a):
        n = len(a)
        h = (n - 1).bit_length()
        if self.flg_first_butterfly_inv:
            self.flg_first_butterfly_inv = False
            es = [0] * 30
            ies = [0] * 30
            mod_m = MOD - 1
            count = (mod_m & -1 * mod_m).bit_length() - 1
            e = pow(self.g, mod_m >> count, MOD)
            ie = pow(e, MOD - 2, MOD)
            for i in range(count - 2, -1, -1):
                es[i] = e
                ies[i] = ie
                e *= e; e %= MOD;
                ie *= ie; ie %= MOD
            now = 1
            for i in range(count - 1):
                self.sum_ie[i] = (ies[i] * now) % MOD
                now *= es[i]; now %= MOD;
        for ph in range(h, 0, -1):
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            inow = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p]
                    a[i + offset] = (l + r) % MOD
                    a[i + offset + p] = (l - r) * inow % MOD
                inow *= self.sum_ie[(~s & -1 * ~s).bit_length() - 1]
                inow %= MOD

    # a: list
    # b: list
    def convolution(self, a, b):
        n = len(a)
        m = len(b)
        if n == 0 or m == 0:
            return []
        if min(n, m) <= 60:
            return self.convolution_naive(a, b, n, m)
        size = n + m - 1
        z = 1 << (size - 1).bit_length()
        a += [0] * (z - n)
        b += [0] * (z - m)
        self.butterfly(a)
        self.butterfly(b)
        c = [None] * z
        for i in range(z):
            c[i] = (a[i] * b[i]) % MOD
        self.butterfly_inv(c)
        c = c[:size]
        iz = pow(z, MOD - 2, MOD)
        for i in range(size):
            c[i] *= iz; c[i] % MOD
        return c

    def convolution_naive(self, a, b, n, m):
        ans = [0] * (n + m -1)
        for i in range(n):
            for j in range(m):
                ans[i+j] += a[i] * b[j]
                ans[i+j] %= MOD
        return ans

################################
