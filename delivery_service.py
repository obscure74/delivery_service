# Номер посылки 145825277
from typing import List

def min_platforms(weights: List[int], limit: int) -> int:
    """
    Определяет минимальное количество платформ для перевозки роботов.
    
    Args:
        weights: Список весов роботов
        limit: Максимальная грузоподъемность платформы
        
    Returns:
        Минимальное количество платформ
    """
    # Сортируем веса для применения метода двух указателей
    weights.sort()
    
    left: int = 0
    right: int = len(weights) - 1
    platforms: int = 0
    
    while left <= right:
        # Если самый тяжелый и самый легкий робот помещаются на одну платформу
        if weights[left] + weights[right] <= limit:
            left += 1  # Забираем легкого робота
            right -= 1  # Забираем тяжелого робота
        else:
            # Если не помещаются, берем только тяжелого робота
            right -= 1
        
        platforms += 1
    
    return platforms


def main() -> None:
    # Чтение входных данных
    weights = list(map(int, input().split()))
    limit = int(input())
    
    # Вычисление результата
    result = min_platforms(weights, limit)
    print(result)


if __name__ == "__main__":
    main()