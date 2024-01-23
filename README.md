# object-colorer
 
## How to Use
1. Paste your vertices for a Float32Array JavaScript WebGL (in (x, y, z, w) format) into a new TXT file in the `arrays` folder.
2. Update the `file_name` variable to match the TXT file you just created:
```python
file_name = "your-file.txt"
```
3. Choose your colormap from [this link](https://matplotlib.org/stable/users/explain/colors/colormaps.html) and change the variable `COLOR_MAP` to match which you want:
```python
COLOR_MAP = "viridis"
```
4. Run the program! Your outputted file should be in the `outputs` folder.
