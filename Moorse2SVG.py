import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Morse code string
morse_code = "..-. .-.. .- --. ---... -.-- --- ..- - ..- -... . .-.-.- -.-. --- -- -..-. .-- .- - -.-. .... ..--.. ...- -.. --.- .-- ....- .-- ----. .-- --. -..- -.-. --.-"

# Split into characters and spaces
elements = []
for char in morse_code:
    if char in ['.', '-']:
        elements.append(char)
    elif char == ' ':
        elements.append(' ')  # Space between letters

# Generate sinewave x positions with enough spacing
spacing = 0.6
x_positions = []
current_x = 0
for element in elements:
    x_positions.append(current_x)
    if element == ' ':
        current_x += spacing * 2  # More space for spaces
    else:
        current_x += spacing

# Sine wave y values
x_vals = np.array(x_positions)
y_vals = np.sin(x_vals / 3) * 0.8  # Smoothed sine wave with amplitude adjustment

# Plot
fig, ax = plt.subplots(figsize=(24, 6), facecolor='white')
ax.set_facecolor('white')

# Plot symbols with oscilloscope-style neon green
green = '#00FF41'

for i, element in enumerate(elements):
    x, y = x_vals[i], y_vals[i]
    if element == '.':
        circle = patches.Circle((x, y), radius=0.1, color=green)
        ax.add_patch(circle)
    elif element == '-':
        rect = patches.FancyBboxPatch((x - 0.15, y - 0.05), 0.3, 0.1,
                                      boxstyle="round,pad=0.02", color=green)
        ax.add_patch(rect)

# Optionally, add a glowing sinewave path for effect
ax.plot(x_vals, y_vals, color=green, linewidth=0.5, alpha=0.15)

# Enhancements for oscilloscope vibe
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(x_vals.min() - 1, x_vals.max() + 1)
ax.set_ylim(y_vals.min() - 1, y_vals.max() + 1)

# Save as SVG
svg_path = "./morse_oscilloscope_style.svg"
fig.savefig(svg_path, format='svg', bbox_inches='tight', transparent=True)
plt.close(fig)

svg_path
