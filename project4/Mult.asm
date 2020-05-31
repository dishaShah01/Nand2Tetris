// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@R0
D=M
@n1   //n1=R0
M=D
@R1
D=M
@R2
M=0
@n2   //n2=R1
M=D
@i    //i=0
M=0
@result
M=0
(LOOP)
@i
D=M
@n2
D=D-M
@STOP
D;JEQ

@result
D=M
@n1
D=D+M
@result
M=D
@i
M=M+1
@LOOP
0;JMP

(STOP)
@result
D=M
@R2
M=D

(END)
@END
0;JMP



