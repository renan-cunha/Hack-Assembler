// Save the first addres in RAM[0] and RAM[2
@16384 // First Address
D=A
@0 
M=D
@2
M=D

// Set max address in RAM[1]
@24575 // Max Adress
D=A
@1
M=D

//Test if key is being presses
@24576
D=M
@10
D;JEQ

//Loop to make screen black
@2
A=M // Read current address
M=!M // invert bits on the current address
@2 
M=M+1 //increment the current address
D=M // save current address on D
@1
D=D-M // current address - max address
@14
D;JLE

//Holds black screen
@24576
D=M
@24
D;JNE

@2
M=M-1 //decrease current address by one

//Loop to make screen white
@2
A=M // Read current address
M=!M // invert bits on the current address
@2 
M=M-1 //decrement the current address
D=M // save current address on D
@0
D=D-M // current address - min address
@30
D;JGE

@2
M=M+1 //increse current address
@10 
M;JMP
