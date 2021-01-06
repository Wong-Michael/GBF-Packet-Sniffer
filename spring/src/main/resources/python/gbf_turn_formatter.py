def tabulate(jsonArray):
    """
    Takes in a list of data cleaned with gbf_cleaner and organizes it into a condensed format based on turns.
    Returns a list of arrays containing the values tracked below 
    """
    turn_summaries = []
    turn = 1
    pos_0_dmg = 0
    pos_1_dmg = 0
    pos_2_dmg = 0
    pos_3_dmg = 0
    pos_0_atk_count = 0
    pos_1_atk_count = 0
    pos_2_atk_count = 0
    pos_3_atk_count = 0
    pos_0_crit_count = 0
    pos_1_crit_count = 0
    pos_2_crit_count = 0
    pos_3_crit_count = 0
    for data in jsonArray:
        if data['dmg_type'] == "ability":
            if data['source_pos'] == 0:
                pos_0_dmg += data['damage']
            elif data['source_pos'] == 1:
                pos_1_dmg += data['damage']
            elif data['source_pos'] == 2:
                pos_2_dmg += data['damage']
            elif data['source_pos'] == 3:
                pos_3_dmg += data['damage']
            
        elif data['dmg_type'] == "normal_attack":
            for atk in data['atk_list']:
                if atk['source_pos'] == 0:
                    pos_0_dmg += atk['damage']
                    pos_0_atk_count = atk['atk_count']
                    pos_0_crit_count = int(atk['is_crit'])
                elif atk['source_pos'] == 1:
                    pos_1_dmg += atk['damage']
                    pos_1_atk_count = atk['atk_count']
                    pos_1_crit_count = int(atk['is_crit'])
                elif atk['source_pos'] == 2:
                    pos_2_dmg += atk['damage']
                    pos_2_atk_count = atk['atk_count']
                    pos_2_crit_count = int(atk['is_crit'])
                elif atk['source_pos'] == 3:
                    pos_3_dmg += atk['damage']
                    pos_3_atk_count = atk['atk_count']
                    pos_3_crit_count = int(atk['is_crit'])
            
            turn_summaries.append(
                [
                    turn, 
                    pos_0_dmg, pos_1_dmg, pos_2_dmg,  pos_3_dmg,
                    pos_0_atk_count, pos_1_atk_count, pos_2_atk_count, pos_3_atk_count,
                    pos_0_crit_count, pos_1_crit_count, pos_2_crit_count, pos_3_crit_count
                ]
            )
            turn += 1
            pos_0_dmg = 0
            pos_1_dmg = 0
            pos_2_dmg = 0
            pos_3_dmg = 0
            pos_0_atk_count = 0
            pos_1_atk_count = 0
            pos_2_atk_count = 0
            pos_3_atk_count = 0
            pos_0_crit_count = 0
            pos_1_crit_count = 0
            pos_2_crit_count = 0
            pos_3_crit_count = 0
    if not(pos_0_dmg == pos_1_dmg == pos_2_dmg == pos_3_dmg == 0):
        # fight did not end in an attack so there is some remaining data to collect
        turn_summaries.append(
                [
                    turn, 
                    pos_0_dmg, pos_1_dmg, pos_2_dmg,  pos_3_dmg,
                    pos_0_atk_count, pos_1_atk_count, pos_2_atk_count, pos_3_atk_count,
                    pos_0_crit_count, pos_1_crit_count, pos_2_crit_count, pos_3_crit_count
                ]
            )
    return turn_summaries
    
    