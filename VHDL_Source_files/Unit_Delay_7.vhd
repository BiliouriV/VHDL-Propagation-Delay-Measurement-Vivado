-----------------------------------------------------------------------------------
-- Company:
-- Engineer:
--
-- Create Date: Thu Oct  8 13:50:34 2020

-- Design Name:
-- Module Name: Unit_Delay_7
-- Project Name:
-- Target Devices:
-- Tool Versions:
-- Description: Generated from Simulink UnitDelay Block
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

entity Unit_Delay_7 is
	Port (
		CLK : in std_logic;
		in1 : in STD_LOGIC_VECTOR(12 DOWNTO 0); -- Fix13_-5
		out1 : out STD_LOGIC_VECTOR(12 DOWNTO 0) -- Fix13_-5
		);
end Unit_Delay_7;
architecture Behavioral of Unit_Delay_7 is
	signal in1_d1 : STD_LOGIC_VECTOR(12 DOWNTO 0) := std_logic_vector(to_signed(16#0#, 13)); -- value=0
begin

	process(CLK)
	begin
		if (CLK'event and CLK='1') then
			in1_d1 <= in1;
		end if;
	end process;

	out1 <= in1_d1;
end Behavioral;
