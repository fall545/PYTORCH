import torch
# x = torch.tensor([
#     [1],
#     [2],
#     [3],
#     [4],
#     [5],
#     [6]
# ],dtype=torch.float32) # input tensor
# y = torch.tensor([
#     [2],
#     [4],
#     [6],
#     [8],
#     [10],
#     [12]
# ],dtype=torch.float32)  # expected output
# w = torch.randn(1,1,dtype=torch.float32,requires_grad=True)
# # b = torch.randn(3, requires_grad=True)
# z = torch.matmul(x, w)
# loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)
x=torch.ones(10)
print(x)