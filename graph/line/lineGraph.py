import matplotlib.pyplot as plt  # Import the pyplot module

days = ['sun', 'mon', 'tues', 'thrus', 'fri', 'satur']

# The 'numbers' list has one extra element compared to 'days', 'satur' should be removed or another day should be added
numbers = [25, 15, 20, 15, 18, 30]

plt.plot(days, numbers,color='orange',linewidth=5,marker='o',markerfacecolor='blue',markersize=12,linestyle='dashdot')

plt.xlabel('Days')
plt.ylabel('number of push ups')
plt.title('my push up graph')
plt.show()
