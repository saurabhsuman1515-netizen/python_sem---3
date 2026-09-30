import matplotlib.pyplot as plt
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
province_population = [12344408, 2441523, 30523371, 110012442, 47886051]
activities = ['Balochistan', 'Gilgit-Baltistan', 'Khyber Pakhtunkhwa', 'Punjab', 'Sindh']
plt.pie(province_population, labels=activities, startangle=90, autopct='%.1f%%',colors =colors)
plt.title('Pakistan Population Province Wise')
plt.show()




import matplotlib.pyplot as plt

# Data to plot
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [45, 30, 15, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
# "Explode" the 1st slice (Python) out by 0.1
explode = (0.1, 0, 0, 0)  
# Create the pie chart
plt.figure(figsize=(6, 6))
plt.pie(
    sizes, 
    explode=explode, 
    labels=labels, 
    colors=colors, 
    autopct='%1.1f%%',  # Format to show percentages
    shadow=True,        # Add a drop shadow
    startangle=140      # Rotate the start position
)
# Ensure the pie chart is drawn as a circle
plt.axis('equal')  
# Add a title and display
plt.title("Programming Language Popularity")
plt.show()
