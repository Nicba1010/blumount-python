from aenum import Enum


class SubPathType(Enum):
    RESERVED1 = 0
    RESERVED2 = 1
    PRIMARY_AUDIO_OF_BROWSABLE_SLIDESHOW = 2
    INTERACTIVE_GRAPHICS_PRESENTATION_MENU = 3
    TEXT_SUBTITLE_PRESENTATION = 4
    OUT_OF_MUX_SYNCHRONOUS_ELEMENTARY_STREAMS = 5
    OUT_OF_MUX_ASYNCHRONOUS_PICTURE_IN_PICTURE = 6
    IN_MUX_SYNCHRONOUS_PICTURE_IN_PICTURE = 7
