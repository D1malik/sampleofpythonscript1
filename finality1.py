import cv2
from PIL import Image


image_path = 'cat1.jpeg'
glasses_path = 'glasses1.png'
hat_path = 'giogio1.png'
cascade_path = 'haarcascade_frontalcatface_extended.xml'

cat_face_cascade = cv2.CascadeClassifier(cascade_path)

# Загрузка изображения
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)

# Загрузка изображений через PIL
cat = Image.open(image_path).convert("RGBA")
glasses = Image.open(glasses_path).convert("RGBA")
hat = Image.open(hat_path).convert("RGBA")

# Обработка каждой мордочки
for (x, y, w, h) in cat_face:
    # Нарисовать прямоугольник для отладки
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)

    # === Очки ===
    resized_glasses = glasses.resize((w, int(h / 3)))
    cat.paste(resized_glasses, (x, y + int(h / 3)), resized_glasses)

    # === Колпак ===
    resized_hat = hat.resize((w, int(h * 1.2)))  # увеличиваем размер колпака
    hat_x = x
    hat_y = y - int(h * 0.9)  # поднимаем выше головы
    if hat_y < 0:
        hat_y = 0
    cat.paste(resized_hat, (hat_x, hat_y), resized_hat)

# Сохранение и показ результата
output_path = "cat_with_glasses_and_hat.png"
cat.save(output_path)
result = cv2.imread(output_path)
cv2.imshow("Cat with glasses and hat", result)
cv2.waitKey(0)
cv2.destroyAllWindows()



