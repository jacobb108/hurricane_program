# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def damages_converter(damages_list):
  damages_conv = []
  for i in range(len(damages_list)):
    if damages_list[i] == "Damages not recorded":
      damages_conv.append(damages_list[i])
    elif "M" in damages[i]:
      trim_dam = damages[i].strip("M")
      trim_dam = float(trim_dam)
      trim_dam = trim_dam * 1000000
      damages_conv.append(round(trim_dam))
    elif "B" in damages[i]:
      trim_dam = damages[i].strip("B")
      trim_dam = float(trim_dam)
      trim_dam = trim_dam * 1000000000
      damages_conv.append(round(trim_dam))
  return damages_conv

updated_damages = damages_converter(damages)
#print(updated_damages)

# write your construct hurricane dictionary function here:

def hurr_dict_name(names, months, years, winds, areas, damages, deaths):
  hurr_dict_name = {}
  for i in range(len(names)):
    hurr_dict_name[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": winds[i], "Areas Affected": areas[i], "Damage": damages[i], "Deaths": deaths[i]}
  return hurr_dict_name

hurr_dict_by_name = hurr_dict_name(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurr_dict_by_name)

# write your construct hurricane by year dictionary function here:

# must put current_cane in brackets in line 63 to initialize as appendable list of dictionaries

def hurr_dict_year(hurr_dict):
  hurr_dict_year = {}
  for hurricane in hurr_dict:
    current_year = hurr_dict[hurricane]["Year"]
    current_cane = hurr_dict[hurricane]
    if current_year not in hurr_dict_year:
      hurr_dict_year[current_year] = [current_cane]
    else:
      hurr_dict_year[current_year].append(current_cane)
  return hurr_dict_year

hurr_dict_by_year = hurr_dict_year(hurr_dict_by_name)
#print(hurr_dict_by_year)

# write your count affected areas function here:

# first create list of unique areas for iteration through the area_counter function

area_list = []
for region in areas_affected:
  for area in region:
    if area not in area_list:
      area_list.append(area)

def area_counter(hurr_dict, area_list):
  area_count_dict = {}  
  for area in area_list:
    count = 0
    for hurricane in hurr_dict:
      if area in hurr_dict[hurricane]["Areas Affected"]:
        count += 1
    area_count_dict[area] = count
  return area_count_dict

area_count = area_counter(hurr_dict_by_name, area_list)
#print(area_count)

# write your find most affected area function here:

# in most_affected_finder function, convert count dictionary into list to sort, then convert sorted list back into dictionary

def most_affected_finder(area_dict):
  count_dict = {}
  for area in area_dict:
    count = area_dict[area]
    if count not in count_dict:
      count_dict[count] = [area]
    else:
      count_dict[count].append(area)
  sorted_counts = sorted(count_dict.items(),reverse=True)
  sorted_count_dict = {count:areas for (count, areas) in sorted_counts}
  return sorted_count_dict

count_count = most_affected_finder(area_count)
#print(count_count)

# write your greatest number of deaths function here:

def max_death_finder(hurr_dict):
  max_death = 0
  max_death_hurricane = ""
  for hurricane in hurr_dict:
    deaths = hurr_dict[hurricane]["Deaths"]
    cane = hurr_dict[hurricane]
    if max_death < deaths:
      max_death = deaths
      max_death_hurricane = cane
  return max_death_hurricane

deadliest_cane = (max_death_finder(hurr_dict_by_name))
#print(deadliest_cane)

# write your function to categorize hurricanes by mortality here:

def mort_scaler(hurr_dict):
  mort_dict = {1: [], 2: [], 3: [], 4: [], 5: []}
  for hurricane in hurr_dict:
    current_cane = hurr_dict[hurricane]
    current_mort = hurr_dict[hurricane]["Deaths"]
    if current_mort > 10000:
      mort_dict[5].append(current_cane)
    elif current_mort > 1000:
      mort_dict[4].append(current_cane)
    elif current_mort > 500:
      mort_dict[3].append(current_cane)
    elif current_mort > 100:
      mort_dict[2].append(current_cane)
    elif current_mort > 0:
      mort_dict[1].append(current_cane)
  return mort_dict

mort_list = mort_scaler(hurr_dict_by_name)
#print(mort_list)

# write your greatest damage function here:

def max_damage_finder(hurr_dict):
  max_damage = 0
  max_damage_hurricane = ""
  for hurricane in hurr_dict:
    damage = hurr_dict[hurricane]["Damage"]
    current_cane = hurr_dict[hurricane]
    if damage != "Damages not recorded":
      if max_damage < damage:
        max_damage = damage
        max_death_hurricane = current_cane
  return max_death_hurricane

costliest_cane = max_damage_finder(hurr_dict_by_name)
#print(costliest_cane)

# write your function to categorize hurricanes by damages here:

def damages_scaler(hurr_dict):
  damages_dict = {1: [], 2: [], 3: [], 4: [], 5: []}
  for hurricane in hurr_dict:
    current_cane = hurr_dict[hurricane]
    current_damages = hurr_dict[hurricane]["Damage"]
    if current_damages != "Damages not recorded":
      if current_damages > 50000000000:
        damages_dict[5].append(current_cane)
      elif current_damages > 10000000000:
        damages_dict[4].append(current_cane)
      elif current_damages > 1000000000:
        damages_dict[3].append(current_cane)
      elif current_damages > 100000000:
        damages_dict[2].append(current_cane)
      elif current_damages > 0:
        damages_dict[1].append(current_cane)
  return damages_dict

damages_list = damages_scaler(hurr_dict_by_name)
#print(damages_list)
