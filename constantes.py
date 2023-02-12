import  pygame

BLOCKSIZE = 20

GRID_HEIGHT = 22
GRID_WIDTH = 10
GRIDSURF = GRID_WIDTH*BLOCKSIZE, GRID_HEIGHT*BLOCKSIZE
TOPLEFT_GRID =  50, 50

SUBINFOSURF = (GRID_WIDTH*BLOCKSIZE)-20, (GRID_HEIGHT/6)*BLOCKSIZE
SUBINFOFORME = 4*BLOCKSIZE, 4*BLOCKSIZE
TOPLEFT_INFOS = 300, 50
TOPLEFT_LINE = 310 ,GRID_HEIGHT*BLOCKSIZE*(1/4)
TOPLEFT_SCORE = 310 ,GRID_HEIGHT*BLOCKSIZE*(2/4)
TOPLEFT_FORME = 310, GRID_HEIGHT*BLOCKSIZE*(3/4)


SCREEN_WIDTH = BLOCKSIZE*30
SCREEN_HEIGHT = BLOCKSIZE*30
SIZESCREEN = SCREEN_WIDTH, SCREEN_HEIGHT

BEGIN_SURF = BLOCKSIZE*20, BLOCKSIZE*20
CENTER_BEGIN = SCREEN_HEIGHT//2, SCREEN_WIDTH//2

GRAVITE = 0.4

INIT_X = GRID_WIDTH//2 -2
INIT_Y = 0

On_game = bool

Z = [[
            [1,1,0,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [1,1,0,0],
            [1,0,0,0],
        ]]

S = [[
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
        
        ],
        [
            [0,1,1,0],
            [1,1,0,0],
            [0,0,0,0],
        ]]

L = [[
            [1,0,0,0],
            [1,0,0,0],
            [1,1,0,0],
        
        ],
        [
            [1,1,1,0],
            [1,0,0,0],
            [0,0,0,0],
        ],
        [
            [1,1,0,0],
            [0,1,0,0],
            [0,1,0,0],
        
        ],
        [
            [0,0,1,0],
            [1,1,1,0],
            [0,0,0,0],
        ]]

J = [[
            [0,1,0,0],
            [0,1,0,0],
            [1,1,0,0],
        
        ],
        [
            [1,0,0,0],
            [1,1,1,0],
            [0,0,0,0],
        ],
        [
            [1,1,0,0],
            [1,0,0,0],
            [1,0,0,0],
        
        ],
        [
            [1,1,1,0],
            [0,0,1,0],
            [0,0,0,0],
        ]]

T = [[
            [1,1,1,0],
            [0,1,0,0],
            [0,0,0,0],
        
        ],
        [
            [0,1,0,0],
            [1,1,0,0],
            [0,1,0,0],
        ],
        [
            [0,1,0,0],
            [1,1,1,0],
            [0,0,0,0],
        
        ],
        [
            [1,0,0,0],
            [1,1,0,0],
            [1,0,0,0],
        ]]

I = [[
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0]
        ],
        [
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0]
    ]]

O = [[
            [1,1,0,0],
            [1,1,0,0],
            [0,0,0,0]]]


LISTFORME = [ Z, S, L, J, I, O, T]
LISTECOLFORME = ["Blue", "Green", "Yellow", "Purple", "Red", "Orange", "Pink"]
