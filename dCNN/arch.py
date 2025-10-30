import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 128, 10, offset="(0,0,0)", to="(0,0,0)", height=8, depth=16, width=2),
    to_BN("bn1", 128, 128, offset="(0,0,0)", to="(conv1-east)", height=8, depth=16, width=1),
    to_Relu("relu1", 128, 128, offset="(0,0,0)", to="(bn1-east)", height=8, depth=16, width=1),
    to_Conv("conv2", 128, 128, offset="(1.8,0,0)", to="(conv1-east)", height=16, depth=16, width=5),
    to_connection("relu1", "conv2"),
    to_BN("bn2", 128, 128, offset="(0,0,0)", to="(conv2-east)", height=16, depth=16, width=1),
    to_Relu("relu2", 128, 128, offset="(0,0,0)", to="(bn2-east)", height=16, depth=16, width=1),
    to_Conv("conv3", 256, 128, offset="(2.5,0,0)", to="(conv2-east)", height=32, depth=32, width=5),
    to_connection("relu2", "conv3"),
    to_BN("bn3", 256, 128, offset="(0,0,0)", to="(conv3-east)", height=32, depth=32, width=1),
    to_Relu("relu3", 256, 128, offset="(0,0,0)", to="(bn3-east)", height=32, depth=32, width=1),
    to_Conv("conv4", 256, 256, offset="(3,0,0)", to="(conv3-east)", height=32, depth=32, width=10),
    to_connection("relu3", "conv4"),
    to_Conv("conv5", 256, 256, offset="(3,0,0)", to="(conv4-east)", height=32, depth=32, width=10),
    to_BN("bn4", 256, 256, offset="(0,0,0)", to="(conv4-east)", height=32, depth=32, width=1),
    to_Relu("relu4", 256, 256, offset="(0,0,0)", to="(bn4-east)", height=32, depth=32, width=1),
    to_connection("relu4", "conv5"),
    to_BN("bn5", 256, 256, offset="(0,0,0)", to="(conv5-east)", height=32, depth=32, width=1),
    to_Relu("relu5", 256, 256, offset="(0,0,0)", to="(bn5-east)", height=32, depth=32, width=1),
    to_Pool("gap", offset="(3,0,0)", to="(conv5-east)", height=32, depth=32, width=1),
    to_connection("relu4", "gap"),
    to_SoftMax("fc1", 256 ,"(2,0,0)", "(gap-east)"),
    to_connection("gap", "fc1"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()