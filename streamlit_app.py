import streamlit as st
import numpy as np
import random
import time

# Game parameters
width = 20
height = 20
snake = [(5, 5)]
snake_direction = (0, 1)
food_position = (random.randint(0, height - 1), random.randint(0, width - 1))
score = 0

def draw_game(snake, food_position):
    grid = np.zeros((height, width))
    for (y, x) in snake:
        grid[y, x] = 1
    food_y, food_x = food_position
    grid[food_y, food_x] = 2
    return grid

def move_snake(snake, direction):
    head_y, head_x = snake[0]
    new_head = (head_y + direction[0], head_x + direction[1])
    return [new_head] + snake[:-1]

def check_collision(snake):
    head = snake[0]
    if (head[0] < 0 or head[0] >= height or 
        head[1] < 0 or head[1] >= width or 
        head in snake[1:]):
        return True
    return False

def grow_snake(snake):
    return [snake[0]] + snake

def reset_game():
    global snake, snake_direction, food_position, score
    snake = [(5, 5)]
    snake_direction = (0, 1)
    food_position = (random.randint(0, height - 1), random.randint(0, width - 1))
    score = 0

st.title("Snake Game")

# Game loop
while True:
    grid = draw_game(snake, food_position)
    st.image(grid, use_column_width=True, clamp=True)
    st.write(f"Score: {score}")

    # Control the snake
    key = st.text_input("Control the snake (W/A/S/D):", "")
    if key:
        if key.lower() == 'w':
            snake_direction = (-1, 0)
        elif key.lower() == 's':
            snake_direction = (1, 0)
        elif key.lower() == 'a':
            snake_direction = (0, -1)
        elif key.lower() == 'd':
            snake_direction = (0, 1)
    
    # Move the snake
    snake = move_snake(snake, snake_direction)

    # Check for collisions
    if check_collision(snake):
        st.write("Game Over! Press 'R' to restart.")
        if st.button("Restart"):
            reset_game()
        break

    # Check for food
    if snake[0] == food_position:
        score += 1
        snake = grow_snake(snake)
        food_position = (random.randint(0, height - 1), random.randint(0, width - 1))

    time.sleep(0.2)

    st.experimental_rerun()
