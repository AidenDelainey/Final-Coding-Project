import pygame

class Item:
    def __init__(self, name, description, item_type, stat_bonus=None):
        self.name = name
        self.description = descriptoin
        self.type = item_type
        self.stat_bonus = stat_bonus or {}
        self.quantity = 1
        

class Inventory:
    def __init__(self, player):
        self.player = player
        self.items = []
        self.selected_index = 0
        self.scroll_offset = 0
        self.max_visible = 8

    def add_item(self, item):
        for inv_item in self.items:
            if inv_item.name == item.name:
                inv_item.quantity += 1
                return
        self.items.append(item)

    def use_selected(self):
        if not self.items:
            return

        item = self.items[self.selected_index]

        if item.type in ["weapon", "accessory", "spell"]:
            equipped = self.player.equip(item)
            if equipped:
                print(f"Equipped {item.name}")
        elif item.type == "consumable":
            print(f"Used {item.name}")
            item.quantity -= 1
            if item.quantity <= 0:
                self.items.remove(item)
