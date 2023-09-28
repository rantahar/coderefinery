
def compute_statistics(temperatures: list[float]) -> float:
    num_measurements = len(temperatures)
    mean = sum(temperatures) / num_measurements
    return mean

def test_compute_statistics():
    test_data = [1,2,3,4]
    mean = compute_statistics(test_data)
    assert mean == 2.5
