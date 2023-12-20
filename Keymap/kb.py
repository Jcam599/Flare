import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.scanners.keypad import MatrixScanner

# from kmk.extensions.peg_rgb_matrix import Color







class KMKKeyboard(_KMKKeyboard):
    def __init__(
        self,
    ):
        # create and register the scanner(s)
        self.matrix = [
            MatrixScanner(
                # required arguments:
                column_pins=self.col_pins,
                row_pins=self.row_pins,
                # optional arguments with defaults:
                columns_to_anodes=self.diode_orientation,
                interval=0.02,  # Debounce time in floating point seconds
                max_events=64,
            ),
        ]

        # Split code:
        split = Split(
            split_flip=True,  # If both halves are the same, but flipped, set this True
            split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
            split_type=SplitType.UART,  # Defaults to UART
            uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
            data_pin=self.rx,  # The primary data pin to talk to the secondary device with
            data_pin2=self.tx,  # Second uart pin to allow 2 way communication
            use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
        )
        self.modules.append(split)

    col_pins = (
        board.D4,
        board.D5,
        board.D8,
        board.D9,
        board.D10,
    )
    row_pins = (
        board.D0,
        board.D1,
        board.D2,
        board.D3,
    )
    diode_orientation = DiodeOrientation.COL2ROW
    rx = board.D7
    tx = board.D6


