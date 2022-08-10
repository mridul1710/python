import discord
import math

client = discord.Client()

#Change your token you got from the first part of the assignment here.
TOKEN = "OTM1MDIwNTM4NjA5NDE4MzAw.Ye4jvA.WE1PAIAk4EZKd-vjE8GHxWNpQ-0"

xc = -1.0
yc = -1.0
r = -1.0
x1 = -1.0
y1 = -1.0
x2 = -1.0
y2 = -1.0

numberOfIntersectionPoints = 0
xIntersectionPointOne = -1.0
yIntersectionPointOne = -1.0
xIntersectionPointTwo = -1.0
yIntersectionPointTwo = -1.0

#
def solveEquation():
    # Do NOT change anything from lines 28-40!
    # This is just the starter code and you do not need to understand what is going on here.
    # Unless you are curious, of course.
    global numberOfIntersectionPoints
    global xIntersectionPointOne
    global yIntersectionPointOne
    global xIntersectionPointTwo
    global yIntersectionPointTwo

    global xc
    global yc
    global r
    global x1
    global y1
    global x2
    global y2
    f_x1 = float(x1)  # Students, you write your code starting from here! Make sure your indentation is in line with lines 28-40
    f_x2 = float(x2)
    f_xc = float(xc)
    f_yc = float(yc)
    f_y1 = float(y1)
    f_y2 = float(y2)
    f_r = float(r)
    xIntersectionPointOne = -1.0    #resetting values so that previous results are not displayed
    yIntersectionPointOne = -1.0
    xIntersectionPointTwo = -1.0
    yIntersectionPointTwo = -1.0
    import math as mt
    a = (((f_x2 - f_x1)**2) + ((f_y2 - f_y1)**2))
    b = 2*((f_x1 - f_xc)*(f_x2 - f_x1)+(f_y1 - f_yc)*(f_y2 - f_y1))
    c = (f_x1 - f_xc)**2+(f_y1 - f_yc)**2-f_r**2

    discrim = b**2 - 4*a*c  # discriminate refers to the term b**2 - 4*a*c
    if discrim < 0 :
        print("there are no intersection points")
        numberOfIntersectionPoints = 0
    elif discrim == 0 :
        alpha = ((-1) * b + mt.sqrt(discrim))/(2*a)  #only positive operator taken as sqrt(0) = 0 and plus or minus doesn't matter
        if alpha > 1 or alpha < 0 : #special case, if alpha not between 0 and 1, there will be no intersection points
            print(f'the line and the circle do not intersect')
            numberOfIntersectionPoints = 0


        else:
            x = (1 - alpha) * f_x1 + alpha * f_x2
            y = (1 - alpha) * f_y1 + alpha * f_y2
            print(f'the line and the circle intersect at one point')
            print(f'({x},{y})')
            numberOfIntersectionPoints  = 1
            xIntersectionPointOne = x  #i used a different variable to represent intersection points so I am passing it to the one mentioned in the file
            yIntersectionPointOne = y  #same here

    elif discrim > 0 :
        alpha_positive = ((-1) * b + mt.sqrt(discrim))/(2 * a) # positive operator considered on the quadratic formula

        alpha_negative = ((-1) * b - mt.sqrt( discrim))/(2 * a)  # negative operator considered on the quadratic formula
        if (alpha_positive > 1 or alpha_positive < 0) and (alpha_negative > 1 or alpha_negative < 0): #special case considered, if both coordinates are not between 0 and 1 both are omited
            print("there are no intersection points")
            numberOfIntersectionPoints = 0

        else:
            xp = (1 - alpha_positive) * f_x1 + alpha_positive * f_x2  # x coordinate when positive operator used
            yp = (1 - alpha_positive) * f_y1 + alpha_positive * f_y2  # y coordinate when positive operator used
            xn = (1 - alpha_negative) * f_x1 + alpha_negative * f_x2  # x coordinate when negative operator used
            yn = (1 - alpha_negative) * f_y1 + alpha_negative * f_y2  # y coordinate when negative operator used
            if alpha_positive > 1 or alpha_positive < 0: #if one of the obtained values of alpha is not between 0 or 1 we simply omit it and go for the other value
                print("the line and circle intersect at 1 point")
                print(f'{xn},{yn}')
                numberOfIntersectionPoints = 1
                xIntersectionPointOne = xn  #same idea as above I
                yIntersectionPointOne = yn


            elif alpha_negative > 1 or alpha_negative < 0:  #if one of the obtained values of alpha is not between 0 or 1 we simply omit it and go for the other value
                print("the line and the circle intersect at 1 point")
                print(f'{xp},{yp}')
                numberOfIntersectionPoints = 1
                xIntersectionPointOne = xp #i used a different variable to represent intersection points so I am passing it to the one mentioned in the file
                yIntersectionPointOne = yp #same here

            else:
                print("the line and circle intersect at two points")
                print(f'({xp}),({yp}) and ({xn}),({yn})')
                numberOfIntersectionPoints = 2
                xIntersectionPointOne = xp  # same idea as before, changing variables according to what is wanted in the file
                yIntersectionPointOne = yp
                xIntersectionPointTwo = xn
                yIntersectionPointTwo = yn

        ###
# Do NOT change anything below here!
# This is just the starter code and you do not need to understand what is going on here.
# Unless you are curious, of course.
###
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$xc'):
        global xc
        xc = message.content.split("=")[1].strip()
        sendMessageToUser = "Your xc coord is: " + xc
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$yc'):
        global yc
        yc = message.content.split("=")[1].strip()
        sendMessageToUser = "Your yc coord is: " + yc
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$r'):
        global r
        r = message.content.split("=")[1].strip()
        sendMessageToUser = "Your r coord is: " + r
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$x1'):
        global x1
        x1 = message.content.split("=")[1].strip()
        sendMessageToUser = "Your x1 coord is: " + x1
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$y1'):
        global y1
        y1 = message.content.split("=")[1].strip()
        sendMessageToUser = "Your y1 coord is: " + y1
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$x2'):
        global x2
        x2 = message.content.split("=")[1].strip()
        sendMessageToUser = "Your x2 coord is: " + x2
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$y2'):
        global y2
        y2 = message.content.split("=")[1].strip()
        sendMessageToUser = "Your y2 coord is: " + y2
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$solve equation'):
        solveEquation()
        sendMessageToUser = "Equation solved, based on your algorithm 😉. Type **$show results** to see your results!"
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$show results'):
        sendMessageToUserNumberOfIntersections = "There are " + str(numberOfIntersectionPoints) + " total number of intersection points. \n"
        sendMessageToUserFirstIntersectionCoordinates = "The first intersection coordinates are ({:.2f},{:.2f}) \n".format(xIntersectionPointOne, yIntersectionPointOne)
        sendMessageToUserSecondIntersectionCoordinates = "The second intersection coordinates are ({:.2f},{:.2f}) \n".format(xIntersectionPointTwo, yIntersectionPointTwo)
        sendMessageToUser = sendMessageToUserNumberOfIntersections + sendMessageToUserFirstIntersectionCoordinates + sendMessageToUserSecondIntersectionCoordinates
        await message.channel.send(sendMessageToUser)

client.run(TOKEN)


