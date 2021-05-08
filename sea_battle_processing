from functools import reduce
def sea_battle_processing(size_of_map: int, ship_positions: str, hit_positions: str) -> str:
    hit_positions_list = set(hit_positions.split(' '))
    
    def is_sunken_or_hitted(ship_start: str, ship_end: str) -> 'sunken' or 'hitted' or 'whole':
        y_end, y_start, x_end, x_start = int(ship_end[:-1]), int(ship_start[:-1]), ord(ship_end[-1].upper()), ord(ship_start[-1].upper())
        ship_parts = set(str(i) + chr(j) for i in range(y_start, y_end+1) for j in range(x_start, x_end+1))
        saved_ship_parts = ship_parts - hit_positions_list
        if len(ship_parts) > len(saved_ship_parts) > 0:
            return 'hitted'
        elif len(saved_ship_parts) == 0:
            return 'sunken'
        else:
            return 'whole'
        
    
    def sum_sunken_hitted_ships(previous_ship, next_ship) -> (int, int):
        return previous_ship[0] + (next_ship == 'sunken'), previous_ship[1] + (next_ship == 'hitted')
        
    sunken_or_hitted_ships = (is_sunken_or_hitted(*ship.split(' ')) for ship in ship_positions.split(','))
    
    sunken_ships, hitted_ships = reduce(sum_sunken_hitted_ships, sunken_or_hitted_ships, (0, 0))
    
    return f'{sunken_ships},{hitted_ships}'
