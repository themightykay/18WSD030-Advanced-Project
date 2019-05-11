#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM SC Rx host
# Author: KD - 10/4/19
# Generated: Sat May 11 14:36:32 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import gr, blocks
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
import threading
import time
from gnuradio import qtgui


class FM_SC_Rx_Host(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FM SC Rx host")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FM SC Rx host")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "FM_SC_Rx_Host")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.sc = sc = 0
        self.samp_rate = samp_rate = 250000
        self.freq = freq = 434e6
        self.bw = bw = 1e6
        self.audio_gain = audio_gain = 0.5
        self.RMS_Value2 = RMS_Value2 = 0
        self.RMS_Value1 = RMS_Value1 = 0

        ##################################################
        # Blocks
        ##################################################
        self.switch = blocks.probe_signal_f()
        self.Value2 = blocks.probe_signal_f()
        self.Value1 = blocks.probe_signal_f()

        def _sc_probe():
            while True:
                val = self.switch.level()
                try:
                    self.set_sc(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (1000000))
        _sc_thread = threading.Thread(target=_sc_probe)
        _sc_thread.daemon = True
        _sc_thread.start()

        self._audio_gain_range = Range(0, 10, 0.01, 0.5, 0)
        self._audio_gain_win = RangeWidget(self._audio_gain_range, self.set_audio_gain, 'Audio Gain', "dial", float)
        self.top_grid_layout.addWidget(self._audio_gain_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)

        def _RMS_Value2_probe():
            while True:
                val = self.Value2.level()
                try:
                    self.set_RMS_Value2(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (1000000))
        _RMS_Value2_thread = threading.Thread(target=_RMS_Value2_probe)
        _RMS_Value2_thread.daemon = True
        _RMS_Value2_thread.start()


        def _RMS_Value1_probe():
            while True:
                val = self.Value1.level()
                try:
                    self.set_RMS_Value1(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (1000000))
        _RMS_Value1_thread = threading.Thread(target=_RMS_Value1_probe)
        _RMS_Value1_thread.daemon = True
        _RMS_Value1_thread.start()

        self.rms_ch2 = blocks.rms_cf(0.0001)
        self.rms_ch1 = blocks.rms_cf(0.0001)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=250000,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	20e3, #bw
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-90, 20)
        self.qtgui_freq_sink_x_0.set_y_label('Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['Ch1', 'Ch2', 'SC', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_threshold_ff_0_0 = blocks.threshold_ff(RMS_Value2<RMS_Value1, RMS_Value2<RMS_Value1, 1)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(RMS_Value2>RMS_Value1, RMS_Value2>RMS_Value1, 0)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((audio_gain, ))
        self.blocks_file_meta_source_0_0 = blocks.file_meta_source('/home/kyp/Documents/18WSD030-Advanced-Project/Kyp_measurements_backup/90_l2_50/433_FM_ch2', False, False, '')
        self.blocks_file_meta_source_0 = blocks.file_meta_source('/home/kyp/Documents/18WSD030-Advanced-Project/Kyp_measurements_backup/90_l2_50/433_FM_ch1', False, False, '')
        self.blks2_selector_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=sc,
        	output_index=0,
        )
        self.audio_sink_0 = audio.sink(24000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=250e3,
        	audio_decimation=1,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.blocks_file_meta_source_0, 0), (self.blks2_selector_0_0, 0))
        self.connect((self.blocks_file_meta_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_file_meta_source_0, 0), (self.rms_ch1, 0))
        self.connect((self.blocks_file_meta_source_0_0, 0), (self.blks2_selector_0_0, 1))
        self.connect((self.blocks_file_meta_source_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_file_meta_source_0_0, 0), (self.rms_ch2, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_threshold_ff_0_0, 0))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.switch, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.rms_ch1, 0), (self.Value1, 0))
        self.connect((self.rms_ch1, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.rms_ch2, 0), (self.Value2, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "FM_SC_Rx_Host")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sc(self):
        return self.sc

    def set_sc(self, sc):
        self.sc = sc
        self.blks2_selector_0_0.set_input_index(int(self.sc))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, 20e3)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.audio_gain, ))

    def get_RMS_Value2(self):
        return self.RMS_Value2

    def set_RMS_Value2(self, RMS_Value2):
        self.RMS_Value2 = RMS_Value2
        self.blocks_threshold_ff_0_0.set_hi(self.RMS_Value2<self.RMS_Value1)
        self.blocks_threshold_ff_0_0.set_lo(self.RMS_Value2<self.RMS_Value1)
        self.blocks_threshold_ff_0.set_hi(self.RMS_Value2>self.RMS_Value1)
        self.blocks_threshold_ff_0.set_lo(self.RMS_Value2>self.RMS_Value1)

    def get_RMS_Value1(self):
        return self.RMS_Value1

    def set_RMS_Value1(self, RMS_Value1):
        self.RMS_Value1 = RMS_Value1
        self.blocks_threshold_ff_0_0.set_hi(self.RMS_Value2<self.RMS_Value1)
        self.blocks_threshold_ff_0_0.set_lo(self.RMS_Value2<self.RMS_Value1)
        self.blocks_threshold_ff_0.set_hi(self.RMS_Value2>self.RMS_Value1)
        self.blocks_threshold_ff_0.set_lo(self.RMS_Value2>self.RMS_Value1)


def main(top_block_cls=FM_SC_Rx_Host, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
