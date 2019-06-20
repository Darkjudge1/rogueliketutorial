#Part 0 Completed 6/18/2019
#Part 1 in progress.
#Created by John Brunson
#Tutorial located at: http://rogueliketutorials.com/tutorials/tcod/part-1/

import tcod as libtcod
from input_handlers import handle_keys

def main():
    screen_width = 80
    screen_height = 50
    player_x = int(screen_width/2)
    player_y = int(screen_height/2)

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
    	libtcod.console_set_default_foreground(con, libtcod.white)
    	libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)
    	libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
    	libtcod.console_flush()

    	libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)

    	action = handle_keys(key)

    	move = action.get('move')
    	exit = action.get('exit')
    	fullscreen = action.get('fullscreen')

    	if move:
    		dx, dy = move
    		player_x += dx
    		player_y += dy

    	if exit:
    		return True

    	if fullscreen:
    		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
