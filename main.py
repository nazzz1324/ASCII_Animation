import pyglet, sys, os, time

def animgif_to_ASCII_animation(animated_gif_path):
  # кортеж символов для анимации
  chars = ('#', '#', '@', '%', '=', '+', '*', ':', '-', '.', ' ')
  clear_console = 'clear' if os.name == 'posix' else 'CLS'

  # загрузка GIF
  anim = pyglet.image.load_animation(animated_gif_path)

  #Перебор кадров GIF
  while True:
    for frame in anim.frames:

      # Извлечение текущего кадра в градациях серого
      data = frame.image.get_data('L', frame.image.width)

      #Перебор пикселей
      outstr = ''
      for (i, pixel) in enumerate(data):
        # Преобразуем значение пикселя в строку перед использованием ord()
        index = int((ord(chr(pixel)) * (len(chars) - 1)) / 255)
        outstr += chars[index] + \
             ('\n' if (i + 1) % frame.image.width == 0 else '')

      # очистка консоли
      os.system(clear_console)

      sys.stdout.write(outstr)
      sys.stdout.flush()
      time.sleep(0.01)

animgif_to_ASCII_animation(u'gif.gif')
