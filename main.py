import pandas as pd

#imported our data set
data = pd.read_excel("pop_data.xlsx")

#removed unnecessary columns
del data["density"]
del data["area"]
del data["land area"]
del data["Unnamed: 7"]

#list to store the changes in population
pop_change = list()
pop_change_percent = list()

#compare 2022 population with 2023 population
for i in range(0,205):
    pop_23 = (data["current population"][i])
    pop_22 = (data["population 2022"][i])
    pop_growth = int(pop_23.replace(',', '')) - int(pop_22.replace(',', ''))
    pop_change.append(pop_growth)

names = list(data["country name"])

new_data = pd.DataFrame({"Country Names" : names, "Population Change" : pop_change}, columns=["Country Names", "Population Change"])
new_data = new_data.sort_values(["Population Change", "Country Names"], ascending=[False, True])
new_data.to_csv("New_Data.csv")


