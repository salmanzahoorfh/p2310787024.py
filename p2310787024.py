import argparse
import matplotlib.pyplot as plt
import numpy as np
#defining variance parameters
def braking_distance(mass, velocity, road_type, wet_dry, inclination):

    # Derive braking distance formula and constants
    g = 9.81  # acceleration due to gravity (m/s^2)
    friction_coefficient = 0.7  # coefficient of friction
    
    braking_distance = (velocity**2) / (2 * g * friction_coefficient)

    # Adjust braking distance based on other parameters
    if road_type == 'wet':
        braking_distance *= 1.2  # Increase braking distance on wet roads
    if inclination > 0:
        braking_distance += inclination * 0.1  # Increase braking distance on inclines
    
    return braking_distance

def simulate_braking_distance(mass, velocity, road_type, wet_dry, inclination, simulation_time=10):
    time_values = np.linspace(0, simulation_time, num=100)
    distance_values = []

    for time in time_values:
        distance = braking_distance(mass, velocity, road_type, wetness, inclination) * time
        distance_values.append(distance)

    return time_values, distance_values

def plot_simulation_results(time_values, distance_values):
    plt.plot(time_values, distance_values)
    plt.title('Braking Distance Simulation')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Simulate braking distance.")
    arg_parser.add_argument("--mass", type=float, default=1000, help="Mass of the vehicle (kg)")
    arg_parser.add_argument("--velocity", type=float, default=30, help="Initial velocity (m/s)")
    arg_parser.add_argument("--road_type", choices=['dry', 'wet'], default='dry', help="Type of road surface")
    arg_parser.add_argument("--wetness", type=float, default=0.0, help="Wetness level (0 to 1)")
    arg_parser.add_argument("--inclination", type=float, default=0.0, help="Road inclination (degrees)")

    cmd_call_args = arg_parser.parse_args()

    # Print the value of the summand_a parameter
    print("Mass:", cmd_call_args.mass)
    print("Velocity:", cmd_call_args.velocity)
    print("Road Type:", cmd_call_args.road_type)
    print("Wetness:", cmd_call_args.wetness)
    print("Inclination:", cmd_call_args.inclination)

    # Simulate braking distance and plot the results
    time_values, distance_values = simulate_braking_distance(
        cmd_call_args.mass,
        cmd_call_args.velocity,
        cmd_call_args.road_type,
        cmd_call_args.wetness,
        cmd_call_args.inclination
    )

    plot_simulation_results(time_values, distance_values)