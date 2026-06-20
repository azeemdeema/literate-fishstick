import sys
from collections import defaultdict

def processGame(events, H):
    """
    events: list of tuples (player, frame, attack_value)
        player: 1 or 2
        frame: non-negative integer
        attack_value: positive integer
    H: starting HP for both players

    Returns: [hp1, hp2] with each clamped to min 0
    """
    # If no events, both players remain at full health
    if not events:
        return [H, H]

    hp = [H, H]

    # Accumulate damage per player per frame in one O(n) pass
    d = defaultdict(lambda: [0, 0])
    for p, f, a in events:
        d[f][2 - p] += a        # player=1 -> damages hp[1], player=2 -> damages hp[0]

    # Process frames in order - only f unique frames sorted, not all n events
    for f in sorted(d):
        hp[0] -= d[f][0]
        hp[1] -= d[f][1]
        if hp[0] <= 0 or hp[1] <= 0:
            break
    
    # Clamp HP to minimum 0 before returning
    return [max(0, hp[0]), max(0, hp[1])]


# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        H = int(input().strip())
        n = int(input().strip())
        events = []
        for _ in range(n):
            parts = input().strip().split()
            events.append((int(parts[0]), int(parts[1]), int(parts[2])))

        result = processGame(events, H)
        print(f"{result[0]} {result[1]}")

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)