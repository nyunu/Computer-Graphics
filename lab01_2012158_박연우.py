#Lab1-1(1)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class DrawingObject:
    def __init__(self):
        pass

    def display(self):      
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.5, 0.5, 0.5)   #색상정의
        glRectf(-0.2, 0.2, 0.2, -0.2)   #정사각형 그리기
        glFlush()

    def main(self):
        glutInit()      
        glutCreateWindow("Lab 01 - Drawing an Object")
        glClearColor (0.0, 0.0, 0.0, 1.0)  #배경 검은색으로 지우고
        glMatrixMode(GL_PROJECTION)  #투상 좌표계(GL_PROJECTION) 의 공간을 앞으로 계산하겠다는 뜻 / 투상 표현 전에 선언
        glLoadIdentity( )
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0) #현재 행렬에 직교 행렬을 곱함
        glutDisplayFunc(self.display)   
        glutMainLoop()

h = DrawingObject()
h.main()

#Lab1-1(2)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class DrawingObject:
    def __init__(self):
        pass

    def display(self):      
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)    #색상정의
        glRectf(-0.5, 0.5, 0.5, -0.5)   #정사각형 그리기
        glFlush()

    def main(self):
        glutInit()      
        glutCreateWindow("Lab 01 - Drawing an Object")
        glClearColor (0.0, 0.0, 0.0, 1.0)  #배경 검은색으로 지우고
        glMatrixMode(GL_PROJECTION)  #투상 좌표계(GL_PROJECTION) 의 공간을 앞으로 계산하겠다는 뜻 / 투상 표현 전에 선언
        glLoadIdentity( )
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0) #현재 행렬에 직교 행렬을 곱함
        glutDisplayFunc(self.display)   
        glutMainLoop()

h = DrawingObject()
h.main()        

#Lab1-1(2)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class DrawingObject:
    def __init__(self):
        pass

    def display(self):      
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 0.0)    #색상정의
        glRectf(-0.7, 0.7, 0.7, -0.7)   #도형 그리기
        glFlush()

    def main(self):
        glutInit()      
        glutCreateWindow("Lab 01 - Drawing an Object")
        glClearColor (0.0, 0.0, 0.0, 1.0)  #배경 검은색으로 지우고
        glMatrixMode(GL_PROJECTION)  #투상 좌표계(GL_PROJECTION) 의 공간을 앞으로 계산하겠다는 뜻 / 투상 표현 전에 선언
        glLoadIdentity( )
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0) #현재 행렬에 직교 행렬을 곱함
        glutDisplayFunc(self.display)   
        glutMainLoop()

h = DrawingObject()
h.main()        

#Lab1-1(3)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class DrawingObject:
    def __init__(self):
        pass

    def display(self):      
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 0.0)    #색상정의
        glRectf(-0.7, 0.7, 0.7, -0.7)   #도형그리기
        glFlush()

    def main(self):
        glutInit()      
        glutCreateWindow("Lab 01 - Drawing an Object")
        glClearColor (0.0, 0.0, 0.0, 1.0)  #배경 검은색으로 지우고
        glMatrixMode(GL_PROJECTION)  #투상 좌표계(GL_PROJECTION) 의 공간을 앞으로 계산하겠다는 뜻 / 투상 표현 전에 선언
        glLoadIdentity( )
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0) #현재 행렬에 직교 행렬을 곱함
        glutDisplayFunc(self.display)   
        glutMainLoop()


h = DrawingObject()
h.main()        

#Lab1-2(1)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class DrawingObject:
    def __init__(self):
        pass

    def display(self):      
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.0, 1.0, 0.0) #색상정의
        glutSolidSphere(0.5, 20, 20) #도형그리기
        glFlush()

    def main(self):
        glutInit()      
        glutCreateWindow("Lab 01 - Drawing an Object")
        glClearColor (0.0, 0.0, 0.0, 1.0)  #배경 검은색으로 지우고
        glMatrixMode(GL_PROJECTION)  #투상 좌표계(GL_PROJECTION) 의 공간을 앞으로 계산하겠다는 뜻 / 투상 표현 전에 선언
        glLoadIdentity( )
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0) #현재 행렬에 직교 행렬을 곱함
        glutDisplayFunc(self.display)   
        glutMainLoop()

h = DrawingObject()
h.main()        

#Lab1-2(2)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class DrawingObject:
    def __init__(self):
        pass

    def display(self):      
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.0, 1.0, 1.0)    #색상정의
        glutSolidTorus(0.2, 0.5, 20, 20)    #도형그리기
        glFlush()

    def main(self):
        glutInit()      
        glutCreateWindow("Lab 01 - Drawing an Object")
        glClearColor (0.0, 0.0, 0.0, 1.0)  #배경 검은색으로 지우고
        glMatrixMode(GL_PROJECTION)  #투상 좌표계(GL_PROJECTION) 의 공간을 앞으로 계산하겠다는 뜻 / 투상 표현 전에 선언
        glLoadIdentity( )
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0) #현재 행렬에 직교 행렬을 곱함
        glutDisplayFunc(self.display)   
        glutMainLoop()

h = DrawingObject()
h.main()        

#Lab1-2(3)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class DrawingObject:
    def __init__(self):
        pass

    def display(self):      
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 1.0)    #색상정의
        glutWireTorus(0.1, 0.5, 20, 20) #도형그리기
        glFlush()

    def main(self):
        glutInit()      
        glutCreateWindow("Lab 01 - Drawing an Object")
        glClearColor (0.0, 0.0, 0.0, 1.0)  #배경 검은색으로 지우고
        glMatrixMode(GL_PROJECTION)  #투상 좌표계(GL_PROJECTION) 의 공간을 앞으로 계산하겠다는 뜻 / 투상 표현 전에 선언
        glLoadIdentity( )
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0) #현재 행렬에 직교 행렬을 곱함
        glutDisplayFunc(self.display)   
        glutMainLoop()

h = DrawingObject()
h.main()        
