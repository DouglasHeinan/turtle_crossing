from turtle import Screen
from crosser import Crosser
from lanes import Lanes
from cars import Car
from update import Update
import random
import time
'''
The main file
'''

def main():
    screen = Screen()
    update = Update()

    screen.setup(width=600, height=600)
    screen.title('Turtle Crossing')
    screen.tracer(0)
    screen.update()
    chris_cross = Crosser()
    lanes = Lanes()
    car_list = []
    level = 1
    lives = 3
    game_over = False
    start_y_dict, start_list = car_speed_position(level)
    for start_car in range(40 + (level * 2)):
        new_car = Car(start_y_dict, start_list, level)
        new_car.start_car()
        car_list = add_car(car_list, new_car)

    update.stage_start(level, lives)
    while not game_over:
        screen.listen()
        screen.onkey(chris_cross.forward, "Up")
        screen.onkey(chris_cross.backward, "Down")
        screen.onkey(chris_cross.left, "Left")
        screen.onkey(chris_cross.right, "Right")

        screen.update()
        time.sleep(.1)

        make_new = random.randrange(0, 1)
        if make_new == 0:
            new_car = Car(start_y_dict, start_list, level)
            car_list = add_car(car_list, new_car)
        for car in car_list:
            car.drive()
            if car.xcor() < -310 or car.xcor() > 310:
                car.hideturtle()
                car_list.remove(car)

        for car in car_list:
            if chris_cross.distance(car) < 10:
                screen.onkey(None, "Up")
                screen.onkey(None, "Down")
                screen.onkey(None, "Left")
                screen.onkey(None, "Right")
                screen.update()
                lives -= 1
                if lives == 0:
                    game_over = True
                    update.game_over(level)
                else:
                    update.stage_start(level, lives)
                    chris_cross.start_chris_cross()
                    for entry in car_list:
                        entry.hideturtle()
                        entry.goto(-310, 0)
                    for start_car in range(40 + (level * 2)):
                        new_car = Car(start_y_dict, start_list, level)
                        for each_car in car_list:
                            if each_car.distance(new_car) < 20:
                                new_car.hideturtle()
                                new_car.goto(-310, 0)
                        car_list.append(new_car)
                        new_car.start_car()
                screen.update()

        if chris_cross.ycor() > 250:
            screen.onkey(None, "Up")
            screen.onkey(None, "Down")
            screen.onkey(None, "Left")
            screen.onkey(None, "Right")
            screen.update()
            level += 1
            update.new_level(level)
            chris_cross.start_chris_cross()
            for car in car_list:
                car.hideturtle()
                car.goto(-310, 0)
            for car in range(40 + (level * 2)):
                new_car = Car(start_y_dict, start_list, level)
                car_list.append(new_car)
                new_car.start_car()
            screen.update()

    screen.exitonclick()


def car_speed_position(level):
    start_y_dict = {}
    start_list = []
    x_pos = [300, -300]
    for y_coordinate in range(-238, 253, 25):
        y_start_pos = y_coordinate
        x_start_pos = random.choice(x_pos)
        start_coordinate = (x_start_pos, y_start_pos)
        start_list.append(start_coordinate)
        start_y_dict[y_start_pos] = random.randint(0, level)
    return start_y_dict, start_list


def add_car(car_list, new_car):
    for car in car_list:
        if car.distance(new_car) < 20:
            new_car.hideturtle()
            new_car.goto(-310, 0)
    if new_car.xcor() > -309:
        car_list.append(new_car)
    return car_list


if __name__ == '__main__':
    main()
