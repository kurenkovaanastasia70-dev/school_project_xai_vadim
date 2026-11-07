"""Minimal, reproducible scene used by the future XAI lessons."""

LAB_LEVEL_ID = "level_1"


class LabSession:
    """Owns laboratory-only state without coupling it to the campaign."""

    def __init__(self, level_id=LAB_LEVEL_ID):
        self.level_id = level_id
        self.paused = False
        self.reset_count = 0

    def enter(self, game):
        """Load the fixed scene every time the laboratory is opened."""
        self.paused = False
        game.load_level_by_id(self.level_id)
        game.reset_player_position()

    @property
    def updates_enabled(self):
        return not self.paused
