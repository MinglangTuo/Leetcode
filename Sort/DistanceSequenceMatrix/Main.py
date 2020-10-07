from DistanceSequenceMatrix import distanceSequenceMatrix
class main():
    new_distance_matrix = distanceSequenceMatrix()
    new_distance_matrix.points(2,2)
    new_distance_matrix.calculateDistance(0,1)
    print(new_distance_matrix.distances)
