import gc

# Collect all objects
gc.collect()

# Filter objects by class type
def get_objects_by_class(cls):
    return [obj for obj in gc.get_objects() if isinstance(obj, cls)]

# Example usage
weapons_in_memory = get_objects_by_class(Item)

for weapon in weapons_in_memory:
    print(weapon)
