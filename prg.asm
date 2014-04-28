stv 10,0
stv 20,1
stv 21,2
stv 23,3
load 0,R1
load 1,R2
load 2,R3
load 3,R4
add R0,R1,R5
sub R2,R3,R6
mul R0,R1,R7
div R2,R3,R8


store R5,4
store R6,5
store R7,6
store R8,8

push R0
push R1
push R2

pop R0
pop R1
pop R2
stv 3,10
stv 4,11

call 35


halt

load 11,R0
load 10,R1
add R0,R1,R2
store R2,10
ret