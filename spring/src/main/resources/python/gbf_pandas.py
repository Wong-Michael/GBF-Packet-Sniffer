import numpy as np
import pandas as pd

def get_statistics(arr):
    numpy_data = np.array(arr)
    df = pd.DataFrame(data=numpy_data, columns=['turn', 
                    'pos_0_dmg', 'pos_1_dmg', 'pos_2_dmg',  'pos_3_dmg',
                    'pos_0_atk_count', 'pos_1_atk_count', 'pos_2_atk_count', 'pos_3_atk_count',
                    'pos_0_crit_count', 'pos_1_crit_count', 'pos_2_crit_count', 'pos_3_crit_count'])
    df['total_damage'] = df['pos_0_dmg'] + df['pos_1_dmg'] + df['pos_2_dmg'] + df['pos_3_dmg']
    
    pos_0_total = df['pos_0_dmg'].sum()
    pos_1_total = df['pos_1_dmg'].sum()
    pos_2_total = df['pos_2_dmg'].sum()
    pos_3_total = df['pos_3_dmg'].sum()
    pos_0_count_avg = df['pos_0_atk_count'].mean()
    pos_1_count_avg = df['pos_1_atk_count'].mean()
    pos_2_count_avg = df['pos_2_atk_count'].mean()
    pos_3_count_avg = df['pos_3_atk_count'].mean()
    pos_0_avg = df['pos_0_dmg'].mean()
    pos_1_avg = df['pos_1_dmg'].mean()
    pos_2_avg = df['pos_2_dmg'].mean()
    pos_3_avg = df['pos_3_dmg'].mean()
    pos_0_avg_crit = df['pos_0_crit_count'].mean()
    pos_1_avg_crit = df['pos_1_crit_count'].mean()
    pos_2_avg_crit = df['pos_2_crit_count'].mean()
    pos_3_avg_crit = df['pos_3_crit_count'].mean()
    
    return f"pos_0_total:{pos_0_total} pos_1_total:{pos_1_total} pos_2_total:{pos_2_total} pos_3_total:{pos_3_total} "\
        f"pos_0_count_avg:{pos_0_count_avg} pos_1_count_avg:{pos_1_count_avg} pos_2_count_avg:{pos_2_count_avg} pos_3_count_avg:{pos_3_count_avg} "\
        f"pos_0_avg:{pos_0_avg} pos_1_avg:{pos_1_avg} pos_2_avg:{pos_2_avg} pos_3_avg:{pos_3_avg} "\
        f"pos_0_avg_crit:{pos_0_avg_crit} pos_1_avg_crit:{pos_1_avg_crit} pos_2_avg_crit:{pos_2_avg_crit} pos_3_avg_crit:{pos_3_avg_crit} "\
