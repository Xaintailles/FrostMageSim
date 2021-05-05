# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:09:24 2021

@author: Gebruiker
"""

import utilities as u

sp_frostbolt = u.Spell('frostbolt', 3500, 2.5, 2.5, 2, -1, 'frost', -1, -1, -1)
sp_flurry = u.Spell('flurry', 3500, 2.5, 2.5, 2, -1, 'frost', -1, -1, -1)
sp_frozen_orb =
sp_icelance = 

spells = {'frostbolt': sp_frostbolt
          ,'flurry': sp_flurry
          }

for spell in spells.values():
    spell.charge_reload_time += 1
    print(spell.charge_reload_time)

bu_icyveins = 
bu_lonelywinter = 
bu_fingersorfrost = 
bu_chainreaction = 

p_xaint = u.Player(1950,3500,1200)

h_history = u.History(0,0,1)

sp_frostbolt.cast_spell(h_history,p_xaint)

print(h_history.total_damage)
print(h_history.time)
