@16384
D=A
@0
M=D
@2
M=D
@24575
D=A
@1
M=D
@24576
D=M
@10
D;JEQ
@2
A=M
M=!M
@2
M=M+1
D=M
@1
D=D-M
@14
D;JLE
@24576
D=M
@24
D;JNE
@2
M=M-1
@2
A=M
M=!M
@2
M=M-1
D=M
@0
D=D-M
@30
D;JGE
@2
M=M+1
@10
M;JMP