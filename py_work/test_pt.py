from getchar import Getchar

from serial import Serial

sp = Serial('COM3', 115200, timeout=1)

def main(args=None):
    try:
        kb  = Getchar()
        key = ''
        # oldkey= ' '
        
        while key!='Q':
            key = kb.getch()
            if key == 'w':
                sp.write(('w').encode())
            elif key == 's':
                sp.write(('s').encode())
            elif key == 'a':
                sp.write(('a').encode())
            elif key == 'd':
                sp.write(('d').encode())
            elif key == 'i':
                sp.write(('i').encode())
            else:
                
                print(key)
    except KeyboardInterrupt:
        print("Program terminated!")

if __name__ == '__main__':
    main()
    

