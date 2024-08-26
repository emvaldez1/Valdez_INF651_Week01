
import random

class Player:
    def __init__(self, name):
        """Initialize the player with a name, health, attack power, defense, experience, and level."""
        self.name = name
        self.health = 100
        self.attack_power = 10
        self.defense = 5
        self.experience = 0
        self.level = 1

    def attack(self, enemy):
        """Calculate and apply damage to the enemy."""
        damage = max(self.attack_power - enemy.defense, 0)
        enemy.health -= damage
        return damage

    def take_damage(self, damage):
        """Reduce the player's health by the damage amount."""
        self.health -= damage

    def is_alive(self):
        """Check if the player is still alive."""
        return self.health > 0

    def level_up(self):
        """Increase player's level, attack power, defense, and restore health."""
        self.level += 1
        self.attack_power += 5
        self.defense += 3
        self.health = 100  # Restore health on level up
        print(f"{self.name} leveled up to level {self.level}!")

class Enemy:
    def __init__(self, name, health, attack_power, defense, exp_points):
        """Initialize the enemy with a name, health, attack power, defense, and experience points."""
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.exp_points = exp_points

    def attack(self, player):
        """Calculate and apply damage to the player."""
        damage = max(self.attack_power - player.defense, 0)
        player.health -= damage
        return damage

    def is_alive(self):
        """Check if the enemy is still alive."""
        return self.health > 0

def combat(player, enemy):
    """Handle the fight between the player and an enemy."""
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        player_damage = player.attack(enemy)
        print(f"{player.name} attacks {enemy.name} for {player_damage} damage.")
        if not enemy.is_alive():
            print(f"{enemy.name} is defeated!")
            player.experience += enemy.exp_points
            if player.experience >= 100:
                player.level_up()
                player.experience = 0  # Reset experience after leveling up
            break
        enemy_damage = enemy.attack(player)
        print(f"{enemy.name} attacks {player.name} for {enemy_damage} damage.")
        if not player.is_alive():
            print(f"{player.name} has been defeated...")

def main():
    """Main function to start the game, create the player and handle the game loop."""
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    # List of enemies
    enemies = [
        Enemy("Goblin", 30, 5, 2, 20),
        Enemy("Orc", 50, 10, 5, 50),
        Enemy("Dragon", 100, 20, 10, 100)
    ]

    # Game loop
    while player.is_alive():
        command = input("Do you want to explore or rest? (explore/rest): ").lower()
        if command == "explore":
            enemy = random.choice(enemies)
            combat(player, enemy)
        elif command == "rest":
            player.health = 100
            print(f"{player.name} rests and recovers to full health.")
        else:
            print("Invalid command.")

    print("Game Over")

# Directly call main() function to start the game
main()
