import tcod as libtcod

def handle_keys(key):
	if key.vk == libtcod.KEY_UP:
		return {'move': (0, -1)}
	elif key.vk == libtcod.KEY_DOWN:
		return {'move': (0, 1)}
	elif key.vk == libtcod.KEY_LEFT:
		return {'move': (-1, 0)}
	elif key.vk == libtcod.KEY_RIGHT:
		return {'move': (1, 0)}

	if key.vk == libtcod.KEY_ENTER and key.lalt:
# If both left alt and enter are pressed at the same time...
		return{'fullscreen': True}
#Exit the Game
	elif key.vk == libtcod.KEY_ESCAPE:
		return{'exit': True}

# No Key was pressed
	return {}