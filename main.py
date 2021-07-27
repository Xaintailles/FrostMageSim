# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:09:24 2021

@author: Gebruiker
"""

import utilities as u
import random

sp_frostbolt = u.Spell('frostbolt', 3500, 2.5, 2.5, 2, -1, 'frost', -1, -1, -1)
sp_flurry = u.Spell('flurry', 3500, 2.5, 2.5, 2, -1, 'frost', -1, -1, -1)
sp_icelance = u.Spell('icelance', 3500, 2.5, 2.5, 2, -1, 'frost', -1, -1, -1)

spells = {'frostbolt': sp_frostbolt
          ,'flurry': sp_flurry
          }

bu_icyveins = u.Buff(present = False
                     ,base_duration = 30000
                     ,present_duration = 0
                     ,max_charges = 1
                     ,current_charges = 0
                     ,effect = {})
bu_lonelywinter = u.Buff(present = False
                     ,base_duration = -1
                     ,present_duration = 0
                     ,max_charges = 1
                     ,current_charges = 0
                     ,effect = {})
bu_fingersoffrost = u.Buff(present = False
                     ,base_duration = 15000
                     ,present_duration = 0
                     ,max_charges = 2
                     ,current_charges = 0
                     ,effect = {})
bu_chainreaction = u.Buff(present = False
                     ,base_duration = 10000
                     ,present_duration = 0
                     ,max_charges = 5
                     ,current_charges = 0
                     ,effect = {})
bu_brainfreeze = u.Buff(present = False
                     ,base_duration = 15000
                     ,present_duration = 0
                     ,max_charges = 1
                     ,current_charges = 0
                     ,effect = {})
bu_winterchill = u.Buff(present = False
                     ,base_duration = 6000
                     ,present_duration = 0
                     ,max_charges = 2
                     ,current_charges = 0
                     ,effect = {})

p_xaint = u.Player(1950,3500,1200)

h_history = u.History(0,0,1)


while h_history.time <= 600:
    
    if bu_brainfreeze.present:
        print('casting flurry')
        sp_flurry.cast_spell(h_history,p_xaint)
        bu_winterchill.current_charges += 2
        bu_brainfreeze.present = False
        continue
    
    elif bu_winterchill.current_charges > 0:
        print('casting IceLance winterchill')
        sp_icelance.cast_spell(h_history,p_xaint)
        bu_winterchill.current_charges -= 1
        if bu_fingersoffrost.current_charges > 0:
            bu_fingersoffrost.current_charges -= 1
        continue
    
    elif bu_fingersoffrost.current_charges > 0:
        print('casting IceLance FoF')
        sp_icelance.cast_spell(h_history,p_xaint)
        bu_fingersoffrost.current_charges -= 1
        if bu_winterchill.current_charges > 0:
            bu_winterchill.current_charges -= 1
        continue
        
    else:
        print('casting frostbolt')
        sp_frostbolt.cast_spell(h_history,p_xaint)
        
        #We check if we generated FoF proc
        if bu_fingersoffrost.current_charges >= bu_fingersoffrost.max_charges:
            continue
        elif random.randrange(0,10000) <= 1500:
            bu_fingersoffrost.current_charges += 1
            
        #we check if we generated a brainfreeze proc
        if random.randrange(0,10000) <= 3000:
            bu_brainfreeze.present = True
        
        continue
    
print('dps is %s' % (str(h_history.total_damage / h_history.time)))




bu_icyveins = u.Buff(present = 0
                 ,base_duration = 30
                 ,current_duration = 0
                 ,max_charges = 1
                 ,current_charges = 0
                 ,effect = [])

print(bu_icyveins.present)
bu_icyveins.refresh_buff()

print(bu_icyveins.current_duration)
    

        
    
