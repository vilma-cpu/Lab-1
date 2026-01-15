# Uppgift 5

# Om n = oändligheten gäller följande likhet: 

# sigma n k=1 (1/(k^k))=(pi)^2/6

# Skriv ett program som beräknar summan för godtyckligt n och räkna ut hur mycket det avviker från svaret då . Använd ditt program för att beräkna summan för n=10, n=100 och n=1000.

import math

n_values = [10, 100, 1000]
infinity_sum = (math.pi ** 2) / 6

for n in n_values:
    total_sum = 0
    for k in range(1, n + 1):
        total_sum += 1 / (k ** 2)  # Rätt formel!
    deviation = abs(infinity_sum - total_sum)
    print(f"För n={n}: Summan är {total_sum} och avvikelsen från pi^2/6 är {deviation}")
