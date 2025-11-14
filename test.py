import math
import numpy as np
import random

class Coordinate:
    def __init__(self, x: float, y: float):
        self.loc = (x, y)

    def to_tuple(self):
        return self.loc

    def distanceTo(self, coor) -> float:
        x = self.loc[0] - coor.loc[0]
        y = self.loc[1] - coor.loc[1]
        x = x * x
        y = y * y
        dist = math.sqrt(x + y)
        return dist

    def get_x(self) -> float:
        return self.loc[0]

    def get_y(self) -> float:
        return self.loc[1]

def calculate_cluster_center(cluster_coordinates: list[Coordinate]) -> Coordinate:
    center_x = np.average([coordinate.get_x() for coordinate in cluster_coordinates])
    center_y = np.average([coordinate.get_y() for coordinate in cluster_coordinates])
    return Coordinate(center_x, center_y)

def calculate_squared_error(center: Coordinate, coordinates: list[Coordinate]) -> float:
    return np.sum(np.square([center.distanceTo(coordinate) for coordinate in coordinates]))

def calculate_sum_squared_error(clusters, centers):
    objective = 0
    for cluster_name, cluster_coordinates in clusters.items():
        cluster_center = centers[cluster_name]
        objective += calculate_squared_error(cluster_center, cluster_coordinates)
    return objective

def test_center_calculation():
    """
    Tests the calculate_cluster_center function.
    """
    print("--- Testing Center Calculation ---")
    cluster = [Coordinate(1, 2), Coordinate(3, 4), Coordinate(5, 6)]
    center = calculate_cluster_center(cluster)
    print(f"Cluster: {[c.to_tuple() for c in cluster]}")
    print(f"Expected Center: (3.0, 4.0)")
    print(f"Calculated Center: {center.to_tuple()}")
    assert math.isclose(center.get_x(), 3.0) and math.isclose(center.get_y(), 4.0), "Center calculation is incorrect!"
    print("Center calculation test passed!")

def test_single_cluster_sse():
    """
    Tests the calculate_squared_error function for a single cluster.
    """
    print("\n--- Testing Single Cluster SSE Calculation ---")
    center = Coordinate(3, 4)
    cluster = [Coordinate(1, 2), Coordinate(3, 4), Coordinate(5, 6)]
    sse = calculate_squared_error(center, cluster)
    print(f"Center:. {center.to_tuple()}")
    print(f"Cluster: {[c.to_tuple() for c in cluster]}")
    print(f"Expected SSE: 16.0")
    print(f"Calculated SSE: {sse}")
    assert math.isclose(sse, 16.0), "Single cluster SSE calculation is incorrect!"
    print("Single cluster SSE calculation test passed!")

def test_multi_cluster_sse():
    """
    Tests the calculate_sum_squared_error function for multiple clusters.
    """
    print("\n--- Testing Multi-Cluster SSE Calculation ---")
    clusters = {
        'cluster1': [Coordinate(1, 2), Coordinate(3, 4)],
        'cluster2': [Coordinate(5, 6), Coordinate(7, 8)]
    }
    centers = {
        'cluster1': Coordinate(2, 3),
        'cluster2': Coordinate(6, 7)
    }
    total_sse = calculate_sum_squared_error(clusters, centers)
    print("Clusters:")
    for name, coords in clusters.items():
        print(f"  {name}: {[c.to_tuple() for c in coords]}")
    print("Centers:")
    for name, center in centers.items():
        print(f"  {name}: {center.to_tuple()}")
    print(f"Expected Total SSE: 8.0")
    print(f"Calculated Total SSE: {total_sse}")
    assert math.isclose(total_sse, 8.0), "Multi-cluster SSE calculation is incorrect!"
    print("Multi-cluster SSE calculation test passed!")


if __name__ == "__main__":
    test_center_calculation()
    test_single_cluster_sse()
    test_multi_cluster_sse()```
