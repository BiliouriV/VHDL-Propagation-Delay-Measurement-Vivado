-----------------------------------------------------------------------------------
-- Company:
-- Engineer:
--
-- Create Date: Thu Oct  8 13:50:34 2020

-- Design Name:
-- Module Name: Add_3
-- Project Name:
-- Target Devices:
-- Tool Versions:
-- Description: Generated from Simulink Sum Block
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


entity Add_3 is
	Port (
		in1 : in STD_LOGIC_VECTOR(@in1_minus@ DOWNTO 0); -- Fix13_-5
		in2 : in STD_LOGIC_VECTOR(@in2_minus@ DOWNTO 0); -- Fix13_-5
		out1 : out STD_LOGIC_VECTOR(@out1_minus@ DOWNTO 0) -- Fix13_-5
		);
end Add_3;
architecture Behavioral of Add_3 is
begin
	out1 <= std_logic_vector(0 + signed(in1) + signed(in2));
end Behavioral;
