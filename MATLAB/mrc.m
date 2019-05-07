%    MRC MATLAB function combines two signals using Equal Gain Combining divesity technique, this is done by adding their
%squares and then getting the square root.
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

function [combined_signal] = mrc(channel_1_power,channel_2_power)
%Maximal ratio combining function combines two signals by adding their
%squares and then getting the square root.
%   The maximal-ratio combining takes two input signals and combines them
%   by adding their squares and then getting the square root. The new
%   combined signal is then passed as an output argument.
a = zeros(1,length(channel_1_power)); % preallocating memory for variable a
combined_signal = zeros(1,length(channel_1_power)); % preallocating memory for variable a1

channel_1_mag = db2mag(channel_1_power); % converting from power (dB) to magnitudes
channel_2_mag = db2mag(channel_2_power); % converting from power (dB) to magnitudes

i=1:1:length(channel_1_power); % generating index vector

a(i) = sqrt(channel_1_mag(i).^2+channel_2_mag(i).^2);
combined_signal(i) = mag2db(a(i)); % convert all data back to power (dB)
end

