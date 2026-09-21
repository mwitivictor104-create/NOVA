"""
NOVA Interrupt System
Detects when the user wants to interrupt
and returns NOVA to listening mode.
"""

from brain.conversation.state import state


class InterruptManager:

    def __init__(self):
        self.interrupted = False


    def trigger(self):
        """
        User interrupted NOVA.
        Stop response and listen.
        """

        self.interrupted = True

        state.interrupt()


    def reset(self):
        """
        Clear interrupt status.
        """

        self.interrupted = False


    def is_interrupted(self):
        return self.interrupted


interrupt = InterruptManager()
