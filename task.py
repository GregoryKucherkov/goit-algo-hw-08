import heapq
import random

def minimize_costs(cables):
    pairs = []
    heapq.heapify(cables)

    #поки в піраміді є білше 1го елемента, повторюємо. В результаті там залишиться один кабель
    while len(cables) > 1:
        #беремо 2 найменші кабелі і з'єднуємо
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cable_pair = (first, second)
        pairs.append(cable_pair)

        # з 2-ох кабелів виходить ще один, тож додємо його у піраміду
        combined_length = first + second
        heapq.heappush(cables, combined_length)
    
    return pairs, list(cables)


# Example usage:
#cables = [5, 8, 3, 2, 7]
cables = [random.randint(1, 100) for _ in range(10)]
print(cables)
result, cost = minimize_costs(cables.copy())

print(f"Порядок з'єднання кабелів для мінімізаціі витрат:{result}")
print(F"Мінімальна вартість:{cost} одиниць")

