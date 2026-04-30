import cv2
import mediapipe as mp

# Inicializar MediaPipe Hands (versión estable)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,  # Permitir hasta dos manos
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Iniciar cámara
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al leer frame")
        break

    # Voltear imagen (efecto espejo)
    frame = cv2.flip(frame, 1)

    # Convertir a RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar con MediaPipe
    result = hands.process(rgb)

    # Si detecta manos
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Detector de Manos", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()