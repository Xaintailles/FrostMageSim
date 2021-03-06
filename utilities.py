# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:12:38 2021

@author: Gebruiker
"""

import random

def random_generation() -> int:
    return random.randrange(0,10000)



# %% Classes
class Player:
    def __init__(self,spell_power
                 ,crit_rating
                 ,haste_rating):
        
        self.spell_power = spell_power
        self.crit_rating = crit_rating
        self.haste_rating = haste_rating
        
class History:
    def __init__(self,time,total_damage,gcd):
        self.time = time
        self.total_damage = total_damage
        self.gcd = gcd  

class Spell:
    def __init__(self,name
                 ,crit_chance
                 ,spell_power_modifier
                 ,cast_time
                 ,crit_modifier
                 ,cooldown,school
                 ,max_charges
                 ,current_charges
                 ,charge_reload_time):
        
        self.name = name
        self.crit_chance = crit_chance
        self.spell_power_modifier = spell_power_modifier
        self.cast_time = cast_time
        self.crit_modifier = crit_modifier
        self.cooldown = cooldown
        self.school = school
        self.max_charges = max_charges
        self.current_charges = current_charges
        self.charge_reload_time = charge_reload_time
        
    def cast_spell(self,history: History
                   ,player: Player):
        spell_base_damage = self.spell_power_modifier * player.spell_power
        crit_bol = random_generation() <= player.crit_rating
        history.total_damage += spell_base_damage + (spell_base_damage * self.crit_modifier * crit_bol)
        history.time += self.cast_time
        
        if self.current_charges > 0:
            self.current_charges -= 1
        
        
class Buff:
    def __init__(self,present
                 ,base_duration
                 ,current_duration
                 ,max_charges
                 ,current_charges
                 ,proc_chance
                 ,effect: dict):
        self.present = present
        self.base_duration = base_duration
        self.current_duration = current_duration
        self.max_charges = max_charges
        self.current_charges = current_charges
        self.proc_chance = proc_chance
        self.effect = effect
            
    def refresh_buff(self):
        self.present = 1
        self.current_duration = self.base_duration
    
    def update_duration(self, elapsed_time: int):
        self.current_duration += elapsed_time
        
    def update_stacks(self):
        self.refresh_buff()
        if self.current_charges < self.max_charges:
            self.current_charges += 1
            
    def global_update(self):
        

            
        
          
        
# %% functions

def cast_spell(player: Player
               , spell: Spell
               , history: History
               , heating_up: Buff
               , hot_streak: Buff):

    damage = spell.spell_power_modifier * player.spell_power
    roll = random_generation()
    
    if spell.charges > 0:
        spell.charges -= 1
       
    if spell.crit_chance >= roll: ## it's a crit

        damage = damage * spell.crit_modifier
        
        if spell.name == 'fireball':
            spell.crit_chance = player.crit_rating
        
        ## checking up and updating heatingup and hotstreak
        if heating_up.present:
            hot_streak.present = True
            heating_up.present = False
        elif spell.school == 'fire' and not(hot_streak.present):
            heating_up.present = True
            
    else:
        if spell.name == 'fireball':
            spell.crit_chance += 1000
    
    history.total_damage += damage
    history.time += spell.cast_time

























