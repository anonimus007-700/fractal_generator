section .text
	global _start
	global julia_quadratic

_start:
	xor rax, rax
julia_quadratic:		; zx, zy, cx, cy, threshold
	push rbp
	mov rbp, rsp

	mov rax, [rbp+24]
	mov rbx, [rbp+32]
	mov rcx, [rbp+38]
	mov rdx, [rbp+46]
	mov rsi, [rbp+54]





;	mov rsi, rax
;	mov rax, 1
;	mov rdi, 1
;	mov rdx, 10
;	syscall
;
;	mov rax, 60
;	xor rdi, rdi
;	syscall




;	add rax, rbx
;	add rcx, rdx
;
;	xor rdx, rdx
;
;.loop:	inc rdx
;	cmp rdx, rsi
;	je .finish
;
;	shl rax, 1		; faster multiplication
;	mov rbx, rax
;	sub rbx, rax
;	add rax, rbx
;
;	add rax, rcx
;
;	and rax, 0x7FFFFFFF	; absolute value
;
;	cmp rax, 4
;	jnge .loop		; if rax > 4
;	mov rax, rdx
;	jmp exit
;
;.finish:
;	dec rsi
;	mov rax, rsi
;
exit:	mov rsp, rbp
	pop rbp
	ret

