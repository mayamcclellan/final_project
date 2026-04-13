import gradio as gr

# making some sample shuttle stops with crowd numbers
def generate_stops():
    return [
        {"name": "Stop A", "crowd": 12},
        {"name": "Stop B", "crowd": 5},
        {"name": "Stop C", "crowd": 20},
        {"name": "Stop D", "crowd": 8}
    ]

# this is my merge sort function
# it keeps splitting the list until it can't split anymore
def merge_sort(stops):

    # if there's only 1 item, it's already sorted
    if len(stops) <= 1:
        return stops

    # find the middle so I can split the list into 2 halves
    mid = len(stops) // 2

    # sorting left side
    left = merge_sort(stops[:mid])

    # sorting right side
    right = merge_sort(stops[mid:])

    # now I combine them back together in order
    return merge(left, right)

# this part actually puts the two sorted lists together
def merge(left, right):
    result = []
    i = 0
    j = 0

    # comparing items from both sides one by one
    while i < len(left) and j < len(right):

        # checking which crowd number is smaller
        if left[i]["crowd"] > right[j]["crowd"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # if anything is left over, just add it in
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# this is where I run everything
def run_sort():

    # get the fake shuttle stop data
    data = generate_stops()

    # i saw some values were strings so i converted everything to int
    for stop in data:
        stop["crowd"] = int(stop["crowd"])

    # now I sort it using merge sort
    sorted_data = merge_sort(data)

    # just making it look nice for output
    output = ""
    for s in sorted_data:
        output += f"{s['name']} {s['crowd']}\n"

    return output

# this makes the simple web app
gr.Interface(
    fn=run_sort,
    inputs=[],
    outputs="text"
).launch()
