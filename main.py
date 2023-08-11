# script to rename and organize "Danny The Airbrush Guy" tattoo stencils
import os
import cv2


directory = "G:\My Drive\Business Projects\Danny The Airbrush Guy\Tattoo Stencils"

# iterate over a list of all files in the directory
for filename in os.listdir(directory):
    # # Find directories with more than one img in it
    # f = os.path.join(directory, filename)
    # if len(os.listdir(f)) > 1:
    #     print(f)

    # Renaming process
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)    # Create window with freedom of dimensions    
    img = cv2.imread(f, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (700, 900))   
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # after viewing img enter image number and update files
    number = input()
    if not os.path.exists(f"{f.replace(filename, '')}\{number}"):
        os.makedirs(f"{f.replace(filename, '')}\{number}")
    os.rename(f, f"{f.replace(filename, '')}\{number}\{number}_stencil_pic.JPEG")
 
print('All images processed.')
