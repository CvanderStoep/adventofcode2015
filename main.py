from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Spell:
    name: str
    cost: int
    damage: int = 0
    healing: int = 0
    armor: int = 0
    duration: int = 0
    mana: int = 0


class Player:
    def __init__(self, hitpoints, mana):
        self.hitpoints = hitpoints
        self.mana = mana
        self.armor = 0
        self.effects = {}
        self.mana_spent = 0

    def apply_effects(self):
        expired_effects = []
        for effect in self.effects:
            if effect == "Shield":
                self.armor = 7
            elif effect == "Recharge":
                self.mana += 101
            self.effects[effect] -= 1
            if self.effects[effect] == 0:
                expired_effects.append(effect)
        for effect in expired_effects:
            if effect == "Shield":
                self.armor = 0
            del self.effects[effect]

    def cast_spell(self, spell):
        self.mana -= spell.cost
        self.mana_spent += spell.cost
        if spell.name in ["Magic Missile", "Drain"]:
            return spell.damage, spell.healing
        else:
            self.effects[spell.name] = spell.duration
        return 0, 0


class Boss:
    def __init__(self, hitpoints, damage):
        self.hitpoints = hitpoints
        self.damage = damage


def apply_poison(boss, effects):
    if "Poison" in effects:
        boss.hitpoints -= 3
        effects["Poison"] -= 1
        if effects["Poison"] == 0:
            del effects["Poison"]


def simulate_game(player, boss, spell_sequence):
    turn = 0
    player = deepcopy(player)
    boss = deepcopy(boss)
    for spell in spell_sequence:
        turn += 1
        # Apply effects at the start of the player's turn
        player.apply_effects()
        apply_poison(boss, player.effects)

        if boss.hitpoints <= 0:
            return player.mana_spent

        # Player casts a spell
        if spell.cost > player.mana or (spell.name in player.effects and player.effects[spell.name] > 0):
            return float('inf')
        damage, healing = player.cast_spell(spell)
        boss.hitpoints -= damage
        player.hitpoints += healing

        if boss.hitpoints <= 0:
            return player.mana_spent

        # Apply effects at the start of the boss's turn
        player.apply_effects()
        apply_poison(boss, player.effects)

        if boss.hitpoints <= 0:
            return player.mana_spent

        # Boss attacks
        damage = max(1, boss.damage - player.armor)
        player.hitpoints -= damage
        if player.hitpoints <= 0:
            return float('inf')

    return float('inf')  # If the sequence doesn't finish the boss, it's invalid


# Define spells
spells = [
    Spell("Magic Missile", 53, damage=4),
    Spell("Drain", 73, damage=2, healing=2),
    Spell("Shield", 113, duration=6),
    Spell("Poison", 173, duration=6),
    Spell("Recharge", 229, duration=5)
]


def find_least_mana_sequence(player, boss):
    from itertools import permutations
    best_mana_cost = float('inf')
    best_sequence = []

    for length in range(1, 11):  # Arbitrary max length, can be adjusted
        # print(f'{length= }')
        for spell_sequence in permutations(spells, length):
            mana_cost = simulate_game(player, boss, spell_sequence)
            if mana_cost < best_mana_cost:
                best_mana_cost = mana_cost
                best_sequence = spell_sequence

    return best_mana_cost, best_sequence


# Initialize player and boss
player = Player(hitpoints=50, mana=500)
boss = Boss(hitpoints=71, damage=10)

# Find the least mana sequence
best_mana_cost, best_sequence = find_least_mana_sequence(player, boss)
print(f"Least mana cost: {best_mana_cost}")
print("Best spell sequence:")
for spell in best_sequence:
    print(spell.name)
