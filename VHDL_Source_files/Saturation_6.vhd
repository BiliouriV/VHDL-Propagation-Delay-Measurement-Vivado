-----------------------------------------------------------------------------------
-- Company:
-- Engineer:
--
-- Create Date: Thu Oct  8 13:50:34 2020

-- Design Name:
-- Module Name: Saturation_6
-- Project Name:
-- Target Devices:
-- Tool Versions:
-- Description: Generated from Simulink Saturate Block
--
-- Dependencies:
--
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;


entity Saturation_6 is
	Port (
		in1 : in STD_LOGIC_VECTOR(@in1_minus@ DOWNTO 0); -- Fix13_-5
		out1 : out STD_LOGIC_VECTOR(@out1_minus@ DOWNTO 0) -- Fix13_-5
		);
end Saturation_6;
architecture Behavioral of Saturation_6 is
	signal l_lim : SIGNED(@in1_minus@ DOWNTO 0);
	signal u_lim : SIGNED(@in1_minus@ DOWNTO 0);
begin
	l_lim <= to_signed(-16#c80#, @in1_plus@); -- value=-100
	u_lim <= to_signed(16#c80#, @in1_plus@); -- value=100

	out1 <= std_logic_vector(l_lim) when signed(in1)<l_lim else
		std_logic_vector(u_lim) when signed(in1)>u_lim else
		in1;
end Behavioral;
