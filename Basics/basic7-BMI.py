years_str = input("Years: ") # do not change this line

# Missing lines here
population = 307357870
years_int = int(years_str)
year_secs = years_int * 31556926
birth = 31556926 / 7
death = 31556926 / 13
immigrants = 31556926 / 35
new_population = years_int * (birth - death + immigrants) + population

print("New population after", years_int, " years is ", int(new_population)) # do not change this line

