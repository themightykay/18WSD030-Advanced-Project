#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: LoRa Rx host
# Author: KD - 1/3/19
# Generated: Wed Mar 27 17:00:09 2019
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fosphor
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import lora
import math
import pmt
import wx


class LoRa_Rx_Host(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="LoRa Rx host")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.spreading_factor = spreading_factor = 8
        self.samp_rate = samp_rate = 1000000
        self.offset = offset = 0
        self.ldr = ldr = False
        self.header = header = False
        self.freq = freq = 434e6
        self.code_rate = code_rate = 5
        self.bw_fft = bw_fft = 1e6
        self.bw = bw = 500e3

        ##################################################
        # Blocks
        ##################################################
        self.pfb_arb_resampler_xxx_0_0 = pfb.arb_resampler_ccf(
        	  bw/samp_rate,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0_0.declare_sample_delay(0)

        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  bw/samp_rate,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self.lora_demod_0_0 = lora.demod(spreading_factor, ldr, 25.0, 2)
        self.lora_demod_0 = lora.demod(spreading_factor, ldr, 25.0, 2)
        self.lora_decode_0_0 = lora.decode(spreading_factor, code_rate, ldr, header)
        self.lora_decode_0 = lora.decode(spreading_factor, code_rate, ldr, header)
        self.fosphor_wx_sink_c_0 = fosphor.wx_sink_c(
        	self.GetWin()
        )
        self.fosphor_wx_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_wx_sink_c_0.set_frequency_range(freq, samp_rate)
        self.Add(self.fosphor_wx_sink_c_0.win)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, 250e3,True)
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu("UDP_CLIENT", '127.0.0.1', '52003', 10000, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", '127.0.0.1', '52002', 10000, False)
        self.blocks_rotator_cc_0_0_0 = blocks.rotator_cc((2 * math.pi * offset) / samp_rate)
        self.blocks_rotator_cc_0_0 = blocks.rotator_cc((2 * math.pi * offset) / samp_rate)
        self.blocks_message_debug_0_0 = blocks.message_debug()
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/kyp/Documents/18WSD030-Advanced-Project/Targets/1/Kyp/data/433_LoRa_ch1', True)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/kyp/Documents/18WSD030-Advanced-Project/Targets/1/Kyp/data/433_LoRa_ch1', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lora_decode_0, 'out'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.lora_decode_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))
        self.msg_connect((self.lora_decode_0_0, 'out'), (self.blocks_message_debug_0_0, 'print'))
        self.msg_connect((self.lora_decode_0_0, 'out'), (self.blocks_socket_pdu_0_0, 'pdus'))
        self.msg_connect((self.lora_demod_0, 'out'), (self.lora_decode_0, 'in'))
        self.msg_connect((self.lora_demod_0_0, 'out'), (self.lora_decode_0_0, 'in'))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_rotator_cc_0_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_rotator_cc_0_0, 0))
        self.connect((self.blocks_rotator_cc_0_0, 0), (self.pfb_arb_resampler_xxx_0_0, 0))
        self.connect((self.blocks_rotator_cc_0_0_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.fosphor_wx_sink_c_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.lora_demod_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.lora_demod_0_0, 0))

    def get_spreading_factor(self):
        return self.spreading_factor

    def set_spreading_factor(self, spreading_factor):
        self.spreading_factor = spreading_factor

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.bw/self.samp_rate)
        self.pfb_arb_resampler_xxx_0.set_rate(self.bw/self.samp_rate)
        self.fosphor_wx_sink_c_0.set_frequency_range(self.freq, self.samp_rate)
        self.blocks_rotator_cc_0_0_0.set_phase_inc((2 * math.pi * self.offset) / self.samp_rate)
        self.blocks_rotator_cc_0_0.set_phase_inc((2 * math.pi * self.offset) / self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.blocks_rotator_cc_0_0_0.set_phase_inc((2 * math.pi * self.offset) / self.samp_rate)
        self.blocks_rotator_cc_0_0.set_phase_inc((2 * math.pi * self.offset) / self.samp_rate)

    def get_ldr(self):
        return self.ldr

    def set_ldr(self, ldr):
        self.ldr = ldr

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.fosphor_wx_sink_c_0.set_frequency_range(self.freq, self.samp_rate)

    def get_code_rate(self):
        return self.code_rate

    def set_code_rate(self, code_rate):
        self.code_rate = code_rate

    def get_bw_fft(self):
        return self.bw_fft

    def set_bw_fft(self, bw_fft):
        self.bw_fft = bw_fft

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.bw/self.samp_rate)
        self.pfb_arb_resampler_xxx_0.set_rate(self.bw/self.samp_rate)


def main(top_block_cls=LoRa_Rx_Host, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
