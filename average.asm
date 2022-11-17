j L1
   




L1: 
addi $sp,$sp,40
move $s0,$sp
L2: 
li $v0,5
syscall
move $t1,$v0
sw $t1,-12($s0)
L3: 
li $t1,0
sw $t1,-16($s0)
L4: 
li $t1,0
sw $t1,-24($s0)
L5: 
lw $t1,-12($s0)
li $t2,1
bgt,$t1,$t2, L7
L6: 
b L12
L7: 
lw $t1,-16($s0)
lw $t2,-12($s0)
add,$t1,$t1,$t2
sw $t1,-28($s0)
L8: 
lw $t1,-28($s0)
sw $t1,-16($s0)
L9: 
lw $t1,-24($s0)
li $t2,1
add,$t1,$t1,$t2
sw $t1,-32($s0)
L10: 
lw $t1,-32($s0)
sw $t1,-24($s0)
L11: 
b L5
L12: 
lw $t1,-16($s0)
lw $t2,-24($s0)
div,$t1,$t1,$t2
sw $t1,-36($s0)
L13: 
lw $t1,-36($s0)
sw $t1,-20($s0)
L14: 
li $v0,1
lw $t1,-20($s0)
move $a0,$t1
syscall
L15: 
li $v0, 10
syscall
L16: 
