%    SC MATLAB function combines two signals using Equal Gain Combining divesity technique, this is done by selecting the one
%with the best SNR.
%    Copyright (C) 2018  K. Dimantides
%
%    This program is free software: you can redistribute it and/or modify
%    it under the terms of the GNU Affero General Public License as published
%    by the Free Software Foundation, either version 3 of the License, or
%    (at your option) any later version.
%
%    This program is distributed in the hope that it will be useful,
%    but WITHOUT ANY WARRANTY; without even the implied warranty of
%    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
%    GNU Affero General Public License for more details.
%
%    You should have received a copy of the GNU Affero General Public License
%    along with this program.  If not, see <https://www.gnu.org/licenses/>.


function [combined_signal] = sc(channel_1_power,channel_2_power)
%Selection combining function combines two signals by selecting the one
%with the best SNR.
%   The selection combining function takes two input signals and combines
%   them by selecting the signal with the best SNR. The new combined
%   signal is then passed as an output argument.
a = zeros(1,length(channel_1_power)); % preallocating memory for variable a

channel_1_mag = db2mag(channel_1_power); % converting from power (dB) to magnitudes
channel_2_mag = db2mag(channel_2_power); % converting from power (dB) to magnitudes

for i=1:1:length(channel_1_power)
    if channel_1_mag(i) > channel_2_mag(i) % if ch1 is larger than ch2
        a(i) = channel_1_mag(i); % select ch1
    elseif channel_1_mag(i) <= channel_2_mag(i)
        a(i) = channel_2_mag(i); % select ch2
    end
end

combined_signal = mag2db(a); % convert all data back to power (dB)
end

