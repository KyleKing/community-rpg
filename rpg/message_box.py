import arcade

from rpg.constants import MESSAGE_BOX_FONT_SIZE, MESSAGE_BOX_MARGIN


class MessageBox:
    def __init__(self, view, message, notes=None):
        self.message = message
        self.notes = notes
        self.view = view
        self.width = 500
        self.height = 50

    def on_draw(self):
        cx = self.view.window.width / 2
        cy = self.view.window.height - self.view.window.height / 8

        arcade.draw_rectangle_filled(
            cx,
            cy,
            self.width + MESSAGE_BOX_MARGIN * 2,
            self.height + MESSAGE_BOX_MARGIN * 2,
            arcade.color.ALMOND,
        )
        arcade.draw_rectangle_outline(
            cx,
            cy,
            self.width + MESSAGE_BOX_MARGIN * 2,
            self.height + MESSAGE_BOX_MARGIN * 2,
            arcade.color.ALLOY_ORANGE,
            4,
        )
        arcade.draw_text(
            self.message,
            cx,
            cy if not self.notes else cy + 10,
            arcade.color.ALLOY_ORANGE,
            MESSAGE_BOX_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=500,
        )
        if self.notes:
            arcade.draw_text(
                self.notes,
                cx,
                cy - 15,
                arcade.color.ALLOY_ORANGE,
                MESSAGE_BOX_FONT_SIZE / 2,
                anchor_x="center",
                anchor_y="center",
                align="center",
                width=500,
            )

    def on_key_press(self, _key, _modifiers):
        self.view.close_message_box()
