import pygame 
import time

# function to implement bubble sort
def bubble_sort(screen, bar_heights, bar_color, bg_color, delay, draw_bars):

    n = len(bar_heights)
    for i in range(n -  1):
        for j in range(n - i - 1):

            # highlight the bars being compared
            screen.fill(bg_color)
            draw_bars(screen, bar_heights, 1000, 600, bar_color, highlight = (j, j + 1))
            pygame.display.flip()

            # swap bars
            if (bar_heights[j] > bar_heights[j + 1]):
                temp = bar_heights[j]
                bar_heights[j] = bar_heights[j + 1]
                bar_heights[j + 1] = temp

            # highlight the bars being swapped
            screen.fill(bg_color)
            draw_bars(screen, bar_heights, 1000, 600, bar_color, highlight = (j, j + 1), swap = True)
            pygame.display.flip()
            time.sleep(delay)


def merge_sort(screen, bar_heights, bar_color, bg_color, delay, draw_bars):

    n = len(bar_heights)
    current_size = 1
    
    while current_size < n:
        for start in range(0, n, current_size * 2): # break array in to chunks

            #calc mid point of current sub array
            mid = min(start + current_size, n) 
            end = min(start + 2 * current_size, n)

            # divide array into 2 halves
            left = bar_heights[start:mid]
            right = bar_heights[mid:end]

            # adjust bars for visualization
            screen.fill(bg_color)
            draw_bars(screen, bar_heights, 1000, 600, bar_color, highlight=range(start, end))
            pygame.display.flip()
            time.sleep(delay)

            merged = merge(screen, left, right, bar_heights, start, bar_color, bg_color, delay, draw_bars)
            bar_heights[start:end] = merged
        
        current_size *= 2

def merge(screen, left, right, bar_heights, start_index, bar_color, bg_color, delay, draw_bars):
    sorted_array = []
    i = j = 0

    # merge
    while i < len(left) and j < len(right):
        screen.fill(bg_color) 
        draw_bars(screen, bar_heights, 1000, 600, bar_color, highlight=[start_index + len(sorted_array)])
        pygame.display.flip()

        if left[i] < right[j]:  # compare elements from both halves
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

        # Update the visualized array
        bar_heights[start_index:start_index + len(sorted_array)] = sorted_array
        time.sleep(delay)

    # append remaining elements from left 
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
        bar_heights[start_index:start_index + len(sorted_array)] = sorted_array
        screen.fill(bg_color)
        draw_bars(screen, bar_heights, 1000, 600, bar_color, highlight=[start_index + len(sorted_array) - 1])
        pygame.display.flip()
        time.sleep(delay)

    # append remaining elements from right
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
        bar_heights[start_index:start_index + len(sorted_array)] = sorted_array
        screen.fill(bg_color)
        draw_bars(screen, bar_heights, 1000, 600, bar_color, highlight=[start_index + len(sorted_array) - 1])
        pygame.display.flip()
        time.sleep(delay)

    return sorted_array


    



