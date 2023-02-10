from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class SolarSystem:

    def __init__(self):
        self.angle = 0.0
        self.angle2 = 0.0
        self.speed = 35
        self.depth = 1

    def menu(self, value):
        if value == 1: self.speed = 55   #fast # 빠를때, 보통때, 느릴때의 속도값 각각 지정
        elif value==2: self.speed = 35   #normal
        elif value==3: self.speed = 15   #slow
        elif value==4: self.depth = 1
        elif value==5: self.depth = 0
        glutPostRedisplay()  # create display event

    def display(self):
        glShadeModel(GL_SMOOTH)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # depth buffer = gbuffer

        if self.depth ==1:
            glEnable(GL_DEPTH_TEST)    #visibility test on # glEnable(GL_DEPTH_TEST) : GL_DEPTH_TEST가 사용되지 되도록 설정
        else:
            glDisable(GL_DEPTH_TEST)  # visibility test off : GL_DEPTH_TEST가 사용되지 않도록 설정

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        gluLookAt(0.0, 30.0, 300.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

        glColor3ub(200, 0, 200)
        glutSolidSphere(13.0, 15, 15);	# Sun

        glPushMatrix() # 태양 위치 저장
        glRotatef(self.angle, 0.0, 1.0, 0.0) # 지구 공전
        glTranslatef(70.0, 0.0, 0.0) # 지구와 태양 사이의 거리 # rotatef -> traslatef
        glColor3ub(0, 255, 0) # 지구 색 지정
        glutSolidSphere(8.0, 15, 15)	# Earth 그리기

        # Moon 지구의 위치를 저장하고 떠나야 함 -> 달도 지구처럼 지구 주위를 공전하면서 지구와 떨어져 있어야 함
        glPushMatrix()
        glRotatef(self.angle, 0.0, 1.0, 0.0) # 달 공전
        glTranslatef(20.0, 0.0, 0.0) # 달과 지구 사이 거리
        glColor3ub(255, 255, 0) # 달 색상 지정
        glutSolidSphere(4.0, 20, 20)  # 달을 그리는 코드 -> 크기 좀 작게 (,20,20)으로 변경
        glPopMatrix() # 달에서 지구로 돌아감

        glPopMatrix() # 지구에서 태양으로 돌아가기

        # Mars
        glPushMatrix() # 현재 위치 좌표 저장
        glRotatef(45, 0.0, 0.0, 1.0)  # z-rotation by 45 degree
        glRotatef(self.angle2, 0.0, 1.0, 0.0) # Mars 공전
        glTranslatef(-120.0, 0.0, 0.0) # Mars 위치로 이동 후
        glColor3ub(255, 0, 0) # Mars 색 지정
        glutSolidSphere(5.0, 20, 20) # Mars 그리기		

        #Mars' Moon
        glPushMatrix() # Mars의 위치 좌표 저장
        glRotatef(self.angle, 0.0, 1.0, 0.0) # 축 회전
        glTranslatef(20.0, 0.0, 0.0) # Mars;s moon의 위치로 이동 후
        glColor3ub(0, 0, 255) # Mars;s moon 색 지정
        glutSolidSphere(3.0, 20, 20) # Mars;s moon 그리기
        glPopMatrix() # Mars로 돌아가기
        glPopMatrix() # 태양으로 돌아가기

        glutSwapBuffers()
    

    def timerFunc(self, value):
    
        self.angle += 2.5
        if self.angle >= 360.0: self.angle = 0.0

        self.angle2 -= 2.5 # 지구와 반대로 회전해야 하기 때문에 -2.5를 해줌
        if self.angle2 <= -360.0: self.angle2 = 0.0 # -360도 이하가 되면 0으로 초기화

        glutPostRedisplay() # create display event
        glutTimerFunc(self.speed, self.timerFunc, 1) # Timer콜백함수 등록
    

    def changeSize(self, w, h):
        if (h == 0): h = 1
        aspect = w/h

        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        gluPerspective(45.0, aspect, 1.0, 1500.0)
        

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 600)
        glutCreateWindow("OpenGL Solar System")

        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glutReshapeFunc(self.changeSize)
        glutDisplayFunc(self.display)

        nMenu = glutCreateMenu(self.menu)
        glutAddMenuEntry("Slow", 1)
        glutAddMenuEntry("Normal", 2)
        glutAddMenuEntry("Fast", 3)
        glutAddMenuEntry("Depth Test On", 4)
        glutAddMenuEntry("Depth Test Off", 5)
        glutAttachMenu(GLUT_RIGHT_BUTTON)

        glutTimerFunc(self.speed, self.timerFunc, 1)
        glutMainLoop()

s = SolarSystem()
s.main()