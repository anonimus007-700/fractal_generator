section .data
	fln dq "0.0001", 0
	flm dq 1.1111
	fmt db "%f", 10, 0

section .text
	global _start
	global julia_quadratic

	extern atof
	extern printf

_start:
	xor rax, rax
julia_quadratic:		; zx, zy, cx, cy, threshold
	push rbp
	mov rbp, rsp

	mov rax, [rbp+24]
	mov rbx, [rbp+32]
	mov rcx, [rbp+40]
	mov rdx, [rbp+48]
	mov rsi, [rbp+56]

	lea rdi, [rax]
	call atof


	mov rax, 60
	xor rdi, rdi
	syscall

