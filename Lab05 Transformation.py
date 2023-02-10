from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class SolarSystem:
    def __init__(self):
        self.myMenu = 1
        self.objType = 1
    
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.drawBox_a()

        if self.objType==1:  # 메뉴 생성을 위해 objType이 1,2,3,4일 때 실행할 명령어를 입력
            self.drawBox_a()
        elif self.objType==2:
            self.drawBox_b()
        elif self.objType==3:
            self.drawBox_c()
        elif self.objType==4:
            self.drawSolar()
        # call a draw function according to menu choice
        # ex. self.drawBox_a()
    
    def MyMainMenu(self, entryID): # 메뉴 생성을 위해 entryID 부여
        if entryID == 1:
            self.objType = 1
        elif entryID == 2:
            self.objType = 2
        elif entryID == 3:
            self.objType = 3
        elif entryID == 4:
            self.objType = 4
        glutPostRedisplay()
        
        
    def drawBox_a(self):
        glClear(GL_COLOR_BUFFER_BIT) # 배경 초기화
        glLoadIdentity() # 초기화 -> 초기 위치에
        glColor3f(1.0, 0.0, 0.0) # 색상이 빨간색인
        glutSolidCube(0.3) # 도형 그리기
        glTranslatef(-0.6, 0.0, 0.0) # x축으로 -0.6만큼 이동한 위치에
        glColor3f(0.0, 0.0, 1.0) # 색상이 파란색인
        glutSolidCube(0.3) # 도형 그리기
        glTranslatef(0.0, -0.6, 0.0) # y축으로 -0.6만큼 이동한 위치에
        glColor3f(1.0, 1.0, 0.0) # 색상이 노란색인
        glutSolidCube(0.3) # 도형 그리기
        glFlush()
    
    def drawBox_b(self):
        glClear(GL_COLOR_BUFFER_BIT) # 배경 초기화
        glLoadIdentity() # 초기화
        glColor3f(1.0, 0.0, 0.0) # 색상이 빨간색인
        glutSolidCube(0.3) # 도형 그리기
        glTranslatef(-0.6, 0.0, 0.0) # x축으로 -0.6만큼 이동하고
        glRotatef(45, 0.0, 0.0, 1.0) # 45도만큼 회전시켜서
        glColor3f(1.0, 1.0, 0.0) # 색상이 노란색인
        glutSolidCube(0.3) # 도형 그리기
        glFlush()

    def drawBox_c(self):
        glClear(GL_COLOR_BUFFER_BIT) # 배경 초기화
        glLoadIdentity() # 초기화
        glColor3f(1.0, 0.0, 0.0) # 색상이 빨간색인
        glutSolidCube(0.3) # 도형 그리기
        glRotatef(45, 0.0, 0.0, 1.0) # 45도 회전하고
        glTranslatef(-0.6, 0.0, 0.0) # 회전한 좌표축에서 -0.6만큼 x축 기준 이동
        glColor3f(1.0, 1.0, 0.0) # 색상이 노란색인
        glutSolidCube(0.3) # 도형 그리기
        glFlush()

    def drawSolar(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, 0.0)

        # sun
        glColor3f(1.0, 0.0, 0.0)
        glutSolidSphere(0.15, 15, 15)

        # Save the sun's position
        glPushMatrix()
        
        # move to the earth's position
        glTranslatef(0.6, 0.0, 0.0) 
        glColor3f(0.0, 1.0, 0.0) 
        # earth
        glutSolidSphere(0.1, 15, 15)

        # save the earth's position
        glPushMatrix()
        # moon
        glColor3f(1.0, 1.0, 1.0)
        # move to the moon position
        glTranslatef(0.0, 0.3, 0.0)
        glutSolidSphere(0.05, 15, 15)

        # back to the earth's position
        glPopMatrix()
        # back to the sun's position
        glPopMatrix()

        # draw mars
        # save sun's position
        glPushMatrix()
        glColor3f(0.0, 0.0, 1.0)
        glRotatef(-45, 0.0, 0.0, 1.0) # 45도 회전
        glTranslatef(-0.6, 0.0, 0.0) # 45도 회전한 좌표축 기준 -0.6만큼 x축 기준 이동
        # draw mars here
        glutSolidSphere(0.05, 15, 15)
        # back to the sun
        glPopMatrix()
        glFlush()

    def main(self):
        glutInit()			
        glutInitDisplayMode(GLUT_RGBA) 		
        glutInitWindowSize(600, 600)			
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Solar System")
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity( );    
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0) 	
        
        MyMainMenuID=glutCreateMenu(self.MyMainMenu) # 메뉴 생성
        glutAddMenuEntry("draw a",1)
        glutAddMenuEntry("draw b",2)
        glutAddMenuEntry("draw c",3)
        glutAddMenuEntry("draw solar",4)
        glutAttachMenu(GLUT_RIGHT_BUTTON)

        # register display callback 
        glutDisplayFunc(self.display)	  	
        glutMainLoop()

s = SolarSystem()
s.main()

        