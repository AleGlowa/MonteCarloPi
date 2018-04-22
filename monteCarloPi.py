import numpy as np
import matplotlib.pyplot as plt
import time as time

total_random_points = int(input("Liczba losowych punktów do oszacowania liczby Pi: "))

inside_circle = 0

#x_plot_array = np.empty(shape=(1, total_random_points))
#y_plot_array = np.empty(shape=x_plot_array.shape)

start_time = time.time()

for i in range(total_random_points):
    x = np.random.rand()
    #x_plot_array = np.append(x_plot_array, [x])
    y = np.random.rand()
    #y_plot_array = np.append(y_plot_array, [y])
    x_squared = x**2
    y_squared = y**2
    if np.sqrt(x_squared + y_squared) < 1.0:
        inside_circle += 1

pi_approx = (inside_circle / total_random_points) * 4
print("Oszacowana wartość: %f" % pi_approx)
print("Różnica między oszacowaną a dokładną liczbą Pi: %f" % (abs(pi_approx-np.pi)))
#print("Błąd w procentach: %f" % ((abs(pi_approx - np.pi)) / np.pi) * 100)
print("Czas wykonania: %f sekund" % (time.time() - start_time))

#random_points_plot = plt.scatter(x_plot_array, y_plot_array, color='blue', s=.5)
#circle_plot = plt.Circle((0, 0), 1, color='red', linewidth=2, fill=False)

#ax = plt.gca()
#ax.cla()
#plt.xlim(-1.0, 1.0)
#plt.ylim(-1.0, 1.0)

#ax.add_artist(random_points_plot)
#ax.add_artist(circle_plot)

#plt.show()
