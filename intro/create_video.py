#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import argparse
import skimage
from skimage import novice
from skimage import io
from skimage import transform
import os
import numpy as np


# Main
if __name__ == "__main__":

    # Args
    parser = argparse.ArgumentParser(prog="create_video", description="Create introduction video")
    parser.add_argument("--logo", type=str, help="PNG image of the logo", required=True)
    parser.add_argument("--background", type=int, help="background red color", required=True)
    parser.add_argument("--logo-size", type=float, help="Logo resize factor", default=1.0)
    parser.add_argument("--width", type=int, help="Image width", default=1080)
    parser.add_argument("--height", type=int, help="Image height", default=720)
    parser.add_argument("--output", type=str, help="Output directory", default=".")
    args = parser.parse_args()

    # Open directory with image
    logo_image = io.imread(args.logo)
    base_image = np.zeros((args.height, args.width, 3), dtype='uint8')
    base_image[:, :, :] = args.background

    # Resize logo
    logo_image = transform.resize(
        logo_image,
        (logo_image.shape[0] * args.logo_size, logo_image.shape[1] * args.logo_size, 3)
    )

    # Put logo on base image
    base_image[:, :, :] = logo_image

    # Save image
    io.imsave(os.path.join(args.output, "test.png"), base_image)

# end if
