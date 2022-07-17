import cv2
import matplotlib.pyplot as plt
import pyperclip


img = cv2.imread("C:\\Users\\elliot\\Desktop\\NewOpenCV\\mrrob.png")

layer = img.copy()

for i in range(4):
	plt.subplot(2, 2, i + 1)

	# using pyrDown() function
	layer = cv2.pyrDown(layer)

	plt.imshow(layer)
	cv2.imshow("str(i)", layer)
	cv2.waitKey(0)
	

cv2.destroyAllWindows()
