# Open the input file
with open("sample.txt", "r") as f:
  # Read the input data from the file
  input_data = f.read()

# Parse the input data
data = {}
for line in input_data.strip().split("\n"):
  valve, flow, _, *tunnels = line.split()
  data[valve] = (int(flow.split("=")[1]), set(tunnels[1:]) if tunnels else set())

# Initialize the current location to valve AA
current = "AA"

# Initialize the total flow to 0
total_flow = 0

# Initialize the visited valves set
visited = set()

# Keep track of the time
time = 0

while True:
  # Break out of the loop if the time exceeds 30 minutes
  if time > 30:
    break
  
  # Get the flow rate and tunnels for the current valve
  flow, tunnels = data[current]
  
  # If the current valve has not been visited and has a non-zero flow rate, add its flow rate to the total
  if current not in visited and flow > 0:
    total_flow += flow
    visited.add(current)
  
  # Find the next valve to visit
  next_valve = None
  for valve in tunnels:
    if valve not in visited:
      next_valve = valve
      break
  
  # If there is no next valve, break out of the loop
  if next_valve is None:
    break
  
  # Update the current valve and time
  current = next_valve
  time += 1

# Print the total flow
print(total_flow)