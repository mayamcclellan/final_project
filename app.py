import gradio as gr

# this is just some sample data for shuttle stops
def generate_stops():
    return [
        {"name": "Stop A", "crowd": 12},
        {"name": "Stop B", "crowd": 5},
        {"name": "Stop C", "crowd": 20},
        {"name": "Stop D", "crowd": 8}
    ]

# this is my merge sort function
# it keeps splitting the list until each part is really small (1 item)
def merge_sort(stops):

    # if there is only 1 item, I just return it because it's already sorted
    if len(stops) <= 1:
        return stops

    # I find the middle so I can split the list into two halves
    mid = len(stops) // 2

    # I sort the left side first
    left = merge_sort(stops[:mid])

    # then I sort the right side
    right = merge_sort(stops[mid:])

    # then I combine both sorted halves together
    return merge(left, right)

# this part merges the two sorted lists together
def merge(left, right):
    result = []
    i = 0
    j = 0

    # I compare items from both lists one by one
    while i < len(left) and j < len(right):

        # I compare crowd numbers to decide which one comes first
        # I made it so higher crowd comes first
        if left[i]["crowd"] > right[j]["crowd"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # if there is anything left in the left list, I add it
    result.extend(left[i:])

    # if there is anything left in the right list, I add it
    result.extend(right[j:])

    return result

# this is where I run everything for the app
def run_sort():

    # I get the sample shuttle stop data
    data = generate_stops()

    # I sort it using my merge sort function
    sorted_data = merge_sort(data)

    # I format the output so it looks clean in the app
    output = "Ranked Shuttle Stops (by crowd size)\n\n"
    for s in sorted_data:
        output += f"{s['name']} → Crowd: {s['crowd']}\n"

    return output

# this creates the actual Gradio app
gr.Interface(
    fn=run_sort,
    inputs=[],
    outputs="text",
    title= "Shuttle Stop Crowd Ranking Simulator"
).launch()
