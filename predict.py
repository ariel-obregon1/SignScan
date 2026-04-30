import cv2
import mediapipe as mp
import pickle
import numpy as np
from collections import deque, Counter  # 👈 NUEVO

# Cargar modelo
with open("modelo.pkl", "rb") as f:
    model = pickle.load(f)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# 👇 historial de predicciones
historial = deque(maxlen=10)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    pred = ""
    pred_estable = ""  # 👈 NUEVO

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            fila = []
            base_x = hand_landmarks.landmark[0].x
            base_y = hand_landmarks.landmark[0].y
            base_z = hand_landmarks.landmark[0].z

            for lm in hand_landmarks.landmark:
                fila.extend([
                    lm.x - base_x,
                    lm.y - base_y,
                    lm.z - base_z
                ])

            fila = np.array(fila).reshape(1, -1)

            pred = model.predict(fila)[0]

            # 👇 guardar en historial
            historial.append(pred)

    # 👇 calcular predicción estable
    if len(historial) == historial.maxlen:
        conteo = Counter(historial)
        pred_estable = conteo.most_common(1)[0][0]

    # Mostrar predicción ESTABLE
    cv2.putText(
        frame,
        f"Letra: {pred_estable}",
        (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (0, 255, 0),
        3
    )

    cv2.imshow("Reconocimiento", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()