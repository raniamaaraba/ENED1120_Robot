#this is the calculations based on the locomation
#test plan for team 150

#test 1 -- distance from x and y 12in(30.48cm) vert
# 20cm for 215

one_one = 0.5
one_two = 0.4
one_three = 0.5
one_four = 0.2
one_five = 0.2

one_y1 =0.5
one_y2 = 0.3
one_y3 = 0.2
one_y4 = 0.0
one_y5 = 0.1

avg_1 = (one_one + one_two + one_three + one_four + one_five) / 5
avg_1y = (one_y1 + one_y2 + one_y3 + one_y4 + one_y5) / 5

#x 0.36
#y 0.22

##print('error for  x1 {0:.2f}'.format(avg_1))
print('error for y1 {0:.2f}'.format(avg_1y))


#test 2 -- distance from x and y 36in(91.44cm) vert
# 20cm for 215

two_one = 0.1
two_two = 0.2
two_three = 1.5
two_four = 0.2
two_five = 0.2

two_y1 =0.5
two_y2 = 0.3
two_y3 = 0.2
two_y4 = 0.0
two_y5 = 0.1

avg_2 = (two_one + two_two + two_three + two_four + two_five) / 5
avg_2y = (two_y1 + two_y2 + two_y3 + two_y4 + two_y5) / 5

#x 0.44
#y 0.22

#print('error for  x2 {0:.2f}'.format(avg_2))
#print('error for y2 {0:.2f}'.format(avg_2y))

#test 3 -- distance from x and y 60in(152.4cm) vert
# 20cm for 215

three_one = -2.5
three_two = -2
three_three = -0.5
three_four = 1.0
three_five = 0.5

three_y1 =3.4
three_y2 = 3.0
three_y3 = 3.0
three_y4 = 1.5
three_y5 = 1.0

avg_3 = (three_one + three_two + three_three + three_four + three_five) / 5
avg_3y = (three_y1 + three_y2 + three_y3 + three_y4 + three_y5) / 5

#x -0.7
# y 2.38

#print('error for  x3 {0:.2f}'.format(avg_3))
#print('error for y3 {0:.2f}'.format(avg_3y))


#test 4 -- distance from x and y 84in(213.36cm) vert
# 20cm for 215

four_one = 1.2
four_two = 1.0
four_three = 1.0
four_four = 0.6
four_five = 1.0

four_y1 =5.0
four_y2 = 4.0
four_y3 = 3.5
four_y4 = 2.7
four_y5 = 2.0

avg_4 = (four_one + four_two + four_three + four_four + four_five) / 5
avg_4y = (four_y1 + four_y2 + four_y3 + four_y4 + four_y5) / 5

#x 0.96
#y 0.96

#print('error for  x4 {0:.2f}'.format(avg_4))
#print('error for y4 {0:.2f}'.format(avg_4y))

#break

x_value = float(input('Please enter the distance x(cm) for the robot to travel: '))
turn_value = float(input('Please enter 1 if the robot turns or 2 for no turn: '))


if turn_value == 1:
    turn_times = float(input('Please enter the number of times that will be completed in the total distance(8 max): '))
    if turn_times ==1:
        if (x_value >= 30):
            #x -0.32
            #y 0.22
            print('The values for error are x: -0.32')
            print('The values for error are y: 0.22')
        elif 30 < x_value <= 90:
            #x -1.40
            #y 0.20
            errorx = ([(-0.32) + (-1.40)]/2)*2
            errory = ([(0.22) + (0.20)]/2)*2
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif 90 < x_value <= 150:
            #x 1.84
            #y 0.60
            errorx = ([(1.84) + (-0.70)]/2)*2
            errory = ([(0.6) + (0.22)]/2)*2
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif x_value > 150:
            #x -4.24
            #y -0.60
            errorx = ([(1.84) + (-4.24)]/2)*2
            errory = ([(-0.60) + (0.22)]/2)*2
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
    elif turn_times == 2:
        if (x_value >= 30):
            x = -0.32 *2
            y = 0.22 *2
            print('The values for error are x: {0:.2f}'.format(x))
            print('The values for error are y: {0:.2f}'.format(y))
        elif 30 < x_value <= 90:
            #x -1.40
            #y 0.20
            errorx = ([(-0.32) + (-1.40)]/2)*4
            errory = ([(0.22) + (0.20)]/2)*4
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif 90 < x_value <= 150:
            #x 1.84
            #y 0.60
            errorx = ([(1.84) + (-0.70)]/2)*4
            errory = ([(0.6) + (0.22)]/2)*4
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif x_value > 150:
            #x -4.24
            #y -0.60
            errorx = ([(1.84) + (-4.24)]/2)*4
            errory = ([(-0.60) + (0.22)]/2)*4
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
    elif turn_times == 3:
        if (x_value >= 30):
            x = -0.32 *3
            y = 0.22 *3
            print('The values for error are x: {0:.2f}'.format(x))
            print('The values for error are y: {0:.2f}'.format(y))
        elif 30 < x_value <= 90:
            #x -1.40
            #y 0.20
            errorx = ([(-0.32) + (-1.40)]/2)*6
            errory = ([(0.22) + (0.20)]/2)*6
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif 90 < x_value <= 150:
            #x 1.84
            #y 0.60
            errorx = ([(1.84) + (-0.70)]/2)*6
            errory = ([(0.6) + (0.22)]/2)*6
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif x_value > 150:
            #x -4.24
            #y -0.60
            errorx = ([(1.84) + (-4.24)]/2)*6
            errory = ([(-0.60) + (0.22)]/2)*6
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
    elif turn_times == 4:
        if (x_value >= 30):
            x = -0.32 *4
            y = 0.22 *4
            print('The values for error are x: {0:.2f}'.format(x))
            print('The values for error are y: {0:.2f}'.format(y))
        elif 30 < x_value <= 90:
            #x -1.40
            #y 0.20
            errorx = ([(-0.32) + (-1.40)]/2)*8
            errory = ([(0.22) + (0.20)]/2)*8
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif 90 < x_value <= 150:
            #x 1.84
            #y 0.60
            errorx = ([(1.84) + (-0.70)]/2)*8
            errory = ([(0.6) + (0.22)]/2)*8
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif x_value > 150:
            #x -4.24
            #y -0.60
            errorx = ([(1.84) + (-4.24)]/2)*8
            errory = ([(-0.60) + (0.22)]/2)*8
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
    elif turn_times == 5:
        if (x_value >= 30):
            x = -0.32 *5
            y = 0.22 *5
            print('The values for error are x: {0:.2f}'.format(x))
            print('The values for error are y: {0:.2f}'.format(y))
        elif 30 < x_value <= 90:
            #x -1.40
            #y 0.20
            errorx = ([(-0.32) + (-1.40)]/2)*10
            errory = ([(0.22) + (0.20)]/2)*10
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif 90 < x_value <= 150:
            #x 1.84
            #y 0.60
            errorx = ([(1.84) + (-0.70)]/2)*10
            errory = ([(0.6) + (0.22)]/2)*10
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif x_value > 150:
            #x -4.24
            #y -0.60
            errorx = ([(1.84) + (-4.24)]/2)*10
            errory = ([(-0.60) + (0.22)]/2)*10
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
    elif turn_times == 6:
        if (x_value >= 30):
            x = -0.32 *6
            y = 0.22 *6
            print('The values for error are x: {0:.2f}'.format(x))
            print('The values for error are y: {0:.2f}'.format(y))
        elif 30 < x_value <= 90:
            #x -1.40
            #y 0.20
            errorx = ([(-0.32) + (-1.40)]/2)*12
            errory = ([(0.22) + (0.20)]/2)*12
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif 90 < x_value <= 150:
            #x 1.84
            #y 0.60
            errorx = ([(1.84) + (-0.70)]/2)*12
            errory = ([(0.6) + (0.22)]/2)*12
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif x_value > 150:
            #x -4.24
            #y -0.60
            errorx = ([(1.84) + (-4.24)]/2)*12
            errory = ([(-0.60) + (0.22)]/2)*12
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
    elif turn_times == 7:
        if (x_value >= 30):
            x = -0.32 *7
            y = 0.22 *7
            print('The values for error are x: {0:.2f}'.format(x))
            print('The values for error are y: {0:.2f}'.format(y))
        elif 30 < x_value <= 90:
            #x -1.40
            #y 0.20
            errorx = ([(-0.32) + (-1.40)]/2)*14
            errory = ([(0.22) + (0.20)]/2)*14
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif 90 < x_value <= 150:
            #x 1.84
            #y 0.60
            errorx = ([(1.84) + (-0.70)]/2)*14
            errory = ([(0.6) + (0.22)]/2)*14
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif x_value > 150:
            #x -4.24
            #y -0.60
            errorx = ([(1.84) + (-4.24)]/2)*14
            errory = ([(-0.60) + (0.22)]/2)*14
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
    elif turn_times == 8:
        if (x_value >= 30):
            x = -0.32 *8
            y = 0.22 *8
            print('The values for error are x: {0:.2f}'.format(x))
            print('The values for error are y: {0:.2f}'.format(y))
        elif 30 < x_value <= 90:
            #x -1.40
            #y 0.20
            errorx = ([(-0.32) + (-1.40)]/2)*16
            errory = ([(0.22) + (0.20)]/2)*16
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif 90 < x_value <= 150:
            #x 1.84
            #y 0.60
            errorx = ([(1.84) + (-0.70)]/2)*16
            errory = ([(0.6) + (0.22)]/2)*16
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
        elif x_value > 150:
            #x -4.24
            #y -0.60
            errorx = ([(1.84) + (-4.24)]/2)*16
            errory = ([(-0.60) + (0.22)]/2)*16
            print('The values for error are x: {0:.2f}'.format(errorx))
            print('The values for error are y: {0:.2f}'.format(errory))
    
        
elif turn_value ==2:
    #run values for 1-4
    if x_value >= 30:
        print('The values for error are x 0.36 & y 0.22')
    elif 30 < x_value <= 90:
        errorx = [(0.36) + (0.44)]/2
        errory = [(0.22) + (0.22)]/2
        print('The values for error are x: {0:.2f}'.format(errorx))
        print('The values for error are y: {0:.2f}'.format(errory))
    elif 90 < x_value <= 150:
        errorx = [(0.44) + (-0.70)]/2
        errory = [(2.38) + (0.22)]/2
        print('The values for error are x: {0:.2f}'.format(errorx))
        print('The values for error are y: {0:.2f}'.format(errory))
    elif x_value > 150:
        errorx = [(0.96) + (-0.70)]/2
        errory = [(2.38) + (0.96)]/2
        print('The values for error are x: {0:.2f}'.format(errorx))
        print('The values for error are y: {0:.2f}'.format(errory))




#break

#test 5 -- distance from x and y 12in(30.48cm) turn
# 20cm for 215

five_one = -0.5
five_two = -0.3
five_three = -0.5
five_four = -0.5
five_five = 0.2

five_y1 = 0.5
five_y2 = 0.5
five_y3 = -0.3
five_y4 = 0.2
five_y5 = 0.2

avg_5 = (five_one + five_two + five_three + five_four + five_five) / 5
avg_5y = (five_y1 + five_y2 + five_y3 + five_y4 + five_y5) / 5

#print('error for  x5 {0:.2f}'.format(avg_5))
#print('error for y5 {0:.2f}'.format(avg_5y))

#x -0.32
#y 0.22

#test 6 -- distance from x and y 36in(91.44cm) turn
# 20cm for 215

six_one = 2.5
six_two = 3.0
six_three = 1.5
six_four = -0.5
six_five = 0.5

six_y1 = -2.0
six_y2 = 1.0
six_y3 = 1.0
six_y4 = 0.5
six_y5 = 0.5

avg_6 = (six_one + six_two + six_three + six_four + six_five) / 5
avg_6y = (six_y1 + six_y2 + six_y3 + six_y4 + six_y5) / 5

#print('error for  x6 {0:.2f}'.format(avg_6))
#print('error for y6 {0:.2f}'.format(avg_6y))

#x -1.40
#y 0.20

#test 7 -- distance from x and y 60in(152.4cm) turn
# 20cm for 215

seven_one = 3.2
seven_two = 2.6
seven_three = 2.0
seven_four = 0.6
seven_five = 0.8

seven_y1 = 0.5
seven_y2 = 0.5
seven_y3 = 1.0
seven_y4 = 0.5
seven_y5 = 0.5

avg_7 = (seven_one + seven_two + seven_three + seven_four + seven_five) / 5
avg_7y = (seven_y1 + seven_y2 + seven_y3 + seven_y4 + seven_y5) / 5

#print('error for  x7 {0:.2f}'.format(avg_7))
#print('error for y7 {0:.2f}'.format(avg_7y))

#x 1.84
#y 0.60

#test 8 -- distance from x and y 36in(91.44cm) turn
# 20cm for 215

eight_one = -7.9
eight_two = -6.4
eight_three = -3.4
eight_four = -3.4
eight_five = -0.1

eight_y1 = -1.0
eight_y2 = -1.0
eight_y3 = -1.0
eight_y4 = 0.0
eight_y5 = 0.0

avg_8 = (eight_one + eight_two + eight_three + eight_four + eight_five) / 5
avg_8y = (eight_y1 + eight_y2 + eight_y3 + eight_y4 + eight_y5) / 5

#print('error for  x8 {0:.2f}'.format(avg_8))
#print('error for y8 {0:.2f}'.format(avg_8y))

#x -4.24
#y -0.60

