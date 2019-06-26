#Part 0 Completed 6/18/2019
#Part 1 Completed 6/18/2019.
#Part 2 in progress
#Created by John Brunson
#Tutorial located at: http://rogueliketutorials.com/tutorials/tcod/part-1/
#TODO: Next version, is it possible to pull these in from a database, JSON, XML, etc.

import tcod as libtcod
from entity import Entity
from input_handlers import handle_keys
from render_functions import render_all, clear_all

def main():
    screen_width = 80
    screen_height = 50
    #instantiate a player
    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    #instatiate a npc.
    npc = Entity(int(screen_width / 2-5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]
   

#input graphics file
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)

    con = libtcod.console_new(screen_width, screen_height)
# Keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()
# Main Game Loop

    while not libtcod.console_is_window_closed():

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        render_all(con, entities, screen_width, screen_height)
        libtcod.console_flush()
        clear_all(con, entities)

 

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player.move(dx,dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()

