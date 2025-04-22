import cv2
import numpy as np

# Kamerayı aç
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Gri tonlara çevir ve bulanıklaştır
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Kenar tespiti
    edges = cv2.Canny(blurred, 200, 450)

    # Konturları bul
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Maksimum 5 şekil göstermek için sayaç
    shape_count = 0

    for contour in contours:
        if shape_count >= 5:  # Maksimum 5 şekil göstermek için sınır koy
            break

        # Konturu yaklaştırarak köşe sayısını bul
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        num_vertices = len(approx)

        # Şekli belirle
        shape = "Bilinmeyen"
        if num_vertices == 3:
            shape = "Triangle"
        elif num_vertices == 4:
            shape = "Rectangle"
        elif num_vertices > 8:
            shape = "Circle"

        # Şekli çerçevele ve ismini yazdır
        cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
        x, y = approx.ravel()[0], approx.ravel()[1] - 10
        cv2.putText(frame, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Şekil sayısını artır
        shape_count += 1

    # Görüntüyü göster
    cv2.imshow("Kamera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
