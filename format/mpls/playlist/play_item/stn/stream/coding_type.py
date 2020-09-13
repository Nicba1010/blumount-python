from aenum import Enum


class CodingType(Enum):
    MPEG1_VIDEO_PRIMARY_SECONDARY = 0x01
    MPEG2_VIDEO_PRIMARY_SECONDARY = 0x02
    MPEG4_AVC_VIDEO_PRIMARY_SECONDARY = 0x1B
    MPEG4_MVC_VIDEO_PRIMARY_SECONDARY = 0x20
    HEVC_VIDEO_PRIMARY_SECONDARY = 0x24
    VC1_VIDEO_PRIMARY_SECONDARY = 0xEA

    MPEG1_AUDIO_PRIMARY_SECONDARY = 0x03
    MPEG2_AUDIO_PRIMARY_SECONDARY = 0x04
    LPCM_AUDIO_PRIMARY = 0x80
    DOLBY_DIGITAL_AUDIO_PRIMARY = 0x81
    DTS_AUDIO_PRIMARY = 0x82
    DOLBY_DIGITAL_TRUEHD_AUDIO_PRIMARY = 0x83
    DOLBY_DIGITAL_PLUS_AUDIO_PRIMARY = 0x84
    DTS_HD_HIGH_RESOLUTION_AUDIO_PRIMARY = 0x85
    DTS_HD_MASTER_AUDIO_AUDIO_PRIMARY = 0x86
    DOLBY_DIGITAL_PLUS_AUDIO_SECONDARY = 0xA1
    DTS_HD_AUDIO_SECONDARY = 0xA2

    PRESENTATION_GRAPHICS_SUBTITLES = 0x90
    INTERACTIVE_GRAPHICS_MENU = 0x91

    TEXT_SUBTITLES = 0x92