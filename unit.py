movement_options = ['infantry', 'mounted', 'armored']

mounted_options = ['horseback', 'wyvernback', 'griffonback']


class Unit:
    def __init__(self, name: str = None, profession: str = None, movement: str = None):
        self.name = name
        self.profession = profession
        self.movement = movement

        if self.name is None:
            raise ValueError("Unit does not have a required value.")

        if self.movement in movement_options:
            pass
        else:
            raise ValueError("Unit has an illegal movement pattern.")
