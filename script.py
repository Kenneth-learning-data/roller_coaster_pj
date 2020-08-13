import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood= pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel= pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(wood.head())
print(steel.head())


# write function to plot rankings over time for 1 roller coaster here:
def roller_rank(name, ranking_DataFrame, park_name):
  if ranking_DataFrame == 'wood':
    wood_roller= wood[(wood.Name == name) & 
                      (wood.Park == park_name)]
    wood_Rank = wood_roller['Rank'].tolist()
    wood_Year_of_Rank= wood_roller['Year of Rank'].tolist()
    plt.plot(wood_Year_of_Rank, wood_Rank)
    plt.title('Roller coaster ranking between 2013 and 2018')
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.show()
  else:
    steel_roller= steel[(steel.Name == name)& 
                      (steel.Park == park_name)]
    steel_Rank = steel_roller['Rank'].tolist()
    steel_Year_of_Rank= steel_roller['Year of Rank'].tolist()
    plt.plot(steel_Year_of_Rank, steel_Rank)
    plt.title('Roller coaster ranking between 2013 and 2018')
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.show()
  
roller_rank("El Toro", "wood", "Six Flags Great Adventure")
roller_rank("Bizarro", "steel", "Six Flags Great Adventure")

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:










plt.clf()

# write function to plot top n rankings over time here:










plt.clf()

# load roller coaster data here:



# write function to plot histogram of column values here:










plt.clf()

# write function to plot inversions by coaster at a park here:










plt.clf()
    
# write function to plot pie chart of operating status here:










plt.clf()
  
# write function to create scatter plot of any two numeric columns here:










plt.clf()