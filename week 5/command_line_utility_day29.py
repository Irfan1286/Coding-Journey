
import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    elif args.o == 'mul':
        return args.x * args.y

    else:
        return 'Please Give A Valid Input!'



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type= float, default=1.0,        # default is the default value if user doesnt input
                        help = 'Please contact Irfan to resolve the problem and provide the error code 00998x')
    parser.add_argument('--y', type= float, default=3.0,
                        help = 'Please contact Irfan to resolve the problem and provide the error code 009x0')
    parser.add_argument('--o', type= str, default='add',        # '--o' is the operator
                        help = 'Please try to input the correct term else provide helpline with error code 98vcx')

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))       # writing to console

# To open the console use powershell
