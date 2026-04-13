## Algorithm Name

Shuttle Stop Crowd Ranking - Merge Sort



I chose Merge Sort because it’s a clear and efficient way to sort shuttle stops based on crowd count, and it works well with lists. It assumes that each stop has a number for crowd count so they can be compared. The list doesn’t need to be sorted before, but my app will check that the crowd counts are valid numbers before running. During the simulation, the user will see which stops are being compared and when they move to a new position. This makes it easier to understand how the final sorted list is built step by step.



## Demo video/gif/screenshot of test



<img width="2223" height="1203" alt="Final code #1" src="https://github.com/user-attachments/assets/5b12b250-4d04-48f7-84ab-ba558255c169" />

<img width="2230" height="1198" alt="Final code #2" src="https://github.com/user-attachments/assets/917307ee-1ed8-492b-b94c-54f95d767df8" />


## Problem Breakdown \& Computational Thinking



#### Decomposition



I broke the problem into smaller steps: first I create or generate a list of shuttle stops with crowd counts, then I sort the list using Merge Sort, and finally I display the sorted results step by step in the app.



#### Pattern Recognition



Merge Sort keeps repeating the same process of splitting the list into smaller parts, comparing values, and then merging them back together in order. This pattern continues until everything is fully sorted.



#### Abstraction



The user will only see the important parts like which stops are being compared and when they move into a new position. I am not showing the internal recursion or extra details because that would make it harder to understand.



#### Algorithm Design



The user inputs or generates a list of shuttle stops, and my program sorts it using Merge Sort while tracking each step. The Gradio interface then shows the comparisons, movements, and final sorted list based on crowd count. The data is stored as a list of dictionaries with each stop name and crowd count.





#### Flowchart



Start

&#x20; ↓

Generate/Input Shuttle Stops

&#x20; ↓

Validate Data

&#x20; ↓

Run Merge Sort

&#x20; ↓

Track Comparisons \& Merges

&#x20; ↓

Display Steps in UI

&#x20; ↓

Show Final Sorted List

&#x20; ↓

End



## Steps to Run



1\. First, download or clone the GitHub repository to your computer.



2\. Then install Gradio by running:

&#x20;  pip install gradio



3\. Open the project in Colab or a Python editor like VS Code.



4\. Run the file called `app.py`.



5\. After that, click the “Run Sort” button in the Gradio app.



6\. The app then shows the step-by-step sorting process and the final ranked list of shuttle stops based on crowd count.



## Hugging Face Link







## Testing



In my initial draft, I ran into several issues while trying to implement Merge Sort. I made mistakes like calculating the middle index incorrectly, skipping elements during the merge step, and not handling all remaining values when combining lists. I also had a problem where one of the crowd counts was stored as a string instead of a number, which caused errors during comparisons. Because of these issues, the sorting either gave incorrect results or didn’t work at all. I fixed these problems step by step with the assistance of ChatGPT, which helped me better understand how Merge Sort works and how to debug my code.

### Draft Code
<img width="2231" height="1207" alt="draft_1" src="https://github.com/user-attachments/assets/98753de7-0f20-4bb6-9a0d-3dd97a1f3714" />

<img width="2236" height="1204" alt="draft_2" src="https://github.com/user-attachments/assets/4cb8daa3-fe6c-4fe3-a702-eed9d154a8be" />

### Edge Case Test



## Author \& AI Acknowledgment



I wrote most of the code, but I had some difficulties so I used AI Level 4 to help me fix the errors in my code.



https://chatgpt.com/share/69dc3a99-6664-83ea-b7e0-85e6b5e1c747

