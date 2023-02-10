from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class MovingBox:
    def __init__(self):
        self.x1 = 0.0 # box1과 box2의 초기위치를 다르게 설정하기 위해 각각 다른 값 넣어줌
        self.y1 = 0.0
        self.x2 = 50.0 
        self.y2 = 1000.0

        self.rsize = 25 
        self.xstep1 = 2.0 # 각 좌표의 이동하는 정도
        self.ystep1 = 2.0
        self.xstep2 = 2.0
        self.ystep2 = 2.0

        self.windowWidth = 100
        self.windowHeight=100
        self.speed = 33

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)
        glRectf(self.x1, self.y1, self.x1 + self.rsize, self.y1 - self.rsize)	    #box1

        glColor3f(0.0, 1.0, 0.0)
        glRectf(self.x2, self.y2, self.x2 + self.rsize, self.y2 - self.rsize)       #box2

        glutSwapBuffers()

    def TimerFunction(self, value):
        # first box
        if self.x1 > (self.windowWidth-self.rsize):	    # right wall - 오른쪽 벽에 부딪혔을 때 사각형의 왼쪽 모서리가 아닌 오른쪽 모서리가 닿음 따라서 windowwidth-rsize
            self.xstep1 = -self.xstep1
            self.x1 = self.windowWidth - self.rsize

        if self.x1 < -self.windowWidth:			        # left wall
            self.xstep1 = -self.xstep1
            self.x1 = -self.windowWidth; 

        if self.y1 > self.windowHeight:			        # top wall
            self.ystep1 = -self.ystep1
            self.y1 = self.windowHeight

        if self.y1 < (-self.windowHeight + self.rsize):	# bottom wall - 위와 같은 원리
            self.ystep1 = -self.ystep1
            self.y1 = -self.windowHeight + self.rsize     

        self.x1 += self.xstep1
        self.y1 += self.ystep1

        # second box
        if self.x2 > (self.windowWidth-self.rsize):	    # right wall
            self.xstep2 = -self.xstep2
            self.x2 = self.windowWidth - self.rsize

        if self.x2 < -self.windowWidth:			        # left wall
            self.xstep2 = -self.xstep2
            self.x2 = -self.windowWidth; 

        if self.y2 > self.windowHeight:			        # top wall
            self.ystep2 = -self.ystep2
            self.y2 = self.windowHeight

        if self.y2 < (-self.windowHeight + self.rsize):	# bottom wall
            self.ystep2 = -self.ystep2
            self.y2 = -self.windowHeight + self.rsize     

        self.x2 += self.xstep2
        self.y2 += self.ystep2

        # add second box

        glutPostRedisplay() # 앞서 수정된 변화 반영
        glutTimerFunc(self.speed, self.TimerFunction, 1) # timer콜백이 한번이 아닌 여러번 진행될 수 있도록
        
    def MyMainMenu(self, entryID): # entryID 번호 부여
    				
        if entryID == 1: #entryID가 1일때는 스피드 -10
            self.speed = self.speed - 10
        elif entryID == 2:
            self.speed = self.speed
        elif entryID == 3:
            self.speed = self.speed + 10

        glutPostRedisplay()
    			

    def ChangeSize(self, w, h):

        if (h == 0): h = 1
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = w / h # 가로로 늘어났는지, 세로로 늘어났는지
        if w <= h:
            self.windowWidth = 100
            self.windowHeight = 100 / aspectRatio   # use aspectRatio
            glOrtho(-100.0, 100.0, -self.windowHeight, self.windowHeight, 1.0, -1.0) # 뷰볼륨 재설정
        else:
            self.windowWidth = 100 * aspectRatio    # use aspectRatio
            self.windowHeight = 100
            glOrtho(-self.windowWidth, self.windowWidth, -100.0, 100.0, 1.0, -1.0) # 뷰볼륨 재설정

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        glutInitWindowSize(800, 600)
        glutCreateWindow("Timer CallBack")
        glutDisplayFunc(self.draw)
        glutReshapeFunc(self.ChangeSize)
        glutTimerFunc(self.speed, self.TimerFunction, 1)

        # 메뉴 구성
        subSphere = glutCreateMenu(self.MyMainMenu)
        glutAddMenuEntry("fast", 1)
        glutAddMenuEntry("normal", 2)
        glutAddMenuEntry("slow", 3)

        glutAttachMenu(GLUT_RIGHT_BUTTON)

        glutMainLoop()
            
d = MovingBox()
d.main()