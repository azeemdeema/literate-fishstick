import sys

def generate_shape(n, shape):
    """
    Generates a geometric pattern on an n x n grid.

    Args:
        n: Grid size (n x n, always odd for diamond)
        shape: Either "checkerboard" or "diamond"

    Returns:
        A 2D list of integers (0 or 1) representing the pattern.
    """
    if shape == "checkerboard":
        h = n >> 1          # bit shift: faster than n // 2
        r = n & 1           # bit AND: faster than n % 2
        row0 = [0, 1] * h + [0] * r
        row1 = [1, 0] * h + [1] * r
        e = (n + 1) >> 1    # number of even-index rows (ceiling division)
        result = [None] * n
        result[::2]  = [row0] * e 
        result[1::2] = [row1] * (n - e) 
        return result
    else:  # diamond
        c = n >> 1          # center index
        rows = []
        append = rows.append   # local method ref: avoids repeated attribute lookup
        for filled in range(c + 1):
            cf = c - filled
            # filled increments naturally 0..c
            append([0] * cf + [1] * (2 * filled + 1) + [0] * cf)
        return rows + rows[-2::-1]  # mirror top half (excluding middle row)


# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        n = int(input().strip())
        shape = input().strip()

        result = generate_shape(n, shape)
        for row in result:
            print(" ".join(str(x) for x in row))

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)