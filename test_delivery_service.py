from delivery_service import min_platforms

def test_examples():
    """Тестирование на примерах из условия."""
    assert min_platforms([1, 2], 3) == 1
    assert min_platforms([3, 2, 2, 1], 3) == 3
    assert min_platforms([3, 5, 3, 4], 5) == 4
    print("Все примеры из условия работают!")

def test_edge_cases():
    """Тестирование краевых случаев."""
    assert min_platforms([1], 3) == 1  # Один робот
    assert min_platforms([5, 5, 5, 5], 5) == 4  # Все по одному
    assert min_platforms([1, 1, 1, 1], 2) == 2  # Все пары
    print("Краевые случаи работают!")

if __name__ == "__main__":
    test_examples()
    test_edge_cases()
    print("Все тесты пройдены!")