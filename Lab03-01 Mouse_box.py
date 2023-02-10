from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class DrawingBox:
    def __init__(self):
        self.TopLeftX=0.0
        self.TopLeftY=0.0
        self.BottomRightX=0.0
        self.BottomRightY=0.0
        self.drawing=False
        self.color = 'r'

    def MyDisplay(self):	
        glViewport(0, 0, 500, 500) # 윈도우 크기에 맞춰 뷰포트 지정
        glClear(GL_COLOR_BUFFER_BIT)

        if self.color == 'r':
            glColor3f(1.0, 0.0, 0.0)
        elif self.color == 'g':
            glColor3f(0.0, 1.0, 0.0)
        elif self.color == 'b':
            glColor3f(0.0, 0.0, 1.0)
        elif self.color == 'c': # 색상지정 -> c, m, y 색상 추가
            glColor3f(0.0, 1.0, 1.0)
        elif self.color == 'm':
            glColor3f(1.0, 0.0, 1.0)
        elif self.color == 'y':
            glColor3f(1.0, 1.0, 0.0)

        glBegin(GL_POLYGON) 
        glVertex3f(self.TopLeftX/500.0, (500-self.TopLeftY)/500.0, 0.0)    # 좌표 정규화	  
        glVertex3f(self.TopLeftX/500.0, (500-self.BottomRightY)/500.0, 0.0)
        glVertex3f(self.BottomRightX/500.0, (500-self.BottomRightY)/500.0, 0.0)     	  
        glVertex3f(self.BottomRightX/500.0, (500-self.TopLeftY)/500.0, 0.0)
        glEnd()
        glFlush()			

    def MyKeyboard(self, KeyPressed, X, Y):
        if KeyPressed == b'r': # 눌려지는 키보드에 따라 색상 지정
            self.color = 'r'
        elif KeyPressed == b'g':
            self.color = 'g'
        elif KeyPressed == b'b':
            self.color = 'b'
        elif KeyPressed == b'c':
            self.color = 'c'
        elif KeyPressed == b'm':
            self.color = 'm'
        elif KeyPressed == b'y':
            self.color = 'y'

    def MyMouseClick(self, Button, State, X, Y):	
        if Button==GLUT_LEFT_BUTTON and State==GLUT_DOWN:	# 왼쪽 마우스 눌렸을 때 현좌표를 각각 topleftX와 topleftY에 저장
            self.TopLeftX = X
            self.TopLeftY = Y
            self.drawing = True # drawing값을 True로 지정
        if Button==GLUT_RIGHT_BUTTON and State==GLUT_DOWN:	# 오른쪽 마우스 눌렸을 때 현좌표를 각각 topleftX와 topleftY에 저장
            self.TopLeftX = X
            self.TopLeftY = Y
            self.drawing = False # drawing값을 False로 지정

    def MyMouseMove(self, X, Y):
        if self.drawing == False: # drawing값이 False이면
            self.BottomRightX = self.TopLeftX # topleftX와 bottomrightx를 같게 해 그림이 그려지지 않도록
            self.BottomRightY = self.TopLeftY # y좌표도 마찬가지로 처리
            glutPostRedisplay()
        if self.drawing == True: #drawing값이 True이면
            self.BottomRightX = X # 정상적으로 그림이 그려지도록 현좌표를 bottomrightx와 bottomrighty에 저장
            self.BottomRightY = Y
            glutPostRedisplay()

    def main(self):
        glutInit()				
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500, 500)    	
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Mouse CallBack")
        #glClearColor(1.0, 1.0, 1.0, 1.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0) 				
        glutDisplayFunc(self.MyDisplay) 
        glutKeyboardFunc(self.MyKeyboard) # 키보드 콜백함수
        glutMouseFunc(self.MyMouseClick) # 마우스 콜백함수
        glutMotionFunc(self.MyMouseMove) # 마우스 콜백함수	
        glutMainLoop()

m = DrawingBox()
m.main()
