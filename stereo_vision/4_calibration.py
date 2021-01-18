# Copyright (C) 2019 Eugene Pomazov, <stereopi.com>, virt2real team
#
# This file is part of StereoPi tutorial scripts.
#
# StereoPi tutorial is free software: you can redistribute it 
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the 
# License, or (at your option) any later version.
#
# StereoPi tutorial is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with StereoPi tutorial.  
# If not, see <http://www.gnu.org/licenses/>.
#
# Most of this code is updated version of 3dberry.org project by virt2real
# 
# Thanks to Adrian and http://pyimagesearch.com, as there are lot of
# code in this tutorial was taken from his lessons.
# 

import os
import cv2
import numpy as np
import json
from stereovision.calibration import StereoCalibrator
from stereovision.calibration import StereoCalibration
from stereovision.exceptions import ChessboardNotFoundError


# Global variables preset
total_photos = 30
photo_width = 3840
photo_height = 1440
img_width = int(photo_width/2)
img_height = photo_height
image_size = (img_width,img_height)

# Chessboard parameters
rows = 6
columns = 9
square_size = 0.9330709


calibrator = StereoCalibrator(rows, columns, square_size, image_size)
photo_counter = -1
print ('Start cycle')
def getImagePath(width, height, num):
    return './pairsE/chess_'+str(num)+"_"+str(width)+'x'+str(height)+'.jpg'

while photo_counter != total_photos-1:
  photo_counter = photo_counter + 1
  print ('Import pair No ' + str(photo_counter))
  # leftName = './pairsA/left_'+str(photo_counter).zfill(2)+'.png'
  # rightName = './pairsA/right_'+str(photo_counter).zfill(2)+'.png'
  leftName = rightName = getImagePath(photo_width, photo_height, photo_counter)
  if os.path.isfile(leftName) and os.path.isfile(rightName):
      pair_img = cv2.imread(leftName, 1)
      # imgLeft = cv2.imread(leftName,1)
      # imgRight = cv2.imread(rightName,1)
      imgLeft = pair_img[0:photo_height, 0:img_width]  # Y+H and X+W
      imgRight = pair_img[0:photo_height, img_width:photo_width]  # Y+H and X+W
      try:
        calibrator._get_corners(imgLeft)
        calibrator._get_corners(imgRight)
      except ChessboardNotFoundError as error:
        print (error)
        print ("Pair No "+ str(photo_counter) + " ignored")
      else:
        calibrator.add_corners((imgLeft, imgRight), False)
        
print ('End cycle')


print ('Starting calibration... It can take several minutes!')
calibration = calibrator.calibrate_cameras()
calibration.export('calib_resultE')
print ('Calibration complete!')


# Lets rectify and show last pair after  calibration
calibration = StereoCalibration(input_folder='calib_resultE')
rectified_pair = calibration.rectify((imgLeft, imgRight))

cv2.imshow('Left CALIBRATED', rectified_pair[0])
cv2.imshow('Right CALIBRATED', rectified_pair[1])
cv2.imwrite("rectifyed_left.jpg",rectified_pair[0])
cv2.imwrite("rectifyed_right.jpg",rectified_pair[1])
cv2.waitKey(0)
