#UK_Graph_Search.py
#21-2-2023 through 16-3-2023
#Jamison Talley

#imports necessary modules
#Note: all searching algorithms are my own
#implementations. Tkinter and the math library
#are the only aspects of this program that weren't
#created from scratch. Because of this, the program
#should work on any machine with python3 installed
#so long as the supporting python files are in the 
#working directory.

import math
from tkinter import *
from tkinter import font
from dfs import dynamic_matrix_dfs
from bfs import matrix_bfs
from ucs import matrix_ucs
from a_star import matrix_a_star

#defines a function that creates the matrix graph
#that store the edge cost between the cities in the UK
def create_matrix():
    matrix = [
        [0,110,110,170,0,0,0,0,0,0,0],
        [110,0,0,140,0,0,0,0,0,0,0],
        [110,0,0,100,0,0,0,0,0,0,0],
        [170,140,100,0,50,100,0,0,0,0,0],
        [0,0,0,50,0,0,110,0,220,0,0],
        [0,0,0,100,0,0,0,0,120,0,0],
        [0,0,0,0,110,0,0,80,140,0,0],
        [0,0,0,0,0,0,80,0,70,0,0],
        [0,0,0,0,220,120,140,70,0,40,0],
        [0,0,0,0,0,0,0,0,40,0,90],
        [0,0,0,0,0,0,0,0,0,90,0]
    ]
    return matrix

#defines a function that creates the potential,
#or heuristic, values for each city depending on
#the goal city
def create_potentials(goal):
    global coords
    potentials = []
    x_0 = coords[goal][0]
    y_0 = coords[goal][1]
    for i1 in range(len(coords)):
        potentials.append(
            math.sqrt(((coords[i1][0] - x_0) ** 2) +
                      ((coords[i1][1] - y_0) ** 2)
                      )
            )
    return potentials


#defines the function that initializes and starts
#the GUI
def display(cities, coords):
    global endpoints
    global t1
    global t2

    #this creates the window and the items that are seen
    #in the start screen including the opening text and
    #the map of the UK
    endpoints = [None,None]
    window = Tk(className="Northern UK")
    canvas_width = 800
    canvas_height = 800
    canvas = Canvas(window, 
            width=canvas_width,
            height=canvas_height)
    canvas.pack(pady=20)
    img = PhotoImage(file="UK_Image.gif")
    t1 = Label(window, text="Traveling in the north?", foreground="#000000",
               font=font.Font(family='Menlo', size=20))
    t1.place(x=430, y=80)
    t2 = Label(window, text="- Press any key to continue -",
                foreground="black",
                font=font.Font(family='Menlo', size=14))
    t2.place(x=450, y=120)
    canvas.create_image(0,0,anchor=NW,image=img)
    
    #places a square at each of the cities that are included
    #in this program
    for i1 in range(len(cities)):
        canvas.create_rectangle(coords[i1][0],coords[i1][1],
                            coords[i1][0] + 10,coords[i1][1] + 10,
                            outline='#000000',width=2, fill='#edebeb')
    global stage
    stage = 0

    #defines a function that restarts the program
    def restart(key):
        #unbinds previously bound keys 
        window.unbind("<Left>")
        window.unbind("<Right>")
        window.unbind("<h>")

        #obtains global variables
        global roads
        global stops
        global path_text
        global algo_text
        global t1
        global t2
        global t4
        global t5
        global t6
        global t7
        global t8
        global t9
        global t10
        global c1
        global c2
        global cursor
        global stage

        #deletes all of the objects from the previous screen
        for i1 in range(len(roads)):
            canvas.delete(roads[i1])
        for i2 in range(len(stops)):
            canvas.delete(stops[i2])
        for i3 in range(len(path_text)):
            path_text[i3].destroy()
        for i4 in range(4):
            algo_text[i4].destroy()
        canvas.delete(cursor)
        t4.destroy()
        t5.destroy()
        t6.destroy()
        t7.destroy()
        t8.destroy()
        t9.destroy()
        t10.destroy()
        canvas.delete(c1)
        canvas.delete(c2)
        #recreates the opening text
        t1 = Label(window, text="Traveling in the north?", foreground="#000000",
               font=font.Font(family='Menlo', size=20))
        t1.place(x=430, y=80)
        t2 = Label(window, text="- Press any key to continue -",
                foreground="black",
                font=font.Font(family='Menlo', size=14))
        t2.place(x=450, y=120)
        window.unbind("<Escape>")
        stage = 0
        window.bind_all('<Key>', start)
        #restarts the program from the start screen function
        start_screen()
        return
    
    #defines a function that takes the user to a 'help'
    #page with information on the algorithms in this program
    def help(key):
        window.unbind("<Left>")
        window.unbind("<Right>")
        #obtains global variables
        global roads
        global stops
        global path_text
        global algo_text
        global t4
        global t5
        global t6
        global t7
        global t9
        global t10
        global c1
        global c2
        global cursor

        #deletes all of the objects from the previous screen
        for i1 in range(len(roads)):
            canvas.delete(roads[i1])
        for i2 in range(len(stops)):
            canvas.delete(stops[i2])
        for i3 in range(len(path_text)):
            path_text[i3].destroy()
        for i4 in range(4):
            algo_text[i4].destroy()
        canvas.delete(cursor)
        t4.destroy()
        t5.destroy()
        t6.destroy()
        t7.destroy()
        t8.destroy
        canvas.delete(c1)
        canvas.delete(c2)
        t9.place(x=530, y=60)
        t10.place(x=360, y=150)

        window.update()
        window.unbind("<h>")
        return
    

    #defines a function that draws a line from each
    #city to the next in a path from the start city
    #to the goal city, and displays the name of each
    #city in order for the user.
    def write_roads(path):
        #obtains global variables
        global matrix
        global coords
        global roads
        global stops
        global path_text
        global t5

        #deletes any previous road lines and city text
        for i1 in range(len(roads)):
            canvas.delete(roads[i1])
        for i2 in range(len(stops)):
            canvas.delete(stops[i2])
        for i2_1 in range(len(path_text)):
            path_text[i2_1].destroy()
        roads = []
        stops = []
        path_text = []
        cost = 0

        #calculates the total cost of the given path
        for i3 in range(len(path) - 1):
            cost += matrix[path[i3]][path[i3 + 1]]

        #displays said cost for the user
        t5.configure(text="Total Distance: "+str(cost)+" mi")

        #draws lines connecting each of the cities in the path
        #and draws a black square on them
        for i3 in range(len(path) - 1):
            roads.append(canvas.create_line(
                coords[path[i3]][0] + 5,
                coords[path[i3]][1] + 5,
                coords[path[i3 + 1]][0] + 5,
                coords[path[i3 + 1]][1] + 5,
                fill='black',width=5))
            stops.append(canvas.create_rectangle(
                coords[path[i3 + 1]][0],
                coords[path[i3 + 1]][1],
                coords[path[i3 + 1]][0] + 10,
                coords[path[i3 + 1]][1] + 10,
                fill='black', width=2))
            
        #displays the name of each city in the path
        #in order for the user
        for i4 in range(len(path)):
            path_text.append(Label(window,
                    text="{:>10}".format(cities[path[i4]]),
                    foreground="#edebeb",
                    background="black",
                    font=font.Font(family='Menlo', size=16),
                    justify="right",bd=1))
            path_text[i4].place(x=620,y= 290 + (i4 * 25))

        #updates the display, and rebinds the left and right
        #keys, so the user can once again switch the active
        #algorithm. The reason the keys are unbound and then
        #subsequently rebound is to dissalow any possibility
        #of the user activating multiple write_road functions
        #at once.
        window.update()
        window.bind("<Left>", algo_left)
        window.bind("<Right>", algo_right)
        return

    #changes the active searching algorithm left by one
    #utilizing periodic boundary conditions.
    def algo_left(key):
        global algo
        window.unbind("<Left>")
        window.unbind("<Right>")
        algo_text[algo].configure(background='#edebeb', foreground='black')
        algo = (algo - 1) % 4
        algo_text[algo].configure(foreground='#edebeb', background='black')
        # window.update()
        write_roads(paths[algo])
        return
    
    #changes the active searching algorithm right by one
    #utilizing periodic boundary conditions.
    def algo_right(key):
        global algo
        window.unbind("<Left>")
        window.unbind("<Right>")
        algo_text[algo].configure(background='#edebeb', foreground='black')
        algo = (algo + 1) % 4
        algo_text[algo].configure(foreground='#edebeb', background='black')
        # window.update()
        write_roads(paths[algo])
        return

    #defines the function that displays the results with the given
    #user input
    def output_screen():
        global coords
        global t3,t4,t5,t6,t7,t8,t9,t10
        global algo_text
        global city_text
        global path_text
        global cursor
        global endpoints
        global roads
        global stops
        global matrix
        global paths
        global algo
        start = endpoints[0]
        goal = endpoints[1]
        canvas.itemconfig(cursor, fill='#edebeb')
        t3.configure(foreground='#edebeb')
        for i1 in range(len(city_text)):
            city_text[i1].configure(foreground='#edebeb',
                                    background='#edebeb')
            
        #takes the user input and runs it through the searching
        #algorithms to get their respective paths
        matrix = create_matrix()
        potentials = create_potentials(goal)
        dfs_res = dynamic_matrix_dfs(matrix,start, goal)
        bfs_res = matrix_bfs(matrix,start, goal)
        ucs_res = matrix_ucs(matrix,start,goal)
        a_star_res = matrix_a_star(matrix,potentials,start,goal)
        paths = [a_star_res,ucs_res,bfs_res,dfs_res]
        roads = []
        stops = []
        
        #creates the text for this screen
        path_text = []
        algos = [" A * ", " UCS ", " BFS ", " DFS "]
        algo = 0
        algo_text = []
        for i2 in range(4):
            algo_text.append(Label(window,
                    text=algos[i2],
                    foreground="#000000",
                    font=font.Font(family='Menlo', size=17),
                    justify="right",bd=1))
            algo_text[i2].place(x=445 + (i2 * 75),y= 130)
        algo_text[0].configure(foreground='#edebeb',
                               background='black')
        t4 = Label(window, text="Active Searching Algorithm",
                    foreground="#000000",
                    font=font.Font(family='Menlo', size=20))
        t4.place(x=425, y=80)
        t5 = Label(window, text="Total Distance: 0 km",
                    foreground="#000000",
                    font=font.Font(family='Menlo', size=16))
        t5.place(x=470, y=170)
        t6 = Label(window, text="Route:",
            foreground="#000000",
            font=font.Font(family='Menlo', size=20))
        t6.place(x=650, y=250)
        t7 = Label(window, text=
                   "Press 'h' for more information about this program",
                    foreground="#000000",
                    font=font.Font(family='Menlo', size=11))
        t7.place(x=430, y=700)
        t8 = Label(window, text=
                   "                           Press 'esc' to restart",
                    foreground="#000000",
                    font=font.Font(family='Menlo', size=11))
        t8.place(x=430, y=720)

        #creates the text for the help screen, but doesn't place it.
        #This could have been done in a later function, but it doesn't
        #make much of a difference either way
        t9 = Label(window,text=
            "This program utilizes 4 algorithms:\n"+
            "A Star (A *)\n Uniform Cost Search (UCS)\n"+
            "Breadth First Search (BFS)\n Depth First Search (DFS)",
                    foreground="#000000",
                    font=font.Font(family='Menlo', size=12),
                    justify="right",bd=1)
        expln = (
    """BFS and DFS are both cost blind searching algorithms
    meaning they don't account for the travel cost
    between cities. Because of this, they may not result
    in the fastest route between two cities. UCS is a
    variation on Dijkstra's algorithm that finds the
    lowest cost path between two nodes. This will always
    produce the shortest path between the specified cities,
    but it will do so relatively inefficiently. The A*
    algorithm expands on this process by utilizing
    environment information to make informed decisions
    on which paths to explore first. The result is more
    time efficient method to find the shortest path.
    If the environment information is inaccurate,
    however, A* may not correctly find the shortest path,
    hence why the inclusion of UCS is necessary.""")
        t10 = Label(window,text=expln,
                    foreground="#000000",
                    font=font.Font(family='Menlo', size=12),
                    justify="right",bd=1)
        write_roads(a_star_res)

        return


    #creates a function that handles the '<Enter>' key event
    #when the user is selecting their start and end cities.
    def add_city(key):
        global t3
        global endpoints
        global stage
        global index
        global c1, c2
        if stage == 1:
            endpoints[0] = index
            t3.configure(text="  Select the ending city")
            c1 = canvas.create_rectangle(
                coords[index][0],coords[index][1],
                coords[index][0] + 10,coords[index][1] + 10,
                fill='black', width=2)
            canvas.itemconfig(cursor, fill='black')
            window.update()
        elif stage == 2:
            endpoints[1] = index
            c2 = canvas.create_rectangle(
                coords[index][0],coords[index][1],
                coords[index][0] + 10,coords[index][1] + 10,
                fill='black', width=2)
            window.bind('<Escape>', restart)
            window.bind('<h>', help)
            window.unbind('<Up>')
            window.unbind('<Down>')
            output_screen()
        window.update()
        stage += 1

    #defines two functions that allow the user to maneuver up and
    #down through the list of cities to pick the start and end 
    #locations. These functions also update the location of the
    #'cursor' (the black square that indicates which city is selected)
    #the functions also update the highlighted text of the list of cities

    def up_city_1(key):
        global index
        global cursor
        global endpoints
        if (index > 0) and (index - 1 != endpoints[0]):
            city_text[index].configure(foreground='black',
                                    background='#edebeb')
            index -= 1
            city_text[index].configure(foreground='#edebeb',
                                    background='black')
            canvas.coords(cursor,coords[index][0],
                                coords[index][1],
                                coords[index][0] + 10,
                                coords[index][1] + 10)
            canvas.itemconfig(cursor, fill='black')
        elif index > 1:
            city_text[index].configure(foreground='black',
                background='#edebeb')
            index -= 1
            up_city_1(key)
        window.update()
    
    def down_city_1(key):
        global endpoints
        global index
        global cursor
        if (index < 10) and ((index + 1) != endpoints[0]):
            city_text[index].configure(foreground='black',
                                    background='#edebeb')
            index += 1
            city_text[index].configure(foreground='#edebeb',
                                    background='black')
            canvas.coords(cursor,coords[index][0],
                                coords[index][1],
                                coords[index][0] + 10,
                                coords[index][1] + 10)
            canvas.itemconfig(cursor, fill='black')
        elif index < 9:
            city_text[index].configure(foreground='black',
                background='#edebeb')
            index += 1
            down_city_1(key)
        window.update()

    #defines a function that makes the 'cursor' square
    #blink while the user is selecting cities.
    def c_blink(x=True):
        global stage
        if x == True:
            x = False
            canvas.itemconfig(cursor, fill='#edebeb')
            city_text
        else:
            canvas.itemconfig(cursor, fill='black')
            x = True
        window.update()
        if stage <= 2:
            window.after(700, c_blink, x)


    #defines a function that handles the stage in which the
    #user is selecting starting and ending cities. This includes
    #creating the objects and text, and calling the cursor blink
    #function
    def select_city_1():
        global t3
        global stage
        global cursor
        global index
        global city_text
        index = 0
        t3 = Label(window, text="Select the starting city",
                    foreground="#000000",
                    font=font.Font(family='Menlo', size=20))
        t3.place(x=430, y=80)
        cursor = canvas.create_rectangle(
                coords[index][0],coords[index][1],
                coords[index][0] + 10,coords[index][1] + 10,
                fill='black', width=2)
        city_text = []
        for i1 in range(11):
            city_text.append(Label(window,
                    text="{:>10}".format(cities[i1]),
                    foreground="#000000",
                    font=font.Font(family='Menlo', size=17),
                    justify="right",bd=1))
            city_text[i1].place(x=597,y= 130 + (i1 * 25))
        city_text[0].configure(foreground='#edebeb',
                               background='black')
        window.update()
        c_blink()
        

    #defines a function that starts the meat of the program
    #once the user has hit a key
    def start(key):
        global stage
        stage = 1
        t1.place(x=1000,y=1000)
        t2.place(x=1000,y=1000)
        window.unbind_all('<Key>')
        window.bind('<Up>', up_city_1)
        window.bind('<Down>', down_city_1)
        window.bind('<Return>', add_city)
        select_city_1()
    

    #defines a function that displays the start screen
    #and animates the 'press any key to continue' text
    def start_screen():
        global stage
        t1.place(x=430, y=80)
        t2.place(x=450, y=120)
        def t2_blink(x=True):
            global stage
            if x == True:
                x = False
                t2.configure(foreground='#edebeb')
            else:
                t2.configure(foreground='black')
                x = True
            window.update()
            if stage == 0:
                window.after(700, t2_blink, x)
        t2_blink()
            
    window.bind_all('<Key>', start)
    window.after(5, start_screen)
    window.mainloop()

#creates a main function for the program to call the display function
#in hindsight, this could have been rolled into the display function
def main():
    global coords
    global cities
    cities = ["Iverness", "Aberdeen", "Oban", "Glasgow",
              "Edinburgh", "Carlisle","Newcastle", "York", 
              "Manchester", "Liverpool", "Holyhead"]
    coords = [[225,170],[300,180],[190,235],[220,270],[265,270],
              [275,335],[330,330],[345,400],[315,440],[282,432],
              [215,450]]
    display(cities, coords)


main()