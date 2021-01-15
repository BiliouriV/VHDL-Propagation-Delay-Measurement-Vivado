-----------------------------------------------------------------------------------
-- Company:
-- Engineer:
--
-- Create Date: Thu Oct  8 13:50:34 2020

-- Design Name:
-- Module Name: Const_1_4
-- Project Name:
-- Target Devices:
-- Tool Versions:
-- Description: Generated from Simulink Constant Block
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


entity Const_1_4 is
	Port (
		out1 : out STD_LOGIC_VECTOR(@out1_minus@ DOWNTO 0) -- Fix5_-2
		);
end Const_1_4;
architecture Behavioral of Const_1_4 is
	signal cst_signed : SIGNED(@out1_minus@ DOWNTO 0);
begin
	cst_signed <= to_signed(16#4#, @out1_plus@); -- value=1
	out1 <= std_logic_vector(cst_signed);
end Behavioral;
