#Part 0 Completed 6/18/2019
#Part 1 Completed 6/18/2019.
#Part 2 Completed 6/26/2019
#Part 3 in progress.
#Created by John Brunson
#Tutorial located at: http://rogueliketutorials.com/tutorials/tcod/part-1/
#TODO: Next version, is it possible to pull these in from a database, JSON, XML, etc.
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
import tcod as libtcod
from entity import Entity
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_functions import render_all, clear_all

def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    #tile colors
    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150)
    }

    #instantiate a player
    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    #instatiate a npc.
    npc = Entity(int(screen_width / 2-5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]
   

#input graphics file
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)
#con is the console
    con = libtcod.console_new(screen_width, screen_height)
#game map
    game_map = GameMap(map_width, map_height) 
    #game_map.make_map()
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)
    logging.debug ('Gamemap called from within engine.')
# Keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()
# Main Game Loop

    while not libtcod.console_is_window_closed():

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        render_all(con, entities, game_map, screen_width, screen_height, colors)
        libtcod.console_flush()
        clear_all(con, entities)

 

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y +dy):
                player.move(dx,dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()

