import matplotlib.pyplot as plt  # Import the pyplot module

subjects = ['bangla', 'english', 'physics', 'cse', 'eee', 'archi','hum']
myMarks = [80,70,60,65,90,80,77]
myFriendsMarks = [72,80,80,70,85,70,80]

plt.plot(subjects,myMarks,label='my marks',marker='o',markerfacecolor='red',markersize=8,linestyle='dashdot')
plt.plot(subjects,myFriendsMarks,label='my friends marks',marker='o',markerfacecolor='yellow',markersize=8,linestyle='dashdot')
plt.xlabel('subjects')
plt.ylabel('marks')
plt.title('marks comparison')
plt.legend()

plt.show()


# plt.show()
