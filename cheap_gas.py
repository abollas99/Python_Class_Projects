import tkinter as tk
import http.client
import json

# Set size and titling the GUI
root = tk.Tk()
root.geometry("400x600")
root.title("Cheapest Gas Stations in US States")

# Connecting to CollectAPI for Gas Price Data
def get_gas_data(state):
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': "apikey 7eAuO4Dbo8jWrLqVlzzqjh:7jI2x3ZdwoA7F2YSbMQIAq"
    }

    conn.request("GET", f"/gasPrice/stateUsaPrice?state={state}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data)

    # Organizing the data and putting it into a dictionary, to then sort by cheapest
    gas_data = {}
    for x in range(len(json_data["result"]["cities"])):
        city_name = json_data["result"]["cities"][x]["name"]
        gas_price = float(json_data["result"]["cities"][x]["gasoline"])
        mid_gas_price = float(json_data["result"]["cities"][x]["midGrade"])
        prem_gas_price = float(json_data["result"]["cities"][x]["premium"])
        diesel_price = float(json_data["result"]["cities"][x]["diesel"])
        city_data = { "Regular": gas_price, "Super": mid_gas_price, "Premium": prem_gas_price, "Diesel": diesel_price }
        gas_data[city_name] = city_data    
    gas_data = dict(sorted(gas_data.items(), key=lambda x: x[1]["Regular"]))
    
    return gas_data

def searchForGas():
    # Get state from input field
    state = state_input.get()
    
    # Get gas data for state
    gas_data = get_gas_data(state)
    
    # Display gas data in text widget
    gas_data_str = json.dumps(gas_data, indent=4)

    gas_text.config(state=tk.NORMAL)
    gas_text.delete("1.0", tk.END)
    gas_text.insert(tk.END, gas_data_str)
    gas_text.config(state=tk.DISABLED)

# Create input field for state
state_frame = tk.Frame(root)
state_frame.pack(side=tk.TOP)
state_label = tk.Label(state_frame, text="State code:")
state_label.pack(side=tk.LEFT)
state_input = tk.Entry(state_frame)
state_input.pack(side=tk.LEFT)

# Allows you to scroll through results
gas_frame = tk.Frame(root)
gas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
label = tk.Label(gas_frame, text="The cheapest gas stations in the selected state:")
label.pack(side=tk.TOP)
scrollbar = tk.Scrollbar(gas_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
gas_text = tk.Text(gas_frame, yscrollcommand=scrollbar.set)
gas_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
scrollbar.config(command=gas_text.yview)

# Create "Search" button
button = tk.Button(root, text="Search", command=searchForGas)
button.pack()

root.mainloop()
