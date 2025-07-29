import cv2 as cv
import numpy as np
#images to be in grayscale
img1 = cv.imread("form.jpg")
img2 = cv.imread("scanned-form.jpg")

img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

im1_gray = cv.cvtColor(img1 , cv.COLOR_BGR2GRAY)
im2_gray = cv.cvtColor(img2 , cv.COLOR_BGR2GRAY)

# create ORB detector
orb = cv.ORB_create(500)
#detect keypoints and compute descriptors
keypoint1 , descriptor1 = orb.detectAndCompute(im1_gray, None)
keypoint2, descriptor2 = orb.detectAndCompute(im2_gray,None)
#display the keypoints
img1_disp = cv.drawKeypoints(img1, keypoint1, outImage=None, color=(0,255,0), flags= cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img2_disp = cv.drawKeypoints(img2, keypoint2, outImage=None, color=(0,255,0), flags= cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#step3: match keypoints in the two image
#match features
matcher = cv.DescriptorMatcher_create(cv.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
# convert it into list for sorting and match
matches =list(matcher.match(descriptor1,descriptor2))
# sort matches
matches.sort(key=lambda x: x.distance, reverse=False)
#remove not so good matches
numGoodMatches = int(len(matches)*0.1)
matches =matches[:numGoodMatches]
#draw the top matches
img_matches = cv.drawMatches(img1 ,keypoints1= keypoint1,img2= img2 , keypoints2=keypoint2 , matches1to2=matches , outImg= None)

#step 4: find Homography
# Extract location of good matches
points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
    points1[i, :] = keypoint1[match.queryIdx].pt
    points2[i, :] = keypoint2[match.trainIdx].pt

# Find homography
h, mask = cv.findHomography(points2, points1, cv.RANSAC)
print(h)

#step5:
height, width , channel = img1.shape
#now wrapping on img_scan
output = cv.warpPerspective(img2, h , (width , height))

cv.namedWindow("window", cv.WINDOW_NORMAL)
out= np.hstack((output,img1))
cv.imshow("window", out)
cv.waitKey(0)
cv.destroyAllWindows()