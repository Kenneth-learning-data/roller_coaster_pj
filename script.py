import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood_df= pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
print(wood_df.head(30))

steel_df= pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(steel_df.head(30))
#x_axis
year_of_rank= wood_df['Year of Rank']


# write function to plot rankings over time for 1 roller coaster here:
def single_rank(name, matertial, park_name):
  if matertial=='wood':
    select_all_roaster_data= wood_df[(wood_df.Name ==name)&(wood_df.Park ==park_name)]
  if matertial=='steel':
   select_all_roaster_data= steel_df[(steel_df.Name ==name)&(steel_df.Park ==park_name)]
  
  x_values= select_all_roaster_data['Year of Rank']
  y_values= select_all_roaster_data['Rank']

  
  plt.figure(figsize=(8, 10))
  plt.plot(range(len(x_values)), y_values)
  ax= plt.subplot()
  ax.set_xticks(range(len(x_values)))
  ax.set_xticklabels(x_values)
  ax.invert_yaxis()
  plt.title(name +" roller coaster ranking over 2013 and 2018")
  plt.xlabel("Year of Rank")
  plt.ylabel("Rank")
  plt.show()

single_rank("El Toro", "wood", "Six Flags Great Adventure")

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def two_rank(name_1, matertial_1, park_name_1, name_2, matertial_2, park_name_2):
  if matertial_1=='wood':
    select_all_roaster_data_1= wood_df[(wood_df.Name ==name_1)&(wood_df.Park ==park_name_1)]
  if matertial_1=='steel':
    select_all_roaster_data_1= steel_df[(steel_df.Name ==name_1)&(steel_df.Park ==park_name_1)]  
  if matertial_2=='wood':
    select_all_roaster_data_2= wood_df[(wood_df.Name ==name_2)&(wood_df.Park ==park_name_2)]
  if matertial_2=='steel':
    select_all_roaster_data_2= steel_df[(steel_df.Name ==name_2)&(steel_df.Park ==park_name_2)] 
  x_values_1= select_all_roaster_data_1['Year of Rank']
  y_values_1= select_all_roaster_data_1['Rank']
  plt.figure(figsize=(8, 10))
  plt.plot(range(len(x_values_1)), y_values_1)
  ax= plt.subplot()
  ax.set_xticks(range(len(x_values_1)))
  ax.set_xticklabels(x_values_1)
  ax.invert_yaxis()
  plt.xlabel("Year of Rank")
  plt.ylabel("Rank")
  #2 plot
  x_values_2= select_all_roaster_data_2['Year of Rank']
  y_values_2= select_all_roaster_data_2['Rank']
  plt.plot(range(len(x_values_2)), y_values_2)
  plt.title(name_1 +""+ name_2+" roller coaster ranking over 2013 and 2018")
  plt.show()

two_rank("El Toro", "wood", "Six Flags Great Adventure", "Goliath", "steel", "Six Flags Over Georgia")
plt.clf()

# write function to plot top n rankings over time here:
def top_n(n, matertial):
  if matertial =='wood':
    select_all_roaster_data= wood_df[wood_df.Rank <= n]
    print(select_all_roaster_data.head(20))
  if matertial =='steel':
    select_all_roaster_data= steel_df[steel_df.Rank <= n]
  plt.figure(figsize=(8, 10))
  ax= plt.subplot()
  x_values= select_all_roaster_data['Year of Rank']
  y_values= select_all_roaster_data['Rank']
  for coaster in set(select_all_roaster_data['Name']):
    coaster_rankings = select_all_roaster_data[select_all_roaster_data["Name"]== coaster]
    ax.plot(coaster_rankings["Year of Rank"], coaster_rankings["Rank"], label =coaster)
  plt.title('Top '+ str(n)+ "rank roller coasters over 2013 and 2018")
  plt.xlabel("Year of Rank")
  plt.ylabel("Rank")
  plt.show()

top_n(5, "wood")







plt.clf()

# load roller coaster data here:
captain_coaster_df=pd.read_csv("roller_coasters.csv")
print(captain_coaster_df)

#7 write function to plot histogram of column values here:
def numeric_column_hist(df, column):
  df= df.dropna()
  plt.hist(df[column], bins=30, alpha=0.5)
  plt.ylabel(column)
  plt.title(column +" of roller coasters")
  plt.show()

numeric_column_hist(captain_coaster_df, "speed")
numeric_column_hist(captain_coaster_df, "height")
numeric_column_hist(captain_coaster_df, "length")
plt.clf()

#8 write function to plot inversions by coaster at a park here:
def num_of_inversions(df, park_name):
  select_row= df[df['name']== park_name]
  
  plt.bar(select_row['name'],select_row["num_inversions"])
  plt.show()
num_of_inversions(captain_coaster_df, "	Parc Asterix")

plt.clf()
