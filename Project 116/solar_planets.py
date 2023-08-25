import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sun",
            (150,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (00,00,255)
            )

cv2.putText(img,
            "Mercury",
            (110,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (00,00,255)
            )

cv2.putText(img,
            "Venus",
            (200,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (00,00,255)
            )

cv2.putText(img,
            "Earth",
            (290,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (00,00,255)
            )

cv2.putText(img,
            "Mars",
            (380,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (00,00,255)
            )

cv2.putText(img,
            "Jupiter",
            (550,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (00,00,255)
            )

cv2.putText(img,
            "Saturn",
            (770,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (00,00,255)
            )

cv2.putText(img,
            "Uranum",
            (965,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (00,00,255)
            )

cv2.putText(img,
            "Neptune",
            (1115,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (00,00,255)
            )
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)
