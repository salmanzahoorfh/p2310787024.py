__doc__='calculatying and plotting the braking distance'

import matplotlib.pyplot as plt

def get_friction_coefficient(road_type, wet_dry):
  mu = {
    'concrete': {'dry': 0.5, 'wet': 0.35},
    'ice': {'dry': 0.15, 'wet': 0.08},}
  return mu[road_type][wet_dry]

def main():
  # Get user input
  velocity = float(input('Enter the initial velocity (m/s): '))
  road_type = input('Enter the road type (concrete/ice): ').lower()
  wet_dry = input('Enter the road condition (dry/wet): ').lower()

  gravity = 9.8
  time_step = 0.1
  distance = 0
  friction_coefficient = get_friction_coefficient(road_type, wet_dry)

  distance_values = [0]
  time_values = [0]
  velocity_values = [velocity]

  while velocity > 0:
    velocity -= friction_coefficient * gravity * time_step
    distance += velocity * time_step

    time_values.append(time_values[-1] + time_step)
    velocity_values.append(velocity)
    distance_values.append(distance)

  plot_simulation_results(time_values, distance_values, velocity_values)

def plot_simulation_results(time_values, distance_values, velocity_values):
  plt.subplot(2, 1, 1)
  plt.plot(time_values, distance_values)
  plt.title('Braking Distance Simulation')
  plt.xlabel('Time (s)')
  plt.ylabel('Distance (m)')
  plt.grid(True)

  plt.subplot(2, 1, 2)
  plt.plot(time_values, velocity_values)
  plt.title('Velocity vs. Time')
  plt.xlabel('Time (s)')
  plt.ylabel('Velocity (m/s)')
  plt.grid(True)

  plt.tight_layout()
  plt.show()

if __name__ == '__main__':
  main()