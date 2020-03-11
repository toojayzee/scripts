import sys, subprocess

max_brightness = 120000
file = r'/sys/class/backlight/intel_backlight/brightness'

def brightness(level):
  if int(level) > max_brightness:
    return 'Max brightness is 12000'
  else:
    subprocess.call(r'echo %s > %s' % (level, file))

if __name__ == '__main__':
  brightness(sys.argv[1])
    
     


