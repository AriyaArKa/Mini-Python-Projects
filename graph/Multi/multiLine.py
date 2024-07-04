import matplotlib.pyplot as plt  # Import the pyplot module

subjects = ['Buuble', 'Insertion', 'Quick', 'Selection', 'Merge', 'Heap','Radix','Counting','Bucket']
# myMarks = [5181,1502,152,2795,673,314,215,159,998]
myFriendsMarks = [5181,1502,152,2795,673,314,215,159,998]

# plt.plot(subjects,myMarks,label='my marks',marker='o',markerfacecolor='red',markersize=8,linestyle='dashdot')
plt.plot(subjects,myFriendsMarks,label='my friends marks',marker='o',markerfacecolor='yellow',markersize=8,linestyle='dashdot')
plt.xlabel('Sortings')
plt.ylabel('Time taken in microseconds')
plt.title('Time taken when size is 1000')
plt.legend()

plt.show()


# plt.show()
