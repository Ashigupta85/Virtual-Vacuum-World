class VacuumWorld:
    def __init__(self, location, room_A_dirty, room_B_dirty):
        self.location = location  # 'A' or 'B'
        self.room_A_dirty = room_A_dirty  # True or False
        self.room_B_dirty = room_B_dirty  # True or False

    def status(self):
        return (self.location, self.room_A_dirty, self.room_B_dirty)

    def is_goal(self):
        return not self.room_A_dirty and not self.room_B_dirty

    def move_left(self):
        if self.location == 'B':
            self.location = 'A'

    def move_right(self):
        if self.location == 'A':
            self.location = 'B'

    def clean(self):
        if self.location == 'A':
            self.room_A_dirty = False
        elif self.location == 'B':
            self.room_B_dirty = False

class ReflexVacuumAgent:
    def act(self, world: VacuumWorld):
        location, room_A_dirty, room_B_dirty = world.status()
        if (location == 'A' and room_A_dirty) or (location == 'B' and room_B_dirty):
            return 'clean'
        elif location == 'A':
            return 'move_right'
        elif location == 'B':
            return 'move_left'

# Example usage:
world = VacuumWorld(location='A', room_A_dirty=True, room_B_dirty=True)
agent = ReflexVacuumAgent()

steps = 0
while not world.is_goal():
    action = agent.act(world)
    print(f"Step {steps}: Location={world.location}, Room A Dirty={world.room_A_dirty}, Room B Dirty={world.room_B_dirty}, Action={action}")
    if action == 'clean':
        world.clean()
    elif action == 'move_left':
        world.move_left()
    elif action == 'move_right':
        world.move_right()
    steps += 1

print(f"All rooms are clean after {steps} steps.")
