import math

total_yes = 9
total_no = 5


# Function to calculate entropy
def entropy(pos, neg):
    total = pos + neg
    p_pos = pos / total
    p_neg = neg / total

    if p_pos == 0:
        entropy_pos = 0
    else:
        entropy_pos = -p_pos * math.log2(p_pos)

    if p_neg == 0:
        entropy_neg = 0
    else:
        entropy_neg = -p_neg * math.log2(p_neg)

    return entropy_pos + entropy_neg


# Entire dataset entropy
total_entropy = entropy(total_yes, total_no)

# Outlook attribute
# Sunny
sunny_yes = 2
sunny_no = 3
sunny_entropy = entropy(sunny_yes, sunny_no)

print("sunny_entropy", sunny_entropy)

# Overcast
overcast_yes = 4
overcast_no = 0
overcast_entropy = entropy(overcast_yes, overcast_no)
print("overcast_entropy", overcast_entropy)
# Rain
rain_yes = 3
rain_no = 2
rain_entropy = entropy(rain_yes, rain_no)
print("rain_entropy", rain_entropy)

# Weighted entropy for Outlook
weighted_entropy_outlook = (5 / 14) * sunny_entropy + (4 / 14) * overcast_entropy + (5 / 14) * rain_entropy
print("Sunny fraction", (5 / 14) * sunny_entropy)
print("Overcast fraction", (4 / 14) * overcast_entropy)
print("Rain fraction", (5 / 14) * rain_entropy)

print("weighted_entropy_outlook", weighted_entropy_outlook)

# Information Gain for Outlook
information_gain_outlook = total_entropy - weighted_entropy_outlook
print("Information gain outlook", information_gain_outlook)

# Store results in a dictionary for easier display
results = {
    "Total Entropy": total_entropy,
    "Sunny Entropy": sunny_entropy,
    "Overcast Entropy": overcast_entropy,
    "Rain Entropy": rain_entropy,
    "Weighted Entropy (Outlook)": weighted_entropy_outlook,
    "Information Gain (Outlook)": information_gain_outlook
}
print("Outlook Start")
print(results)

print("Outlook End")

# Temperature attribute
# Hot
hot_yes = 2
hot_no = 2
hot_entropy = entropy(hot_yes, hot_no)

# Mild
mild_yes = 4
mild_no = 2
mild_entropy = entropy(mild_yes, mild_no)

# Cool
cool_yes = 3
cool_no = 1
cool_entropy = entropy(cool_yes, cool_no)

# Weighted entropy for Temp
weighted_entropy_temp = (4 / 14) * hot_entropy + (6 / 14) * mild_entropy + (4 / 14) * cool_entropy
print("Cold fraction", (4 / 14) * cool_entropy)
print("Hot fraction",  (4 / 14) * hot_entropy)
print("Mild fraction",  (6 / 14) * mild_entropy)
print("weighted_entropy_temp",weighted_entropy_temp)
# Information Gain for Temp
information_gain_temp = total_entropy - weighted_entropy_temp
print("Information Gain (Temp)", information_gain_temp)


# Store Temp results in the dictionary
results.update({
    "Hot Entropy": hot_entropy,
    "Mild Entropy": mild_entropy,
    "Cool Entropy": cool_entropy,
    "Weighted Entropy (Temp)": weighted_entropy_temp,
    "Information Gain (Temp)": information_gain_temp
})

print(results)

# Humidity attribute
# High
high_yes = 3
high_no = 4
high_entropy = entropy(high_yes, high_no)

# Normal
normal_yes = 6
normal_no = 1
normal_entropy = entropy(normal_yes, normal_no)

# Weighted entropy for Humidity
weighted_entropy_humidity = (7 / 14) * high_entropy + (7 / 14) * normal_entropy

# Information Gain for Humidity
information_gain_humidity = total_entropy - weighted_entropy_humidity
print("Information Gain (Humidity)", information_gain_humidity)

# Store Humidity results in the dictionary
results.update({
    "High Entropy": high_entropy,
    "Normal Entropy": normal_entropy,
    "Weighted Entropy (Humidity)": weighted_entropy_humidity,
    "Information Gain (Humidity)": information_gain_humidity
})

print(results)

# Wind attribute
# Weak
weak_yes = 6
weak_no = 2
weak_entropy = entropy(weak_yes, weak_no)

# Strong
strong_yes = 3
strong_no = 3
strong_entropy = entropy(strong_yes, strong_no)

# Weighted entropy for Wind
weighted_entropy_wind = (8 / 14) * weak_entropy + (6 / 14) * strong_entropy

# Information Gain for Wind
information_gain_wind = total_entropy - weighted_entropy_wind

print("Information Gain (Wind)", information_gain_wind)

# Store Wind results in the dictionary
results.update({
    "Weak Entropy": weak_entropy,
    "Strong Entropy": strong_entropy,
    "Weighted Entropy (Wind)": weighted_entropy_wind,
    "Information Gain (Wind)": information_gain_wind
})

print(results)

# Subset for Outlook = Sunny
sunny_yes = 2
sunny_no = 3
sunny_entropy = entropy(sunny_yes, sunny_no)

# Sunny subset counts for Temp, Humidity, and Wind
# Temp
sunny_hot_yes = 0
sunny_hot_no = 2
sunny_hot_entropy = entropy(sunny_hot_yes, sunny_hot_no)

sunny_mild_yes = 1
sunny_mild_no = 1
sunny_mild_entropy = entropy(sunny_mild_yes, sunny_mild_no)

sunny_cool_yes = 1
sunny_cool_no = 0
sunny_cool_entropy = entropy(sunny_cool_yes, sunny_cool_no)

# Weighted entropy for Temp within Sunny subset
weighted_entropy_sunny_temp = (2 / 5) * sunny_hot_entropy + (2 / 5) * sunny_mild_entropy + (1 / 5) * sunny_cool_entropy

# Information Gain for Temp within Sunny subset
information_gain_sunny_temp = sunny_entropy - weighted_entropy_sunny_temp

# Humidity
sunny_high_yes = 0
sunny_high_no = 3
sunny_high_entropy = entropy(sunny_high_yes, sunny_high_no)

sunny_normal_yes = 2
sunny_normal_no = 0
sunny_normal_entropy = entropy(sunny_normal_yes, sunny_normal_no)

# Weighted entropy for Humidity within Sunny subset
weighted_entropy_sunny_humidity = (3 / 5) * sunny_high_entropy + (2 / 5) * sunny_normal_entropy

# Information Gain for Humidity within Sunny subset
information_gain_sunny_humidity = sunny_entropy - weighted_entropy_sunny_humidity

# Wind
sunny_weak_yes = 1
sunny_weak_no = 2
sunny_weak_entropy = entropy(sunny_weak_yes, sunny_weak_no)

sunny_strong_yes = 1
sunny_strong_no = 1
sunny_strong_entropy = entropy(sunny_strong_yes, sunny_strong_no)

# Weighted entropy for Wind within Sunny subset
weighted_entropy_sunny_wind = (3 / 5) * sunny_weak_entropy + (2 / 5) * sunny_strong_entropy

# Information Gain for Wind within Sunny subset
information_gain_sunny_wind = sunny_entropy - weighted_entropy_sunny_wind

# Store Sunny subset results in the dictionary
sunny_subset_results = {
    "Sunny Subset Entropy": sunny_entropy,
    "Sunny Hot Entropy": sunny_hot_entropy,
    "Sunny Mild Entropy": sunny_mild_entropy,
    "Sunny Cool Entropy": sunny_cool_entropy,
    "Weighted Entropy (Sunny Temp)": weighted_entropy_sunny_temp,
    "Information Gain (Sunny Temp)": information_gain_sunny_temp,
    "Sunny High Entropy": sunny_high_entropy,
    "Sunny Normal Entropy": sunny_normal_entropy,
    "Weighted Entropy (Sunny Humidity)": weighted_entropy_sunny_humidity,
    "Information Gain (Sunny Humidity)": information_gain_sunny_humidity,
    "Sunny Weak Entropy": sunny_weak_entropy,
    "Sunny Strong Entropy": sunny_strong_entropy,
    "Weighted Entropy (Sunny Wind)": weighted_entropy_sunny_wind,
    "Information Gain (Sunny Wind)": information_gain_sunny_wind
}

print(sunny_subset_results)

# Subset for Outlook = Rain
rain_yes = 3
rain_no = 2
rain_entropy = entropy(rain_yes, rain_no)

# Rain subset counts for Temp, Humidity, and Wind
# Temp
rain_mild_yes = 2
rain_mild_no = 1
rain_mild_entropy = entropy(rain_mild_yes, rain_mild_no)

rain_cool_yes = 1
rain_cool_no = 1
rain_cool_entropy = entropy(rain_cool_yes, rain_cool_no)

# Weighted entropy for Temp within Rain subset
weighted_entropy_rain_temp = (3 / 5) * rain_mild_entropy + (2 / 5) * rain_cool_entropy

# Information Gain for Temp within Rain subset
information_gain_rain_temp = rain_entropy - weighted_entropy_rain_temp

# Humidity
rain_high_yes = 1
rain_high_no = 1
rain_high_entropy = entropy(rain_high_yes, rain_high_no)

rain_normal_yes = 2
rain_normal_no = 1
rain_normal_entropy = entropy(rain_normal_yes, rain_normal_no)

# Weighted entropy for Humidity within Rain subset
weighted_entropy_rain_humidity = (2 / 5) * rain_high_entropy + (3 / 5) * rain_normal_entropy

# Information Gain for Humidity within Rain subset
information_gain_rain_humidity = rain_entropy - weighted_entropy_rain_humidity

# Wind
rain_weak_yes = 2
rain_weak_no = 0
rain_weak_entropy = entropy(rain_weak_yes, rain_weak_no)

rain_strong_yes = 1
rain_strong_no = 2
rain_strong_entropy = entropy(rain_strong_yes, rain_strong_no)

# Weighted entropy for Wind within Rain subset
weighted_entropy_rain_wind = (3 / 5) * rain_weak_entropy + (2 / 5) * rain_strong_entropy

# Information Gain for Wind within Rain subset
information_gain_rain_wind = rain_entropy - weighted_entropy_rain_wind

# Store Rain subset results in the dictionary
rain_subset_results = {
    "Rain Subset Entropy": rain_entropy,
    "Rain Mild Entropy": rain_mild_entropy,
    "Rain Cool Entropy": rain_cool_entropy,
    "Weighted Entropy (Rain Temp)": weighted_entropy_rain_temp,
    "Information Gain (Rain Temp)": information_gain_rain_temp,
    "Rain High Entropy": rain_high_entropy,
    "Rain Normal Entropy": rain_normal_entropy,
    "Weighted Entropy (Rain Humidity)": weighted_entropy_rain_humidity,
    "Information Gain (Rain Humidity)": information_gain_rain_humidity,
    "Rain Weak Entropy": rain_weak_entropy,
    "Rain Strong Entropy": rain_strong_entropy,
    "Weighted Entropy (Rain Wind)": weighted_entropy_rain_wind,
    "Information Gain (Rain Wind)": information_gain_rain_wind
}

print(rain_subset_results)
