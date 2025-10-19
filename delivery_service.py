# Номер посылки 145825277
def min_platforms(robot_weights: list[int], max_capacity: int) -> int:
    """
    Определяет минимальное количество платформ для перевозки роботов.
    
    Алгоритм: метод двух указателей на отсортированном списке весов.
    - Сортируем веса роботов
    - Используем два указателя: на самого легкого и самого тяжелого робота
    - Если оба робота помещаются на платформу - перевозим их вместе
    - Если нет - перевозим только тяжелого робота
    - Считаем количество использованных платформ
    
    Args:
        robot_weights: Список весов роботов
        max_capacity: Максимальная грузоподъемность платформы
        
    Returns:
        Минимальное количество платформ
    """
    sorted_weights = sorted(robot_weights)
    
    light_robot_index = 0
    heavy_robot_index = len(sorted_weights) - 1
    platforms_count = 0
    
    while light_robot_index <= heavy_robot_index:
        light_weight = sorted_weights[light_robot_index]
        heavy_weight = sorted_weights[heavy_robot_index]

        if light_weight + heavy_weight <= max_capacity:
            light_robot_index += 1

        heavy_robot_index -= 1
        platforms_count += 1
    
    return platforms_count


def main() -> None:
    robot_weights = [int(x) for x in input().split()]
    max_capacity = int(input())
    
    print(min_platforms(robot_weights, max_capacity))


if __name__ == "__main__":
    main()
