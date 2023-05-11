import tkinter as tk
# opens new window once button is clicked
def open_new_window():
	# closes original window
	root.withdraw()
	# creates new window and sets size
	new_window = tk.Toplevel()
	new_window.geometry("400x700")
	# creates all titles for each input
	input1_label = tk.Label(new_window, text="Height(in):")
	input1_label.place(x=100, y=40)
	input2_label = tk.Label(new_window, text="Weight(lbs):")
	input2_label.place(x=100, y=100)
	input3_label = tk.Label(new_window, text="Age:")
	input3_label.place(x=100, y=160)
	input4_label = tk.Label(new_window, text="Sex:")
	input4_label.place(x=100, y=220)
	input5_label = tk.Label(new_window, text="Goal(gain/lose/maintain):")
	input5_label.place(x=100, y=280)
	input6_label = tk.Label(new_window, text="Weight loss/gain per week(0, 0.5, 1, 1.5, 2):")
	input6_label.place(x=100, y=340)
	input7_label = tk.Label(new_window, text="How many calories do you burn exercising?")
	input7_label.place(x=100, y=400)
	input8_label = tk.Label(new_window, text="Whats your body type(endo, meso, ecto):")
	input8_label.place(x=100, y=460)

	# Create the box to input text
	# .place() sets location, and .insert sets default values
	height = (tk.Entry(new_window))
	height.place(x=100, y=60)
	height.insert(64, 64)
	weight = (tk.Entry(new_window))
	weight.place(x=100, y=120)
	weight.insert(150, 150)
	age = (tk.Entry(new_window))
	age.place(x=100, y=180)
	age.insert(18, 18)
	sex = tk.Entry(new_window)
	sex.place(x=100, y=240)
	goal = tk.Entry(new_window)
	goal.place(x=100, y=300)
	goal.insert(0,"maintain")
	w_change = (tk.Entry(new_window))
	w_change.place(x=100, y=360)
	w_change.insert(0,0)
	do_ex = tk.Entry(new_window)
	do_ex.place(x=100, y=420)
	do_ex.insert(0, 0)
	body = (tk.Entry(new_window))
	body.place(x=100, y=480)

	# this function is called when calculate is pressed
	# this functions have the formulas for determining the calories and macros
	def calculate():
		info_arr = list()
		w = int(weight.get()) / 2.205
		h = int(height.get()) * 2.54
		a = int(age.get())
		s = sex.get().lower()
		g = goal.get().lower()
		b = body.get().lower()
		ex = int(do_ex.get())
		wl = float(w_change.get())

		k_cal = int(Harris(w, h, a, s))
		k_cal += ex

		if g == "gain":
			k_cal += wl * 500
			info_arr = Mass_Gain(b, k_cal)
		elif g == "lose":
			k_cal += wl * 500
			info_arr = Lose_Fat(b, k_cal)
		else:
			info_arr = Maintain(b, k_cal)
		#changes the text in results
		result_label.config(
			text=f"Calories: {k_cal}\nProtein: {info_arr[1]}g\nCarbs: {info_arr[0]}g\nFat: {info_arr[2]}g",
			bg="lightblue")

	# button to calculate
	the_button = tk.Button(new_window, text="Calculate", command=calculate, fg="blue")
	the_button.place(x=150, y=550)

	# Where results are displayed
	result_label = tk.Label(new_window, text="")
	result_label.place(x=150, y=600)


	#formulas
	def percent_of_kcal(percent, total_kcal):
		kcal_percent = percent * total_kcal
		return kcal_percent

	# formula for the amount of daily calories you require based on Harris-Benedicts equation
	def Harris(weight, height, age, gender):
		calories = 0
		if gender == "m":
			calories += 66.4730 + (13.7516 * weight) + (5.0033 * height) - (6.7550 * age)
		elif gender == "f":
			calories += 655.0955 + (9.5634 * weight) + (1.8496 * height) - (4.6756 * age)
		return calories

	# formulas for macronutrients specified by goals
	def Mass_Gain(body_type, daily_kcal):
		if body_type == "ecto":
			carb_intake = 0.25 * percent_of_kcal(0.60, daily_kcal)
			protein_intake = 0.25 * percent_of_kcal(0.25, daily_kcal)
			fat_intake = (1 / 9) * percent_of_kcal(0.15, daily_kcal)
		elif body_type == "meso":
			carb_intake = 0.25 * percent_of_kcal(0.50, daily_kcal)
			protein_intake = 0.25 * percent_of_kcal(0.30, daily_kcal)
			fat_intake = (1 / 9) * percent_of_kcal(0.20, daily_kcal)
		elif body_type == "endo":
			carb_intake = 0.25 * percent_of_kcal(0.40, daily_kcal)
			protein_intake = 0.25 * percent_of_kcal(0.35, daily_kcal)
			fat_intake = (1 / 9) * percent_of_kcal(0.25, daily_kcal)
		return [round(carb_intake), round(protein_intake), round(fat_intake)]

	def Maintain(body_type, daily_kcal):
		if body_type == "ecto":
			carb_intake = 0.25 * percent_of_kcal(0.50, daily_kcal)
			protein_intake = 0.25 * percent_of_kcal(0.25, daily_kcal)
			fat_intake = (1 / 9) * percent_of_kcal(0.25, daily_kcal)
		elif body_type == "meso":
			carb_intake = 0.25 * percent_of_kcal(0.40, daily_kcal)
			protein_intake = 0.25 * percent_of_kcal(0.30, daily_kcal)
			fat_intake = (1 / 9) * percent_of_kcal(0.30, daily_kcal)
		elif body_type == "endo":
			carb_intake = 0.25 * percent_of_kcal(0.30, daily_kcal)
			protein_intake = 0.25 * percent_of_kcal(0.35, daily_kcal)
			fat_intake = (1 / 9) * percent_of_kcal(0.35, daily_kcal)
		return [round(carb_intake), round(protein_intake), round(fat_intake)]

	def Lose_Fat(body_type, daily_kcal):
		if body_type == "ecto":
			carb_intake = 0.25 * percent_of_kcal(0.30, daily_kcal)
			protein_intake = 0.25 * percent_of_kcal(0.40, daily_kcal)
			fat_intake = (1 / 9) * percent_of_kcal(0.30, daily_kcal)
		elif body_type == "meso":
			carb_intake = 0.25 * percent_of_kcal(0.20, daily_kcal)
			protein_intake = 0.25 * percent_of_kcal(0.45, daily_kcal)
			fat_intake = (1 / 9) * percent_of_kcal(0.35, daily_kcal)
		elif body_type == "endo":
			carb_intake = 0.25 * percent_of_kcal(0.10, daily_kcal)
			protein_intake = 0.25 * percent_of_kcal(0.50, daily_kcal)
			fat_intake = (1 / 9) * percent_of_kcal(0.40, daily_kcal)
		return [round(carb_intake), round(protein_intake), round(fat_intake)]

# the code for welcome page
root = tk.Tk()
root.geometry("400x100")
info_label = tk.Label(root, text="Welcome!!!\n This calculator will use data about your body to determine how\n many calories you should consume and which macronutrients\n you should consume for your fitness goal. ")
info_label.pack()
# Create a button that opens the new window when clicked
button_1 = tk.Button(root, text="Next", command=open_new_window)
button_1.pack()

root.mainloop()
