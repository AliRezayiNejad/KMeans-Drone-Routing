import math
import random


class Coordinate:
    def __init__(self, x, y):
        self.loc = (round(x, 1), round(y, 1))
    
    # calculates the euclidean distance from self to arg coor
    def distanceTo(self, coor) -> float:
        x = self.loc[0] - coor.loc[0]
        y = self.loc[1] - coor.loc[1]
        x = x*x # will always be positive
        y = y*y # will always be positive
        dist = math.sqrt(x + y)
        return round(dist, 1)
    
    # determines if self is contained in arg of list[Coordinate]
    def isIn(self, coordinates: list) -> bool:
        for coordinate in coordinates:
            if coordinate.get_x() == self.get_x() and coordinate.get_y() == self.get_y():
                return True
        return False

    # returns formatted string for file writing
    def __str__(self) -> str:
        return f"{self.loc[0]}\t{self.loc[1]}"
    
    # getter for x coordinate
    def get_x(self) -> float:
        return self.loc[0]
    
    # getter for y coordinate
    def get_y(self) -> float:
        return self.loc[1]

def k_means_clustering(k, coordinates: list[Coordinate]):
    clusters = {}
    old_clusters = None
    
    # Initialize Centers
    centers = random.sample(coordinates, k)
    
    while True:
        for i in range(k):
            clusters[i] = []
        
        # Decide class memberships
        for coordinate in coordinates:
            shortest_dist = float('inf')
            cluster_idx = -1
            for center_idx, center in enumerate(centers):
                distance_to_center = coordinate.distanceTo(center)
                if distance_to_center < shortest_dist:
                    shortest_dist = distance_to_center
                    cluster_idx = center_idx
            clusters[cluster_idx].append(coordinate)

        if clusters == old_clusters:
            break
        
        # Calculate new centers
        for cluster_idx, cluster_coords in clusters.items():
            x_sum = 0
            y_sum = 0
            for coord in cluster_coords:
                x_sum += coord.get_x()
                y_sum += coord.get_y()
            centers[cluster_idx] = Coordinate(x_sum / len(cluster_coords), y_sum / len(cluster_coords))
        old_clusters = clusters
    return centers, clusters

def calculate_squared_error(centers, clusters):
    objective = 0
    for cluster_idx, cluster_coords in clusters.items():
        cluster_center = centers[cluster_idx]
        for coord in cluster_coords:
            objective += (cluster_center.distanceTo(coord)**2)
    return round(objective, 2)

def main():
    # TODO: Input Handling
    coordinates = [Coordinate(1, 1), Coordinate(1, 2), Coordinate(2, 1), Coordinate(6, 6), Coordinate(6, 5), Coordinate(5,6)]
    distance_matrix = [[coordinate_A.distanceTo(coordinate_B) for coordinate_B in coordinates] for coordinate_A in coordinates]
    # TODO: Cluster for all 1 <= k <= 4

    # Run multiple trials with random starts 
    centers_bsf = None
    clusters_bsf = None
    objective_function = float("inf")
    for _ in range(10):
        centers, clusters = k_means_clustering(2, coordinates)
        score = calculate_squared_error(centers, clusters)
        if score < objective_function:
            objective_function = score
            centers_bsf = centers
            clusters_bsf = clusters
    print(objective_function)
    # TODO: Route Finding
    # TODO: Output Handling


if __name__ == "__main__":
    main()