import tkinter as tk
from tkinter import ttk
import random
import time
from tkinter import messagebox

data = []

# Sorting algorithms (No changes needed here)

def bubble_sort(data, drawData):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['#FFC13F' if x == j or x == j+1 else '#00BFFF' for x in range(len(data))])
                time.sleep(1.0)
    drawData(data, ['#00BFFF' for x in range(len(data))])

def insertion_sort(data, drawData):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        drawData(data, ['#FFC13F' if x == j or x == j+1 else '#00BFFF' for x in range(len(data))])
        time.sleep(1.0)
    drawData(data, ['#00BFFF' for x in range(len(data))])

def selection_sort(data, drawData):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        drawData(data, ['#FFC13F' if x == i or x == min_idx else '#00BFFF' for x in range(len(data))])
        time.sleep(1.0)
    drawData(data, ['#00BFFF' for x in range(len(data))])

# Quick sort algorithm
def quick_sort(data, drawData, low, high):
    if low < high:
        pi = partition(data, low, high)
        drawData(data, ['#FFC13F' if x == pi else '#00BFFF' for x in range(len(data))])
        time.sleep(1.0)
        quick_sort(data, drawData, low, pi-1)
        quick_sort(data, drawData, pi+1, high)
    drawData(data, ['#00BFFF' for x in range(len(data))])

# Heapify function for heap sort
def heapify(data, n, i, drawData):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If left child is larger than root
    if left < n and data[left] > data[largest]:
        largest = left

    # If right child is larger than the largest so far
    if right < n and data[right] > data[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        drawData(data, ['#FFC13F' if x == i or x == largest else '#00BFFF' for x in range(len(data))])  # Highlight the swapped elements
        time.sleep(1.0)
        heapify(data, n, largest, drawData)  # Recursively heapify the affected sub-tree

# Heap sort function
def heap_sort(data, drawData):
    n = len(data)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawData)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # Swap the root (largest element) with the last element
        drawData(data, ['#FFC13F' if x == i or x == 0 else '#00BFFF' for x in range(len(data))])  # Highlight the swapped elements
        time.sleep(1.0)
        heapify(data, i, 0, drawData)  # Heapify the root again

    drawData(data, ['#00BFFF' for x in range(len(data))])  # Final draw to show the sorted array

def partition(data, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

# Sorting visualizer (no changes)

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(data[i]), fill="white")
    root.update_idletasks()

# Generate new random data
def generate():
    global data
    data = [random.randint(1, 100) for _ in range(15)]
    drawData(data, ['#00BFFF' for x in range(len(data))])

# Start selected algorithm
def startAlgorithm():
    global data
    if not data: return
    if algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData)
    elif algMenu.get() == 'Insertion Sort':
        insertion_sort(data, drawData)
    elif algMenu.get() == 'Selection Sort':
        selection_sort(data, drawData)
    elif algMenu.get() == 'Quick Sort':
        quick_sort(data, drawData, 0, len(data)-1)
    elif algMenu.get() == 'Heap Sort':
         heap_sort(data, drawData)
    drawData(data, ['#00BFFF' for x in range(len(data))])

def process_input_data():
    global data
    input_data = entry_data.get()  # Get input from the entry widget

    # Check if input is empty
    if not input_data.strip():
        messagebox.showerror("Empty Input", "Input cannot be empty! Please enter numbers separated by commas.")
        return
    try:
        # Convert the input string to a list of integers
        data = [int(x.strip()) for x in input_data.split(',')]
        print(data)
        # If no data is provided after conversion, raise a ValueError
        if len(data) == 0:
            raise ValueError
        # Draw the data after input
        drawData(data, ['#00BFFF' for _ in range(len(data))])     
    except ValueError:
        # Catch any invalid input errors (non-integer inputs or empty list)
        messagebox.showerror("Invalid Input", "Invalid input! Please enter valid numbers separated by commas.")


# Clear data and reset state
def clear_data():
    global data
    data = []  # Reset the data
    entry_data.delete(0, tk.END)  # Clear the input field
    error_label.config(text="")  # Clear the error message
    canvas.delete("all")  # Clear the canvas
    drawData([], [])  # Redraw the empty canvas

# Tkinter UI Setup (Ensure you use grid() for layout consistency)
root = tk.Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg='#2E2E2E')  # Dark background

# Main UI frame
UI_frame = tk.Frame(root, width=300, height=200, bg='#2E2E2E')
UI_frame.grid(row=0, column=0, padx=10, pady=5, sticky=tk.N)

tk.Label(UI_frame, text="Algorithm: ", bg='#2E2E2E', fg='white').grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
algMenu = ttk.Combobox(UI_frame, values=['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort', 'Heap Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

# Input field and button for user data
entry_label = tk.Label(UI_frame, text="Enter numbers separated by commas:", bg='#2E2E2E', fg='white')
entry_label.grid(row=1, column=0, columnspan=2, pady=10)

error_label = tk.Label(UI_frame, text="", fg="red", bg='#2E2E2E')
error_label.grid(row=2, column=0, columnspan=2, pady=5)

entry_data = tk.Entry(UI_frame, width=30)
entry_data.grid(row=3, column=0, columnspan=2, pady=10)

# Button setup
button_frame = tk.Frame(UI_frame, bg='#2E2E2E')
button_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

tk.Button(button_frame, text="Start", command=startAlgorithm, bg='#00BFFF', fg='white').grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Generate Array", command=generate, bg='#00BFFF', fg='white').grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Add", command=process_input_data, bg='#00BFFF', fg='white').grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="Clear", command=clear_data, bg='#00BFFF', fg='white').grid(row=0, column=3, padx=5, pady=5)

# Canvas for drawing the bars
canvas = tk.Canvas(root, width=600, height=400, bg='#1C1C1C')
canvas.grid(row=0, column=1, rowspan=2, padx=10, pady=5)

root.mainloop()
