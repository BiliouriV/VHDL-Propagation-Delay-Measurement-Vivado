-----------------------------------------------------------------------------------
-- Company:
-- Engineer:
--
-- Create Date: Thu Oct  8 13:50:34 2020

-- Design Name:
-- Module Name: Multiport_Switch_5
-- Project Name:
-- Target Devices:
-- Tool Versions:
-- Description: Generated from Simulink MultiPortSwitch Block
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


entity Multiport_Switch_5 is
	Port (
		in1 : in STD_LOGIC_VECTOR(@in1_minus@ DOWNTO 0); -- Fix5_-2
		in2 : in STD_LOGIC_VECTOR(@in2_minus@ DOWNTO 0); -- Fix13_-5
		in3 : in STD_LOGIC_VECTOR(@in3_minus@ DOWNTO 0); -- Fix13_-5
		out1 : out STD_LOGIC_VECTOR(@out1_minus@ DOWNTO 0) -- Fix13_-5
		);
end Multiport_Switch_5;
architecture Behavioral of Multiport_Switch_5 is
	signal id0 : signed(2 downto 0); -- integer part of Fix5_-2
	signal id1 : signed(2 downto 0); -- integer part of Fix5_-2
begin
	id0 <= to_signed(16#0#, 3); -- value=0
	id1 <= to_signed(16#1#, 3); -- value=1

	out1 <= in2 when id0 = signed(in1(4 downto 2)) else
			in3 when id1 = signed(in1(4 downto 2)) else
			in3; -- default case is the last case
end Behavioral;
