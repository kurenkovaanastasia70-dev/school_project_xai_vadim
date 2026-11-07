"""Tutor scaffolding tests for lesson 2: the fixed laboratory scene."""

import os
import unittest

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame

pygame.init()
pygame.display.set_mode((1, 1))

from gamestate import GameState
from lab_mode import LAB_LEVEL_ID, LabSession
from main_work import Game


class Lesson02LabScaffoldingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.display.set_mode((1, 1))

    def test_lab_session_starts_unpaused(self):
        session = LabSession()

        self.assertEqual(session.level_id, LAB_LEVEL_ID)
        self.assertTrue(session.updates_enabled)

    def test_open_lab_loads_the_fixed_scene(self):
        game = Game()

        game.open_lab()

        self.assertEqual(game.state, GameState.LAB)
        self.assertEqual(game.current_level_id, LAB_LEVEL_ID)
        self.assertGreater(len(game.walls), 0)
        self.assertGreater(len(game.ghost_manager.ghosts), 0)

    def test_lab_scene_can_render_headlessly(self):
        game = Game()
        game.open_lab()

        game.draw()

        self.assertEqual(game.state, GameState.LAB)


if __name__ == "__main__":
    unittest.main()
