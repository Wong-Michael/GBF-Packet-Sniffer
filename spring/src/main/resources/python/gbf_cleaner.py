import sys
import json
from typing import List
import math
import logging

filter_set = {"loop_damage", "damage", "ability", "attack", "special_npc", "special"}

damage_set = {"loop_damage", "damage"}

normal_atk_set = {'attack', 'special_npc', 'special', 'damage', 'ability', 'effect'}

def clean_file(filepath):
    """
    Takes in a path to a gbf battledata json file and returns a cleaned and filtered list
    of battle info basic on the first command it finds from the list of filter_set.
    It returns a dictionary of the filtered data or an empty string if it does not find
    a 'cmd' value from the filter_set
    """
    with open (filepath) as openFile:
        json_data = json.load(openFile)
        if 'scenario' not in json_data.keys():
            return ""
        # All the data is in the scenario object
        json_data = json_data['scenario']

        # Some fields in this list are not dictionaries so we must filter them out before filtering by command 
        list = [data for data in json_data if isinstance(data, dict) if data["cmd"] in filter_set]

        flat_dict = flat_mapping(list)

        return flat_dict

def flat_mapping(list):
    if len(list) == 0:
        return ""

    # the first cmd denotes the triggering action
    type = list[0]['cmd']

    # ablility based damage
    if type == "ability":
        return ability_dmg_mapping(list)
    # normal attack damage
    elif type == "attack" or type == "special":
        return normal_atk_mapping(list)
    #ignore other types
    else:
        return ""

# In every atk command, any of the normal_atk_set cmds contain important information to track so all must be handled
def normal_atk_mapping(list):
    dict_json = {}
    dict_json['dmg_type'] = "normal_attack"
    list_json = []
    atk_list = [atk for atk in list if atk["cmd"] in normal_atk_set]
    is_extra_damage = False
    extra_damage_pos = 0
    is_CA_burst = False

    for atk in atk_list:
        # Abilities are most of the time followed up by a damage object with their actually values so we must track it between iterations
        if atk['cmd'] == 'ability':
            is_extra_damage = True
            extra_damage_pos = atk['pos'] # to be used for the next atk['cmd'] == 'damage'/'loop_damage' json object in the next iteration
                
        # Charge attack burst damage also follows the same separated style
        elif atk['cmd'] == 'effect':
            if 'burst' in atk['kind']:
                is_CA_burst = True
        
        # Section for parsing attack commands which are the normal attacks
        elif atk['cmd'] == "attack" and atk['from'] == 'player': # we also check from == player because the boss also can have an atk cmd
            attack = {}
            attack['source_pos'] = atk['pos']
            attack['atk_count'] = len(atk['damage'])
            # Guarenteed that there is one damage object and that critical is either true or false
            attack['is_crit'] = atk['damage'][0][0]['critical'] 
            attack['damage'] = 0
            for hits in atk['damage']:
                for hit in hits:
                    attack['damage'] += hit['value']
            list_json.append(attack)

        # Section for charge attacks, the json has 2 values for it so we must check both
        elif atk['cmd'] == 'special_npc' or atk['cmd'] == 'special': 
            attack = {}
            attack['source_pos'] = atk['pos']
            attack['atk_count'] = math.nan
            # Guarenteed that there is one damage object and that critical is either true or false
            attack['is_crit'] = atk['list'][0]['damage'][0]['critical'] 
            attack['damage'] = 0
            for hits in atk['list']:
                for hit in hits['damage']:
                    attack['damage'] += hit['value']
            list_json.append(attack)

        # Section for random damage json objects which the parses has to manually link to a character    
        elif (atk['cmd'] == 'damage' or atk['cmd'] == 'loop_damage') and atk['to'] != 'player':
            for hit in atk["list"]:
                # Sometimes the atk['list'] contains json objects, sometimes the dictionaries 
                # are contained in another array which must be iterated through
                if isinstance(hit, dict):
                    if is_extra_damage:
                        list_json[extra_damage_pos]['damage'] += hit['value']
                        is_extra_damage = False
                    elif is_CA_burst:
                        list_json[0]['damage'] += hit['value']
                        is_CA_burst = False
                    else:
                        # There are quite a few instances where a damage object does not have a related json object 
                        # before it so we default to it being from the character in the first position
                        list_json[0]['damage'] += hit['value'] 
                elif isinstance(hit, List):
                    for nested_hit in hit:
                        if is_extra_damage:
                            list_json[len(list_json)-1]['damage'] += nested_hit['value']
                            is_extra_damage = False
                        elif is_CA_burst:
                            list_json[0]['damage'] += nested_hit['value']
                            is_CA_burst = False
                        else:
                            list_json[0]['damage'] += nested_hit['value'] 

    dict_json['atk_list'] = list_json
    return dict_json

def ability_dmg_mapping(list):
    dict_json = {}
    dict_json['dmg_type'] = "ability"
    dict_json['source_pos'] = list[0]['pos']
    dict_json['ablilty_name'] = list[0]['name']
    dmg_part = [data for data in list if isinstance(data, dict) if data["cmd"] in damage_set]
    dict_json['damage'] = 0
    for hits in dmg_part:
        for hit in hits["list"]:
            if isinstance(hit, dict):
                dict_json['damage'] += hit['value']
            elif isinstance(hit, List):
                for nested_hit in hit:
                    dict_json['damage'] += nested_hit['value']
    return dict_json

# test code
def main():
    json_data_file = sys.argv[1]
    print(clean_file(json_data_file))
        
if __name__ == "__main__":
    main()