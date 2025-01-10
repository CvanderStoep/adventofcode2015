def calculate_wrapping_paper_and_ribbon(present_dimensions):
    total_paper = 0
    total_ribbon = 0

    for dimensions in present_dimensions:
        l, w, h = map(int, dimensions.split('x'))

        # Calculate the surface areas
        lw = l * w
        wh = w * h
        hl = h * l

        # Calculate the smallest side area
        smallest_side = min(lw, wh, hl)

        # Calculate total wrapping paper needed for this present
        wrapping_paper = 2 * lw + 2 * wh + 2 * hl + smallest_side
        total_paper += wrapping_paper

        # Calculate the smallest perimeter
        smallest_perimeter = min(2 * (l + w), 2 * (w + h), 2 * (h + l))

        # Calculate the volume (for the bow)
        volume = l * w * h

        # Calculate total ribbon needed for this present
        ribbon = smallest_perimeter + volume
        total_ribbon += ribbon

    return total_paper, total_ribbon


# Example usage
present_dimensions = ["2x3x4", "1x1x10"]
total_paper_needed, total_ribbon_needed = calculate_wrapping_paper_and_ribbon(present_dimensions)
print(f"Total wrapping paper needed: {total_paper_needed} square feet")  # Output: 101
print(f"Total ribbon needed: {total_ribbon_needed} feet")  # Output: 48
