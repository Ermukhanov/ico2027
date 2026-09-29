#!/usr/bin/env python3
"""
rsa_auto.py — пробует несколько путей решения RSA-задачи по очереди,
вместо того чтобы упасть на первой же непригодной попытке.
Использование: python3 rsa_auto.py N E C
"""
import sys

def bytes_from_int(m):
    try:
        b = m.to_bytes((m.bit_length() + 7) // 8, 'big')
        return b
    except Exception:
        return None

def try_print(label, m):
    b = bytes_from_int(m)
    print(f"[{label}] m = {m}")
    if b:
        try:
            print(f"[{label}] as text: {b.decode(errors='replace')}")
        except Exception:
            pass

def main():
    if len(sys.argv) != 4:
        print("usage: rsa_auto.py N E C")
        sys.exit(1)
    n, e, c = (int(x) for x in sys.argv[1:4])

    print(f"n bits: {n.bit_length()}, e = {e}")

    # --- Путь 1 (дешёвый, первым): c = m^e БЕЗ взятия остатка по модулю ---
    try:
        import sympy
        m, exact = sympy.integer_nthroot(c, e)
        print(f"[*] Проверка целочисленного {e}-го корня из c: exact={exact}")
        if exact:
            try_print("integer-nth-root", m)
            return
    except Exception as ex:
        print(f"[-] integer_nthroot не удался: {ex}")

    # --- Путь 2 (дешёвый): c + k*n тоже может быть точным корнем ---
    try:
        import sympy
        for k in range(1, 6):
            cand = c + k * n
            m, exact = sympy.integer_nthroot(cand, e)
            if exact:
                print(f"[*] Нашлось при c + {k}*n")
                try_print(f"low-exponent-broadcast (k={k})", m)
                return
    except Exception as ex:
        print(f"[-] Broadcast-путь не удался: {ex}")

    # --- Путь 3 (дорогой, последним, с ограничением времени): факторизация n ---
    try:
        import sympy
        print("[*] Пробую факторизовать n (лимит по времени — если n большой простой*простой, скорее всего не выйдет)...")
        factors = sympy.factorint(n, limit=10**5)  # маленький лимит — быстро сдаться, если не выходит
        if len(factors) >= 2 or (len(factors) == 1 and list(factors.values())[0] > 1):
            print(f"[+] Факторизация: {factors}")
            primes = []
            for p, k in factors.items():
                primes.extend([p] * k)
            if len(primes) == 2:
                p, q = primes
                phi = (p - 1) * (q - 1)
                try:
                    d = pow(e, -1, phi)
                    m = pow(c, d, n)
                    try_print("classic-RSA", m)
                    return
                except ValueError:
                    print("[-] e не обратим по модулю phi(n) — классический путь не подходит.")
        else:
            print("[-] n не факторизуется быстро (вероятно, большие простые множители).")
    except Exception as ex:
        print(f"[-] Факторизация не удалась/пропущена: {ex}")

    print("[-] Ни один автоматический путь не сработал.")
    print("    Проверь: может это Wiener attack (маленькое d), common modulus")
    print("    (два шифротекста с одним n, разными e), или Coppersmith (частично известное m).")
    print("    Смотри 07_CHEATSHEETS/16_CRYPTO.md для деталей этих атак.")

if __name__ == "__main__":
    main()
