import argparse
def parse_args():
    parser = argparse.ArgumentParser(
        description='test argparse function')
    parser.add_argument('path', help='test path')
    parser.add_argument('-o', '--out', 
                        help='output date',
                        default=10,
                        type=int)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    print(args)
    path = args.path
    out = args.out
    print(f"path is : {path}")
    print(f"out is : {out}")

if __name__ == '__main__':
    main()

'''
结果为：
(py310) C:\my_project\MMSegmentation\3mmseg\demo>python demo_argparse.py ../demo --out 2
path is : ../demo
out is : 2
'''

