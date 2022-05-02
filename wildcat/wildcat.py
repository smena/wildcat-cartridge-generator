from webapp import app
import argparse
from Cartridge import Cartridge

def __init__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', '-c',
                        type=int,
                        help='Number of cartridges to generate',
                        default=1)
    args = parser.parse_args()

    cartridge = Cartridge.generate_cartridge(args)
    return cartridge