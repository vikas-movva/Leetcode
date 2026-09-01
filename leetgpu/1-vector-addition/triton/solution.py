# LeetGPU Solution
# Challenge: #1 · Vector Addition
# Language: Triton (triton)

import torch
import triton
import triton.language as tl


@triton.jit
def vector_add_kernel(a, b, c, n_elements, BLOCK_SIZE: tl.constexpr):
    # get program id
    pid = tl.program_id(0)
    
    # compute the start index for this block
    block_start = pid * BLOCK_SIZE
    
    # offset is a list of pointers to the elements in the block
    offset = block_start + tl.arange(0, BLOCK_SIZE)
    
    # mask to guard oob memory access
    mask = offset < n_elements
    
    # load the elements in the block
    x = tl.load(a + offset, mask=mask)
    y = tl.load(b + offset, mask=mask)
    
    # compute add
    out  = x + y
    
    # store the result in c
    tl.store(c + offset, out, mask=mask)


# a, b, c are tensors on the GPU
def solve(a: torch.Tensor, b: torch.Tensor, c: torch.Tensor, N: int):
    BLOCK_SIZE = 1024
    grid = (triton.cdiv(N, BLOCK_SIZE),)
    vector_add_kernel[grid](a, b, c, N, BLOCK_SIZE)
