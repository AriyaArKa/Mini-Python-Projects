import matplotlib.pyplot as plt  # Import the pyplot module

days = ['Buuble', 'Insertion', 'Quick', 'Selection', 'Merge', 'Heap','Radix','Counting','Bucket']

# The 'numbers' list has one extra element compared to 'days', 'satur' should be removed or another day should be added
numbers = [626113,160694,1673,501094,5059,3912,2195,741,2992]

plt.plot(days, numbers,color='orange',linewidth=5,marker='o',markerfacecolor='blue',markersize=12,linestyle='dashdot')

plt.xlabel('Sortings')
plt.ylabel('Time taken in microseconds')
plt.title('Time taken when size is 10000')
plt.show()

# import matplotlib.pyplot as plt
#
# # Sample data
# array_sizes = [1000, 5000, 10000]
# bubble_sort_times = [5181, 149490, 626113]
# insertion_sort_times = [1502, 45341, 160694]
# Quick_sort_times = [152, 882, 1673]
# Selection_sort_times = [2795, 161643, 501094]
# merge_sort_times = [673, 3117, 5059]
# Heap_sort_times = [314, 1863, 3912]
# Radix_sort_times = [215, 1078, 2195]
# Counting_sort_times = [159, 447, 741]
# Bucket_sort_times = [998, 1995, 2992]
#
# # Plotting
# plt.plot(array_sizes, bubble_sort_times, label='Bubble Sort')
# plt.plot(array_sizes, insertion_sort_times, label='Insertion Sort')
# plt.plot(array_sizes, Quick_sort_times, label='Quick Sort')
# plt.plot(array_sizes, Selection_sort_times, label='Selection Sort')
# plt.plot(array_sizes, merge_sort_times, label='Merge Sort')
# plt.plot(array_sizes, Heap_sort_times, label='Heap Sort')
# plt.plot(array_sizes, Radix_sort_times, label='Radix Sort')
# plt.plot(array_sizes, Counting_sort_times, label='Counting Sort')
# plt.plot(array_sizes, Bucket_sort_times, label='Bucket Sort')
#
#
# # Labeling and customization
# plt.xlabel('Array Size')
# plt.ylabel('Time Taken (micros)')
# plt.title('Sorting Algorithm Performance')
# plt.legend()
#
# # Set logarithmic scale for y-axis
# plt.yscale('log')
#
# # Show plot
# plt.show()

