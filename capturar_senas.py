import cv2
import mediapipe as mp
import csv
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

label = input("Letra que vas a capturar: ")

# Control de tiempo
ultimo_guardado = 0
intervalo = 0.2  # segundos

contador = 0  # 👈 contador de muestras

with open("datos.csv", mode="a", newline="") as f:
    writer = csv.writer(f)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                tiempo_actual = time.time()

                if tiempo_actual - ultimo_guardado > intervalo:
                    base_x = hand_landmarks.landmark[0].x
                    base_y = hand_landmarks.landmark[0].y
                    base_z = hand_landmarks.landmark[0].z
                    fila = [label]
                    for lm in hand_landmarks.landmark:
                        fila.extend([
                            lm.x - base_x,
                            lm.y - base_y,
                            lm.z - base_z
    ])
                    writer.writerow(fila)
                    ultimo_guardado = tiempo_actual

                    contador += 1  # 👈 suma 1
                    print(f"Muestras: {contador}")

        # 👇 Mostrar contador en pantalla
        cv2.putText(
            frame,
            f"Muestras: {contador}",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Captura", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()