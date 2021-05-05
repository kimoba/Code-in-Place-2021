# define constants
ROWS = 3
COLUMNS = 3

def main():
    print("Welcome to first person Karel. You're at row 1, column 1, facing East (facing column " + str(COLUMNS) + ")")
    facing_direction = 'East' # this variable will keep track of the way Karel is facing -- it changes if the user says to "turn left"!
    curr_col = 1 # this variable ...
    curr_row = 1 # ... and this one keep track of Karel's position in the world! they may change if the user says to "move"
    action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    while action != "":

        if action == "turn left":  # check directions

            if facing_direction == 'East':
                facing_direction = 'North'
                print(f"You turned left and are now facing {facing_direction}")
            elif facing_direction == 'North':
                facing_direction = 'West'
                print(f"You turned left and are now facing {facing_direction}")
            elif facing_direction == 'West':
                facing_direction = 'South'
                print(f"You turned left and are now facing {facing_direction}")
            elif facing_direction == 'South':
                facing_direction = 'East'
                print(f"You turned left and are now facing {facing_direction}")

            # get new user action
            action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
        
        if action == "move":
            
            # facing EAST and moving
            if facing_direction == 'East' and curr_col < COLUMNS:
                curr_col += 1
                print(f"You moved one step forward and now you're at row {curr_row} column {curr_col}.")
            # facing WEST and moving
            elif facing_direction == 'West' and curr_col > 1:
                curr_col -= 1
                print(f"You moved one step forward and now you're at row {curr_row} column {curr_col}.")
            # facing NORTH and moving
            elif facing_direction == 'North' and curr_row < ROWS:
                curr_row += 1
                print(f"You moved one step forward and now you're at row {curr_row} column {curr_col}.")
            # facing SOUTH and moving
            elif facing_direction == 'South' and curr_row > 1:
                curr_row -= 1
                print(f"You moved one step forward and now you're at row {curr_row} column {curr_col}.")
            else:
                # if column or row == 0
                print("You can't move forward")

            # get new user action
            action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    
    #  if user stops input, tell them where they are
    print(f"You've ended up at row {curr_row} and column {curr_col} facing {facing_direction}.")

        # print(facing_direction)
        # print(curr_col)
        # print(curr_row)


if __name__ == "__main__":
    main()
