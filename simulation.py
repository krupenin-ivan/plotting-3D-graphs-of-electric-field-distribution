length = 1400
width = 1000
height = 1000
step = 10

nx = int(length / step)
ny = int(width / step)
nz = int(height / step)

coordinates_centers = []
for i in range(nx):
    for j in range(ny):
        for k in range(nz):
            x = step / 2 + i * step
            y = step / 2 + j * step
            z = step / 2 + k * step
            coordinates_centers.append([x, y, z])

potentials_coordinates_centers = []
for i in range(len(coordinates_centers)):
    potentials_coordinates_centers.append(0)

print(len(potentials_coordinates_centers))
