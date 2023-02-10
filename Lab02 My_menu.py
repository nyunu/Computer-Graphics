from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys					

class MenuEvent:
    def __init__(self):
        self.objType = 1
        self.color = 'r'
        self.size = 0.0
    
    # display Event
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        # 색상 정의
        if self.color =='r':
            glColor3f(1.0, 0.0, 0.0)
        elif self.color =='g':
            glColor3f(0.0, 1.0, 0.0)
        elif self.color == 'b':
            glColor3f(0.0, 0.0, 1.0)
        elif self.color == 'c':
            glColor3f(0.5, 1.0, 1.0)
        elif self.color == 'm':
            glColor3f(1.0, 0.0, 1.0)
        elif self.color == 'y':
            glColor3f(1.0, 1.0, 0.0)

        # 도형 정의 / 도형 생성시에 size 변수를 사용해 크기가 변화할 수 있도록
        if self.objType==1:
            glutSolidSphere(0.2 + self.size, 15, 15)
        elif self.objType==2:
            glutWireSphere(0.2 + self.size, 15, 15)
        elif self.objType==3:
            glutSolidTorus(0.1 + self.size, 0.3 + self.size, 40, 20)
        elif self.objType==4:
            glutWireTorus(0.1 + self.size, 0.3 + self.size, 40, 20)
        elif self.objType==5:
            glutSolidTeapot(0.3 + self.size)
        elif self.objType==6:
            glutWireTeapot(0.3 + self.size)

        glFlush( )				

    # 키값에 따라 값 설정 / Keyboard Event
    def myKey(self, key,  X,  Y):
        print("key pressed", key)
        if key == b'q':
            sys.exit(0)
        elif key == b'x':
            self.size = self.size + 0.1
        elif key == b'y':
            self.size = self.size - 0.1
        elif key == b'r':
            self.color = 'r'
        elif key == b'g':
            self.color = 'g' 
        elif key == b'b':
            self.color = 'b' 
        elif key == b'c':
            self.color = 'c' 
        elif key == b'm':
            self.color = 'm'
        elif key == b'y':
            self.color = 'y' 
        
        glutPostRedisplay()

    # entryID 번호 부여
    def myMenu(self, id):
        entryID = int(id)
        if entryID == 1:
            self.objType = 1
        elif entryID == 2:
            self.objType = 2
        elif entryID == 3:
            self.objType = 3
        elif entryID == 4:
            self.objType = 4
        elif entryID == 5:
            self.objType = 5
        elif entryID == 6:
            self.objType = 6
        elif entryID == 7:
            self.color = 'r'
        elif entryID == 8:
            self.color = 'g'
        elif entryID == 9:
            self.color = 'b'
        elif entryID == 12:
            self.color = 'c'
        elif entryID == 13:
            self.color = 'm'
        elif entryID == 14:
            self.color = 'y'
        elif entryID == 10:
            self.size = self.size + 0.1
        elif entryID == 11:
            self.size = self.size - 0.1
        elif entryID == 99:
            sys.exit(0)
        glutPostRedisplay()  # 현재의 윈도우를 재생하도록 요구

    def main(self):
        # 윈도우 구성
        glutInit()
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500, 500)  	
        glutInitWindowPosition(0, 0)
        glutCreateWindow("OpenGL Menu Callback")
        self.objType = 1
        glClearColor (0.0, 0.0, 0.0, 1.0)	
        glMatrixMode(GL_PROJECTION);    
        glLoadIdentity()    
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
        
        # 메뉴 구성
        subSphere = glutCreateMenu(self.myMenu)
        glutAddMenuEntry("Solid Sphere", 1)
        glutAddMenuEntry("Wired Sphere", 2)

        subTorus = glutCreateMenu(self.myMenu)
        glutAddMenuEntry("Solid Torus", 3)
        glutAddMenuEntry("Wired Torus", 4)

        subTeapot = glutCreateMenu(self.myMenu)
        glutAddMenuEntry("Solid Teapot", 5)
        glutAddMenuEntry("Wired Teapot", 6)

        subShape = glutCreateMenu(self.myMenu)		
        glutAddSubMenu("Sphere", subSphere)	
        glutAddSubMenu("Torus", subTorus)	
        glutAddSubMenu("Teapot", subTeapot)	

        subColor = glutCreateMenu(self.myMenu)		
        glutAddMenuEntry("Red color", 7)
        glutAddMenuEntry("Green color", 8)
        glutAddMenuEntry("Blue color", 9)
        glutAddMenuEntry("Cyan color", 12)
        glutAddMenuEntry("Magenta color", 13)
        glutAddMenuEntry("Yellow color", 14)

        subSize = glutCreateMenu(self.myMenu)
        glutAddMenuEntry("Bigger (X)", 10)
        glutAddMenuEntry("Smaller (Y)", 11)

        MyMainMenuID = glutCreateMenu(self.myMenu)
        glutAddSubMenu("Shape", subShape)	
        glutAddSubMenu("Color", subColor)	
        glutAddSubMenu("Size", subSize)		
        glutAddMenuEntry("Exit", 99)
        
        glutAttachMenu(GLUT_RIGHT_BUTTON)

        # callback 함수 등록
        glutKeyboardFunc(self.myKey)
        glutDisplayFunc(self.display)		
        glutMainLoop()

m = MenuEvent()
m.main()