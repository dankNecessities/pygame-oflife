import pygame, random, unittest
from pygame.locals import *
from sys import exit

def random_boolean():
    """Generates a random boolean value"""
    i = int(random.random()*10)
    return True if i % 2 else False

def new_gol_grid(size):
    """Initializes a grid with random boolean states at each index"""
    gol_grid = []
    for x in range(size[0]):
        gol_grid.append([])
        for y in range(size[1]):
            gol_grid[x].append(random_boolean())

    return gol_grid

def update_g_list(g_list, position, value):
    """Overwrites a value at a specific point in a grid"""
    if (len(g_list) < (position[0] - 1)):
        print('Position at x:{} for {} does not exist in list'.format(position[0]))
        exit()

    for i in g_list:
        if (len(i) < position[1] - 1):
            print('Position at y:{} does not exist in list'.format(position[1]))
            exit()

    old_item = g_list[position[0]][position[1]]
    g_list[position[0]].remove(old_item)
    g_list[position[0]].insert(position[1], value)
    return g_list

def check_neighbours_state(object_grid, object_position):
    """Counts the number of alive or dead neighbours for a cell
    NOTE: This program only checks neighbour states for (A x B) size grids"""
    alive_neighbours = 0
    dead_neighbours = 0
    x = object_position[0]
    y = object_position[1]
    
    if (len(object_grid) < (x - 1)):
        print('Position at x:{} does not exist in list'.format(x))
        exit()

    for i in object_grid:
        if len(object_grid) < (y - 1):
            print('Position at y:{} does not exist in list'.format(y))
            exit()

    x_plus = x + 1
    y_plus = y + 1
    x_minus = x - 1
    y_minus = y - 1
    
    if x == 0: 
        if y == 0:
            right_up_neighbour = object_grid[x_plus][-1]
            up_neighbour = object_grid[x][-1]
            left_up_neighbour = object_grid[-1][-1]
            left_neighbour = object_grid[-1][y]
            left_down_neighbour = object_grid[-1][y_plus]

            down_neighbour = object_grid[x][y_minus]
            right_down_neighbour = object_grid[x_plus][y_minus]
            right_neighbour = object_grid[x_plus][y]
        elif y == (len(object_grid[0]) - 1):
            right_down_neighbour = object_grid[x_plus][0]
            down_neighbour = object_grid[x][0]
            left_down_neighbour = object_grid[-1][0]
            left_neighbour = object_grid[-1][y]
            left_up_neighbour = object_grid[-1][y_minus]

            up_neighbour = object_grid[x][y_minus]
            right_up_neighbour = object_grid[x_plus][y_minus]
            right_neighbour = object_grid[x_plus][y]
        else:
            left_up_neighbour = object_grid[-1][y_minus]
            left_neighbour = object_grid[-1][y]
            left_down_neighbour = object_grid[-1][y_plus]

            up_neighbour = object_grid[x][y_plus]
            right_up_neighbour = object_grid[x_plus][y_plus]
            right_neighbour = object_grid[x_plus][y]
            right_down_neighbour = object_grid[x_plus][y_minus]
            down_neighbour = object_grid[x][y_minus]
            
    elif x == (len(object_grid) - 1):
        if y == 0:
            left_up_neighbour = object_grid[x_minus - 1][-1]
            up_neighbour = object_grid[x_minus][-1]
            right_up_neighbour = object_grid[0][-1]
            right_neighbour = object_grid[0][y]
            right_down_neighbour = object_grid[0][y_plus]

            down_neighbour = object_grid[x][y_minus]
            left_down_neighbour = object_grid[x_minus][y_minus]
            left_neighbour = object_grid[x_minus][y]
        elif y == (len(object_grid[0]) - 1):
            right_up_neighbour = object_grid[0][y_minus]
            right_neighbour = object_grid[0][y]
            right_down_neighbour = object_grid[0][0]
            down_neighbour = object_grid[x][0]
            left_down_neighbour = object_grid[x_minus][0]

            left_neighbour = object_grid[x_minus][y]
            left_up_neighbour = object_grid[x_minus][y_minus]
            up_neighbour = object_grid[x][y_minus]
        else:
            right_up_neighbour = object_grid[0][y_plus]
            right_neighbour = object_grid[0][y]
            right_down_neighbour = object_grid[0][y_minus]

            left_up_neighbour = object_grid[x_minus][y_plus]
            up_neighbour = object_grid[x][y_plus]
            down_neighbour = object_grid[x][y_minus]
            left_down_neighbour = object_grid[x_minus][y_minus]
            left_neighbour = object_grid[x_minus][y]    
                           
    elif y == (len(object_grid[0]) - 1):
        right_down_neighbour = object_grid[x_plus][0]
        down_neighbour = object_grid[x][0]
        left_down_neighbour = object_grid[x_minus][0]

        left_up_neighbour = object_grid[x_minus][y]
        up_neighbour = object_grid[x][y_minus]
        right_up_neighbour = object_grid[x_plus][y]
        right_neighbour = object_grid[x_plus][y_minus]    
        left_neighbour = object_grid[x_minus][y_minus]
            
    elif y == 0:
        left_up_neighbour = object_grid[x_minus][-1]
        up_neighbour = object_grid[x_minus][-1]
        right_up_neighbour = object_grid[x_plus][-1]

        right_neighbour = object_grid[x_plus][y]
        right_down_neighbour = object_grid[x_plus][y_minus]
        down_neighbour = object_grid[x][y_minus]
        left_down_neighbour = object_grid[x_minus][y_minus]
        left_neighbour = object_grid[x_minus][y]

    else:
        left_up_neighbour = object_grid[x_minus][y_plus]
        up_neighbour = object_grid[x][y_plus]
        right_up_neighbour = object_grid[x_plus][y_plus]
        right_neighbour = object_grid[x_plus][y]
        right_down_neighbour = object_grid[x_plus][y_minus]
        down_neighbour = object_grid[x][y_minus]
        left_down_neighbour = object_grid[x_minus][y_minus]
        left_neighbour = object_grid[x_minus][y]

    if up_neighbour == True:
        alive_neighbours += 1
    else:
        dead_neighbours += 1

    if right_up_neighbour == True:
        alive_neighbours += 1
    else:
        dead_neighbours += 1

    if right_neighbour == True:
        alive_neighbours += 1
    else:
        dead_neighbours += 1

    if right_down_neighbour == True:
        alive_neighbours += 1
    else:
        dead_neighbours += 1

    if down_neighbour == True:
        alive_neighbours += 1
    else:
        dead_neighbours += 1

    if left_down_neighbour == True:
        alive_neighbours += 1
    else:
        dead_neighbours += 1

    if left_neighbour == True:
        alive_neighbours += 1
    else:
        dead_neighbours += 1

    if left_up_neighbour == True:
        alive_neighbours += 1
    else:
        dead_neighbours += 1

    cell_neighbours = (alive_neighbours, dead_neighbours)
    return cell_neighbours

def renew_or_kill_cell(cell_grid, cell_position):
    """Changes the state of a cell basing on neighbours' properties"""
    print(cell_grid)

    cell_state = cell_grid[cell_position[0]][cell_position[1]]
    neighbours_state = check_neighbours_state(cell_grid, cell_position)
    alive_neighbours = neighbours_state[0]
    dead_neighbours = neighbours_state[1]

    if cell_state == True and alive_neighbours > 3:
        updated_grid = update_g_list(cell_grid, cell_position, False)
        return updated_grid

    elif cell_state == True and alive_neighbours < 2:
        updated_grid = update_g_list(cell_grid, cell_position, False)
        return updated_grid

    elif cell_state == True and alive_neighbours == 2 or alive_neighbours == 3:
        updated_grid = cell_grid
        return updated_grid

    elif cell_state == False and alive_neighbours == 3:
        updated_grid = update_g_list(cell_grid, cell_position, True)
        return updated_grid
    
    else:
        return cell_grid

def draw_grid(size, images):
    #UNTESTED
    p_list = new_gol_grid(size)
    l_image = pygame.image.load(images[0])
    d_image = pygame.image.load(images[1])
    
    i = l_image.get_width()
    j = l_image.get_height()

    m = d_image.get_width()
    n = d_image.get_height()

    for x in range(size[0]):
        for y in range(size[1]):
            p_list = renew_or_kill_cell(p_list, (x, y))
            if p_list[x][y] == True:
                screen.blit(l_image, (x*i, y*j))
            else:
                screen.blit(d_image, (x*m, y*n))

#Start of program
pygame.init()
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

while True:
    time_passed = clock.tick() / 1000.0
    frame_load_time = 0.5

    while time_passed < frame_load_time:
        time_passed += clock.tick() / 1000.0
        print(time_passed)

    for event in pygame.event.get():

        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()

    draw_grid((10, 10), ('bib.png', 'bib2.png'))

    pygame.display.update()

class gol_tests(unittest.TestCase):

    def test_random_boolean(self):
        x = random_boolean()
        if x != None:
            x = True
        self.assertEqual(x, True)

    def test_new_gol_grid(self):
        test_size = (5, 5)
        y = new_gol_grid(test_size)
        self.assertEqual(test_size[0], len(y[0]))
        self.assertEqual(test_size[1], len(y[1]))

    def test_update_g_list(self):
        z_list = [[True, False],[True, True, False],[False, True]]  
        new_z_list = update_g_list(z_list, (2, 1), False)
        self.assertEqual(new_z_list[2][1], False)

    def test_check_neighbours_state(self):
        h_list = [[True, True], 
                  [True, False],
                  [False, True], 
                  [False, False]]
        tstate = check_neighbours_state(h_list, (1,1))
        self.assertEqual((tstate[0] + tstate[1]), 8)

    def test_renew_or_kill_cell(self):
        f_list = [[True, True, False],
                  [False, True, True],
                  [True, False, False],
                  [False, True, True]]
        new_f_list = renew_or_kill_cell(f_list, (1, 1))
        self.assertEqual(new_f_list[1][1], False)

if __name__ == '__main__':
    unittest.main()
