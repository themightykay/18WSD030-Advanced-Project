#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM PoC Rx host
# Author: KD - 6/12/18
# Generated: Mon Feb  4 19:43:18 2019
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
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import xmlrpclib
from gnuradio import qtgui


class FM_PoC_Rx_Host(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FM PoC Rx host")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FM PoC Rx host")
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

        self.settings = Qt.QSettings("GNU Radio", "FM_PoC_Rx_Host")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 44100
        self.rx_gain = rx_gain = 0
        self.freq = freq = 434e6
        self.bw = bw = 1e6
        self.audio_gain = audio_gain = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._freq_range = Range(70e6, 3000e6, 10e6, 434e6, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency (Hz)', "slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 0, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self._bw_range = Range(100e3, 50e6, 100e3, 1e6, 200)
        self._bw_win = RangeWidget(self._bw_range, self.set_bw, 'BandWidth', "slider", float)
        self.top_grid_layout.addWidget(self._bw_win, 2, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(2,3)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self._audio_gain_range = Range(0, 1000, 0.1, 0.5, 0)
        self._audio_gain_win = RangeWidget(self._audio_gain_range, self.set_audio_gain, 'Audio Gain', "dial", float)
        self.top_grid_layout.addWidget(self._audio_gain_win, 2, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(2,3)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]
        self.xmlrpc_client0_0 = xmlrpclib.Server('http://192.168.10.2:30000')
        self.xmlrpc_client0 = xmlrpclib.Server('http://192.168.10.2:30000')
        self.xmlrpc_client = xmlrpclib.Server('http://192.168.10.2:30000')
        self._rx_gain_range = Range(0, 70, 1, 0, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RF Gain', "slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win, 0, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_HAMMING, #wintype
        	freq, #fc
        	200e3, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
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

        labels = ['Channel 1', 'Channel 2', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.channel_2_stream_pull = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://192.168.10.2:9995', 100, False, -1)
        self.channel_1_stream_pull_0_0 = zeromq.pull_source(gr.sizeof_float, 1, 'tcp://192.168.10.2:9993', 100, False, -1)
        self.channel_1_stream_pull_0 = zeromq.pull_source(gr.sizeof_float, 1, 'tcp://192.168.10.2:9997', 100, False, -1)
        self.channel_1_stream_pull = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://192.168.10.2:9999', 100, False, -1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((audio_gain, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((audio_gain, ))
        self.audio_sink_0 = audio.sink(24000, '', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.audio_sink_0, 1))
        self.connect((self.channel_1_stream_pull, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.channel_1_stream_pull_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.channel_1_stream_pull_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.channel_2_stream_pull, 0), (self.qtgui_freq_sink_x_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "FM_PoC_Rx_Host")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.xmlrpc_client0.set_rx_gain(self.rx_gain)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.xmlrpc_client.set_freq(self.freq)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, 200e3)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.xmlrpc_client0_0.set_bw(self.bw)

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.audio_gain, ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.audio_gain, ))


def main(top_block_cls=FM_PoC_Rx_Host, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
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