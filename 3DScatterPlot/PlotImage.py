import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import os.path
# https://matplotlib.org/users/colors.html
# https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
# https://imgur.com/a/aRBd1
# Colors are an RGB or RGBA tuple of floats in [0, 1]
# colors = [tuple(image[r, c,:] / 255) for r in range(image.shape[0]) for c in range(image.shape[1])]

def plot(imagePath, points=10000, pprint=False, save=False, display=True):
    """
    Plot an image as a 3D scatter plot

    imagePath: Filepath for image to plot. Must be small or this will take forever
    """
    image = mpimg.imread(imagePath)
    pixels = image.shape[0] * image.shape[1]
    # Sample the image N times, where N=points. Call this smallImage
    sampleRate = max(pixels // points, 1)
    flatImage = np.reshape(image, (pixels, 3))
    smallImage = flatImage[::sampleRate, ... ]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = [tuple(smallImage[r,:] / 255) for r in range(smallImage.shape[0])]
    ax.scatter(
        smallImage[:,0],
        smallImage[:,1],
        smallImage[:,2], c=colors, s=16,alpha=1 )
    if pprint:
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])
    else:
        ax.set_title(os.path.basename(imagePath), y=1.1)
        ax.set_xlabel('Red')
        ax.xaxis.label.set_color('red')
        ax.set_ylabel('Green')
        ax.yaxis.label.set_color('green')
        ax.set_zlabel('Blue')
        ax.zaxis.label.set_color('blue')

        # Print the original image in top left corner
        aspectRatio = image.shape[0] / image.shape[1]
        height = 0.4
        width = height * aspectRatio
        # [left, bottom, width, height]
        imageaxis = fig.add_axes([0., 1.0 - height, height * aspectRatio, height], anchor = "NW")
        imageaxis.imshow(image)
        imageaxis.axis('off')

    # Draw each axis pane with RGB in pastel colors
    ax.w_xaxis.set_pane_color((255/255, 189/255, 189/255, 255/255))
    ax.w_yaxis.set_pane_color((225/255,247/255,213/255,255/255))
    ax.w_zaxis.set_pane_color((201/255,201/255,255/255,255/255))

    # Allow to save - change filename based on prettyprint setting
    if save:
        if pprint:
            plt.savefig(prepend_pprint(path, 'pprint-'))
        else:
            plt.savefig(prepend_pprint(path, 'print-'))
    if display:
        plt.show()

def prepend_pprint(path, prefix):
    """ Adds prefix before the filepath name """
    (head, tail) = os.path.split(path)
    return os.path.join(head, prefix + tail)


def is_valid_image(arg):
    """
    Verifies that a given argument is a valid image files

    arg: string representing filepath

    Returns
    -------
    img : A W*H*3 array representing a color image
    """

    if not os.path.isfile(arg):
        raise argparse.ArgumentTypeError(f"{arg} does not exist!")
    else:
        try:
            img = mpimg.imread(arg)
            return arg
        except IOError:
            raise argparse.ArgumentTypeError(f"{arg} isn't a valid image file!")
        except:
            raise argparse.ArgumentTypeError(f"Something wrong with input files")

if __name__ =="__main__":
    parser = argparse.ArgumentParser(description='Creates a 3D scatter plot of the colors present in an image')
    parser.add_argument('input_files', metavar='IMG_PATHS', nargs='+',
                        type=is_valid_image, help="Image filepaths to plot")
    parser.add_argument('-p', '--points', type=int, metavar="Pts",
                        default=10000, help="Max number of pixels to plot")
    parser.add_argument('-pp', '--pprint', help='Prints the scatter plots without extra information', action='store_true' )
    parser.add_argument('-s', '--save', help='Saves each plot prefixed with pprint- or print-', action='store_true')
    parser.add_argument('--nodisplay', help="Don't graph plots", action='store_true')
    args = parser.parse_args()
    for path in args.input_files:
        plot(path, args.points, args.pprint, args.save, not args.nodisplay)
