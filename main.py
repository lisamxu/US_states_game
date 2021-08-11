import turtle
screen = turtle.Screen()
import pandas

screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)


#check if guess among top 50 states
    #create pandas dataframe from csv data, create state list,
    #create while loop, while game is true
    #check if user input is value in state list
    #if yes, then retrieve coordinates
        #get the row with the state name, get x coordinate, get y coordinate
    # write/plot name on map (see turtle)
    #if no, ask user for input again

data = pandas.read_csv("50_states.csv")
print(data)
all_states = data.state.to_list()
print(all_states)
guessed_states = []


score = 0
while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess a state", prompt="Enter a state name")
    tanswer_state = answer_state.title()
    print(tanswer_state)
    if tanswer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if tanswer_state in all_states:
        guessed_states.append(tanswer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        score += 1
        data_row = data[data.state == tanswer_state]
        data_row_list = data_row.values.tolist()
        print(data_row_list)
        x_value = data_row_list[0][1]
        print(x_value)
        y_value = data_row_list[0][2]
        print(y_value)
        t.setposition(x_value, y_value)
        t.write(tanswer_state, align="right")
        print(score)


#states to learn.csv


#use loop to allow user to keep guessing
#record correct guesses in a list
#keep track of the score


turtle.mainloop()

