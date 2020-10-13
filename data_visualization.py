import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

with open('data/black_mirror.json','r') as f:
    tv_01 = f.read()
with open('data/game_of_thrones.json','r') as f:
    tv_02 = f.read()

black_mirror = []
black_mirror = json.loads(tv_01)

game_of_thrones = []
game_of_thrones = json.loads(tv_02)

avg_run_time = {}
run_times_s1 = []
run_times_s2 = []
run_times_s3 = []

# Creating the dictionary with season 1,2,3 and extracting the run time values and placing them into a list based on the season
for season in ['S1', 'S2', 'S3']:
    avg_run_time[season] = 0
for episode in black_mirror["_embedded"]["episodes"]:
    if episode["season"] == 1:
        run_times_s1.append(episode["runtime"])
    if episode["season"] == 2:
        run_times_s2.append(episode["runtime"])
    if episode["season"] == 3:
        run_times_s3.append(episode["runtime"])

# Calculating the average runtime per season
avg_run_time_s1 = sum(run_times_s1) / 3
avg_run_time_s2 = sum(run_times_s2) / 3
avg_run_time_s3 = sum (run_times_s3) / 6

avg_run_time["S1"] = avg_run_time_s1
avg_run_time["S2"] = avg_run_time_s2
avg_run_time["S3"] = avg_run_time_s3

# Generating the plot for Black Mirror Data
fig, ax = plt.subplots()
ax.set(
    xlabel = 'Seasons of Black Mirror',
    ylabel='Average Episode Runtime in Minutes',
    )

x = list(sorted(avg_run_time.keys()))
heights = []

for label in avg_run_time:
    heights.append(avg_run_time[label])

ax.bar(x, heights)
plt.show()


# Creating the dictionary for episode runtimes
s1_ep_times = {}
s2_ep_times = {}
s3_ep_times = {}
s4_ep_times = {}
s5_ep_times = {}
s6_ep_times = {}
s7_ep_times = {}
s8_ep_times = {}
for episode in game_of_thrones["_embedded"]["episodes"]:
    if episode["season"] == 1:
        s1_ep_times[episode["number"]] = ""
        s1_ep_times[episode["number"]] = episode["runtime"]
    if episode["season"] == 2:
        s2_ep_times[episode["number"]] = ""
        s2_ep_times[episode["number"]] = episode["runtime"]
    if episode["season"] == 3:
        s3_ep_times[episode["number"]] = ""
        s3_ep_times[episode["number"]] = episode["runtime"]
    if episode["season"] == 4:
        s4_ep_times[episode["number"]] = ""
        s4_ep_times[episode["number"]] = episode["runtime"]
    if episode["season"] == 5:
        s5_ep_times[episode["number"]] = ""
        s5_ep_times[episode["number"]] = episode["runtime"]
    if episode["season"] == 6:
        s6_ep_times[episode["number"]] = ""
        s6_ep_times[episode["number"]] = episode["runtime"]
    if episode["season"] == 7:
        s7_ep_times[episode["number"]] = ""
        s7_ep_times[episode["number"]] = episode["runtime"]
    if episode["season"] == 8:
        s8_ep_times[episode["number"]] = ""
        s8_ep_times[episode["number"]] = episode["runtime"]

# Using the dictionary to build a list for the x varibale (keys) and a list for the y variable (values)
s1 = list(sorted(s1_ep_times.keys()))
s1_heights = []
for label in s1_ep_times:
    s1_heights.append(s1_ep_times[label])

s2 = list(sorted(s2_ep_times.keys()))
s2_heights = []
for label in s2_ep_times:
    s2_heights.append(s2_ep_times[label])

s3 = list(sorted(s1_ep_times.keys()))
s3_heights = []
for label in s3_ep_times:
    s3_heights.append(s3_ep_times[label])

s4 = list(sorted(s4_ep_times.keys()))
s4_heights = []
for label in s4_ep_times:
    s4_heights.append(s4_ep_times[label])

s5 = list(sorted(s5_ep_times.keys()))
s5_heights = []
for label in s5_ep_times:
    s5_heights.append(s5_ep_times[label])

s6 = list(sorted(s6_ep_times.keys()))
s6_heights = []
for label in s6_ep_times:
    s6_heights.append(s6_ep_times[label])

s7 = list(sorted(s7_ep_times.keys()))
s7_heights = []
for label in s7_ep_times:
    s7_heights.append(s7_ep_times[label])

s8 = list(sorted(s8_ep_times.keys()))
s8_heights = []
for label in s8_ep_times:
    s8_heights.append(s8_ep_times[label])

# Labeling the plot
plt.xlabel("Episode Number")
plt.ylabel("Runtime in Minutes")

# Legend
green_patch = mpatches.Patch(color = 'green', label = 'Season 1')
yellow_patch = mpatches.Patch(color = 'yellow', label = 'Season 2')
purple_patch = mpatches.Patch(color = 'purple', label = 'Season 3')
red_patch = mpatches.Patch(color = 'red', label = 'Season 4')
blue_patch = mpatches.Patch(color = 'blue', label = 'Season 5')
brown_patch = mpatches.Patch(color = 'brown', label = 'Season 6')
orange_patch = mpatches.Patch(color = 'orange', label = 'Season 7')
black_patch = mpatches.Patch(color = 'black', label = 'Season 8')

plt.legend(handles = [green_patch, yellow_patch, purple_patch, red_patch, blue_patch, brown_patch, orange_patch, black_patch], loc = 0, bbox_to_anchor = (1.05,1))

# Creating the smooth lines with the new list values
plt.plot(s1, s1_heights, color = 'green')
plt.plot(s2, s2_heights, color = 'yellow')
plt.plot(s3, s3_heights, color = 'purple')
plt.plot(s4, s4_heights, color = 'red')
plt.plot(s5, s5_heights, color = 'blue')
plt.plot(s6, s6_heights, color = 'brown')
plt.plot(s7, s7_heights, color = 'orange')
plt.plot(s8, s8_heights, color = 'black')

plt.grid(True)
plt.show()

