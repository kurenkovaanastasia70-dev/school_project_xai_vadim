"""Tutor scaffolding tests for lesson 2: the fixed laboratory scene."""

import os
import unittest

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame

pygame.init()
pygame.display.set_mode((1, 1))

from gamestate import GameState
from handlers import handle_lab_events
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

    def test_space_toggles_lab_pause(self):
        game = Game()
        game.open_lab()
        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_SPACE})

        handle_lab_events(game, event)

        self.assertTrue(game.lab_session.paused)
        self.assertFalse(game.lab_session.updates_enabled)
        handle_lab_events(game, event)
        self.assertFalse(game.lab_session.paused)

    def test_r_restores_the_fixed_player_start(self):
        game = Game()
        game.open_lab()
        expected_center = game.player_rect.center
        game.player_rect.move_ip(200, 150)

        handle_lab_events(
            game,
            pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_r}),
        )

        self.assertEqual(game.player_rect.center, expected_center)
        self.assertEqual(game.lab_session.reset_count, 1)
        self.assertFalse(game.lab_session.paused)

    def test_escape_returns_from_lab_to_menu(self):
        game = Game()
        game.open_lab()
        game.keys_pressed[pygame.K_w] = True

        handle_lab_events(
            game,
            pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_ESCAPE}),
        )

        self.assertEqual(game.state, GameState.MENU)
        self.assertFalse(any(game.keys_pressed.values()))


if __name__ == "__main__":
    unittest.main()
